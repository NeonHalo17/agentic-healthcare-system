import streamlit as st

from api_client import query_agent
from components import (
    display_answer,
    display_tool_results
)
import requests
from config import BACKEND_URL
# Main Frontend app 
# Page
st.set_page_config(
    page_title="Healthcare Agent",
    page_icon="🩺",
    layout="wide"
)

# Title
st.title("🩺 Agentic Healthcare Assistant")

# Sidebar
with st.sidebar:

    st.header("Session")

    session_id = st.text_input(
        "Session ID",
        value="session1"
    )

    patient_id = st.text_input(
        "Patient name",
        value=""
    )

# Query input area
query = st.text_area(
    "Ask a healthcare question"
)

# Submit button
if st.button("Submit"):

    if query.strip():

        with st.spinner("Thinking..."):

            response = query_agent(
                session_id=session_id,
                query=query
            )

        display_answer(
            response["answer"]
        )

        display_tool_results(
            response["tool_results"]
        )

tab_chat, tab_eval = st.tabs(
    [
        "Healthcare Assistant",
        "Evaluation"
    ]
)

if st.button("Run Evaluation"):
    response = requests.post(f"{BACKEND_URL}/evaluation/run").json()
    metrics = response["metrics"]
    timings = response["timings"]
    
    st.metric(
        "Accuracy",
        f"{metrics['accuracy']:.1%}"
    )

    st.metric(
        "Average Latency",
        f"{metrics['average_latency']:.0f} ms"
    )

    st.metric(
        "Booking Success",
        f"{metrics['booking_success_rate']:.1%}"
    )

    st.subheader("Module Performance")

    st.bar_chart(timings)