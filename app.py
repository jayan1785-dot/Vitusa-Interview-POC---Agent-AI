import streamlit as st

st.title("🛒 AI Shopping Assistant")

# Product list
products = ["Laptop", "Smartphone", "Headphones"]
choice = st.selectbox("Choose a product:", products)
st.write(f"You selected: {choice}")

# FAQ chatbot
faq = {
    "price": "The laptop costs $999.",
    "returns": "Yes, we offer 30-day free returns.",
    "delivery": "Delivery takes 3–5 business days."
}

user_input = st.text_input("Ask a question:")
if user_input:
    for key, answer in faq.items():
        if key in user_input.lower():
            st.write("🤖 Bot:", answer)
            break
    else:
        st.write("🤖 Bot: Sorry, I don’t know that yet.")
