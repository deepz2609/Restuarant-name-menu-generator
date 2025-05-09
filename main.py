import streamlit as st
from langchain_helper import generate_menu



st.title("Restaurant Menu Generator")

cusine = st.sidebar.selectbox("pick a restaurant type", ["Italian", "Chinese", "Indian", "Mexican", "French", "Japanese", "Thai", "Greek", "Spanish", "American"])



if cusine:
    response = generate_menu(cusine)

    st.header(response['restaurant_name'].strip()) # Strip any leading/trailing whitespace
    menu_items = response['menu_items'].strip().split(', ')
    st.subheader("Menu Items")
    for item in menu_items:
        st.write(f"- {item}")
        


