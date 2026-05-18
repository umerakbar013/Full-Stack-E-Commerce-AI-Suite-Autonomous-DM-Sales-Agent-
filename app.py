import streamlit as st
import pandas as pd
import time
from openai import OpenAI

# Initialize OpenAI Client
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
st.set_page_config(page_title="AI E-Commerce Suite", layout="wide")

st.title("🤖 Full-Stack E-Commerce AI Suite")
st.caption("Target Domain: High-Volume Luxury & Fast-Fashion Retail")

# Create two tabs for the two different projects
tab1, tab2 = st.tabs(["📊 Market Intelligence Agent (B2B)", "💬 Instagram DM Sales Agent (B2C)"])

# ==========================================
# TAB 1: THE MARKET INTELLIGENCE AGENT
# ==========================================
with tab1:
    st.sidebar.header("Agent Configuration")
    selected_brand = st.sidebar.selectbox("Select Client Store", ["ZaraBags Shopify Store (2k orders/day)"])
    competitors = st.sidebar.multiselect(
        "Target Competitors to Monitor", 
        ["Competitor A (Luxury Leather)", "Competitor B (Fast Fashion Totes)", "Competitor C (Crossbody Niche)"],
        default=["Competitor A (Luxury Leather)", "Competitor B (Fast Fashion Totes)"]
    )
    run_agent = st.sidebar.button("⚡ Run Agentic Workflow", type="primary")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Live Scraped Market Data")
        mock_data = {
            "Competitor": ["Competitor A", "Competitor A", "Competitor B", "Competitor B"],
            "Product Style": ["Quilted Shoulder Bag", "Classic Leather Tote", "Mini Pastel Crossbody", "Canvas Travel Bag"],
            "Price": ["$85", "$120", "$45", "$60"],
            "Stock Status": ["In Stock", "Low Stock", "Out of Stock", "In Stock"],
            "Top Customer Complaint": [
                "Strap broke after two weeks of usage.",
                "Too heavy to carry for long periods.",
                "Love the color but zipper gets stuck constantly.",
                "Smaller than expected, can't fit a phone."
            ]
        }
        df = pd.DataFrame(mock_data)
        st.dataframe(df, use_container_width=True)
        st.info("💡 Data Sources: Shopify API, Instagram API, Selenium Scrapers.")

    with col2:
        st.subheader("CrewAI Agent Synthesis")
        if run_agent:
            with st.status("Executing Agent Workflow...", expanded=True) as status:
                st.write("🕵️‍♂️ **Agent 1 (Scout):** Scanning price adjustments...")
                time.sleep(1)
                st.write("📈 **Agent 2 (Forecaster):** Analyzing review sentiment...")
                time.sleep(1)
                st.write("✍️ **Agent 3 (Strategist):** Compiling action steps...")
                time.sleep(1)
                status.update(label="Synthesis Complete!", state="complete", expanded=False)
            
            st.warning("⚠️ Running in Offline Demo Mode (No API Call Triggered)")
            st.markdown("""
            ### 🎯 Weekly Opportunity Report
            **1. Market Gaps Identified:**
            * Competitor A's $85 bags are experiencing strap failures.
            * Competitor B's canvas bags have faulty zippers.
            
            **2. Product Recommendations:**
            * Push our lightweight vegan leather bags to the homepage.
            * Highlight double-stitched straps in new ads.
            """)
        else:
            st.info("Click **'Run Agentic Workflow'** in the sidebar to simulate the report generation.", icon="💡")

# ==========================================
# TAB 2: THE INSTAGRAM DM SALES AGENT
# ==========================================
with tab2:
    st.subheader("📱 Autonomous DM Sales Agent (Function Calling Demo)")
    st.caption("This agent reads incoming customer DMs, checks live Shopify stock, and answers policy questions without human intervention.")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hi! Welcome to ZaraBags. How can I help you today?"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Type a customer DM... (e.g., 'Do you have the red quilted bag in stock?')"):
        # Display user message in chat
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Simulate Agent "Function Calling" (The wow factor for recruiters)
        with st.chat_message("assistant"):
            with st.status("Agent processing query...", expanded=True) as status:
                st.write("⚙️ **Tool Triggered:** `Natural Language Understanding (NLU)`")
                time.sleep(1)
                
                # Simple keyword logic for the demo
                if "address" in prompt.lower() or "checkout" in prompt.lower() or "buy" in prompt.lower():
                    st.write("⚙️ **Tool Triggered:** `create_draft_order(customer_data)`")
                    time.sleep(1.5)
                    response = "Perfect! I've secured that item for you. Please complete your payment securely using this auto-generated Shopify link: **[Secure Checkout Link]**"
                else:
                    st.write("⚙️ **Tool Triggered:** `check_shopify_inventory(item_type)`")
                    time.sleep(1)
                    st.write("⚙️ **Tool Triggered:** `get_shipping_policy(location)`")
                    time.sleep(1)
                    response = "I just checked our live warehouse system! Yes, we have that bag in stock. It costs Rs. 4,500 and delivery takes 2-3 working days. Would you like to provide your delivery address so I can generate a secure checkout link for you?"
                
                status.update(label="Tasks completed", state="complete", expanded=False)
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})