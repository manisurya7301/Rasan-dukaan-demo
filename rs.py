import streamlit as st

# Example Streamlit app code
st.title("Add Product")
st.write("Welcome to the Add Product Page!")

# Use Streamlit widgets for input
product_name = st.text_input("Product Name")
price = st.number_input("Price", min_value=0.0)

if st.button("Add Product"):
    st.success(f"Product '{product_name}' added successfully!")
