import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

st.set_page_config(page_title="Public Policy RAG Demo v2: Azure Multi-Doc", layout="centered")

st.markdown("""
<style>
    .block-container {max-width: 900px; padding-top: 1rem; padding-bottom: 3rem;}
    .main {background-color: #f8f9fa;}
    h1 {color: #2c3e50; text-align: center;}
    h3 {color: #34495e;}
    .stMarkdown {font-size: 1.1rem; line-height: 1.6;}
</style>
""", unsafe_allow_html=True)

st.title("Public Policy RAG Demo v2: Multi-Document CMS Policy Retrieval (Personal Project)")

# (Keep your preferred text block from last—Version 1 with examples no quotes)

# Hardcoded PDFs
pdf_files = [
    "cms_ncci_2025_policy_manual.pdf",
    "2025-2026-medicaid-rate-guide-082025.pdf",
    "managed-care-compliance-toolkit.pdf"
]

# Azure config from env vars (set in App Service)
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    azure_deployment="gpt-4o-mini-embedding"  # If separate embedding deployment, or use chat model
)

llm = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    temperature=0.05
)

vector_store = AzureSearch(
    azure_search_endpoint=AZURE_SEARCH_ENDPOINT,
    azure_search_key=AZURE_SEARCH_KEY,
    index_name="rag-index",
    embedding_function=embeddings.embed_query
)

@st.cache_resource
def load_and_index_documents():
    if vector_store.index_exists():
        return vector_store
    
    missing = [f for f in pdf_files if not os.path.exists(f)]
    if missing:
        st.error(f"Missing PDFs for local indexing: {missing}. Cloud uses managed index.")
        st.stop()
    
    st.info(f"Processing 3 PDFs locally for index...")
    
    docs = []
    for pdf in pdf_files:
        loader = PyPDFLoader(pdf)
        docs.extend(loader.load())
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
    splits = splitter.split_documents(docs)
    
    vector_store.add_documents(splits)
    st.success("Azure multi-document index ready!")
    
    return vector_store

retriever = load_and_index_documents().as_retriever(search_kwargs={"k": 12})

# Prompt & chain (same as v2)
# (Keep your prompt/format_docs/chain/chat from previous)

st.caption("Personal open-source project v2—feedback welcome! Public documents only.")