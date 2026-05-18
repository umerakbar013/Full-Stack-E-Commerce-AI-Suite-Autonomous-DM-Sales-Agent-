# Agentic E-Commerce Market Intelligence System  &  customer DM interactions.

A dual-agent AI suite built for high-volume Shopify storefronts to automate competitive analysis and customer DM interactions.

## Features
* **B2B Market Intelligence:** Simulates scraping competitor data (Shopify JSON, Instagram) and uses an LLM to generate actionable weekly merchandising reports.
* **B2C Customer Agent:** A function-calling chat interface that handles customer queries, checks live inventory, reads shipping policies, and generates secure checkout links without human intervention.

## Tech Stack
* **Frontend:** Streamlit
* **AI Orchestration:** OpenAI API (gpt-4o-mini), Function Calling concepts, CrewAI architecture patterns.
* **Data Processing:** Pandas

## How to Run Locally
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Add your OpenAI API Key to `app.py`.
4. Run the app: `streamlit run app.py`
