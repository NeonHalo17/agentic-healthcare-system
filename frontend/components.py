import streamlit as st

# Reusable components for the UI
def display_answer(answer: str):

    st.subheader("🩺 Assistant")

    st.write(answer)


def display_tool_results(results: dict):

    with st.expander("Retrieved Information"):

        st.json(results)