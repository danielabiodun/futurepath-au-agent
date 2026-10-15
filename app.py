import streamlit as st
from agent1 import run_agent   # or: from agent import run_agent  if you renamed the file

st.set_page_config(page_title="FuturePath AU", page_icon="🛡️")
st.title("FuturePath AU")
st.caption("Cybersecurity pathway navigator — suggestions only; you and a mentor decide.")

user_input = st.text_area(
    "Tell us your goal and background",
    placeholder="e.g. Finished Year 12, no coding experience, interested in cyber"
)

if st.button("Find pathways") and user_input.strip():
    with st.spinner("Searching verified pathways..."):
        answer = run_agent(user_input)
    st.markdown(answer)
    st.info("Check official source links and deadlines before applying.")