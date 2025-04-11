
import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️")
st.title("ℹ️ About This App")

st.write("""
This web app helps to:
- Add new COVID patient records
- View, edit, delete, and export patient details
- Visualize the data (gender ratio, recovery status, etc.)

Developed with ❤️ using Python and Streamlit.
""")
