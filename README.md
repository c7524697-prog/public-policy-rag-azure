# Public Policy RAG Demo v2: Multi-Document CMS Policy Retrieval (Personal Project)

Personal open-source project exploring retrieval-augmented generation (RAG) for policy and compliance research.  
v2 adds multi-document support: Merged indexing of three public CMS documents for cross-document queries.

Answers grounded exclusively in these official public documents (freely downloadable):
- 2025 Medicaid NCCI Policy Manual (coding edits/guidelines): [CMS link](https://www.cms.gov/files/document/2025nccimedicaidpolicymanualcomplete.pdf)
- 2025-2026 Medicaid Managed Care Rate Development Guide (rate setting): [CMS link](https://www.medicaid.gov/medicaid/managed-care/downloads/2025-2026-medicaid-rate-guide-082025.pdf)
- Medicaid and CHIP Managed Care Program Integrity Toolkit (compliance tools): [CMS link](https://www.cms.gov/files/document/managed-care-compliance.pdf)

No private, confidential, or personal data used—pure public federal guidance available to anyone. Not affiliated with or endorsed by any government agency.

## Why Multi-Document RAG
Professionals working with federal healthcare policy (e.g., state compliance officers, analysts, or consultants) often need to quickly locate and understand specific rules in lengthy official documents—like coding edits, guidelines, or implementation details—to support accurate decision-making or rate adjustments.  
This prototype merges the three sources into one searchable index, retrieving relevant, cited excerpts across documents for broader insights.

**Intended Value**: Faster access to precise information from official sources, aiding general research, policy review, or professional workflows—while ensuring responses stay strictly tied to the original text for reliability.

## Accessibility
High contrast colors, large readable sans-serif fonts, and good line height for better usability (WCAG basics for visually impaired users).

## How to Use 🔍
Ask natural-language questions. Responses provide factual summaries + expandable source excerpts with file/page.

Try these examples (copy-paste):
- What is the National Correct Coding Initiative?
- How are capitation rates developed in managed care?
- Compare NCCI PTP edits and program integrity requirements.
- Summarize rate adjustments and medically unlikely edits (MUEs).
- Explain modifiers in NCCI and their relation to compliance tools.

Built with LangChain + Azure AI Search + Azure OpenAI + App Service—all free/low-cost tiers for sustainable demo.

Live Azure demo: rag-demo-app-bvgthfbga2evbbeh.centralus-01.azurewebsites.net

Feedback welcome!