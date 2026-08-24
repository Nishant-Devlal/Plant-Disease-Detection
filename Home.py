import streamlit as st

st.set_page_config(
    page_title="Home | PlantGuard AI",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 PlantGuard AI")

st.subheader("AI Powered Plant Disease Detection")

st.write(
    """
    Welcome to PlantGuard AI a deep learning based
    plant disease detection system.

    Upload an image of a plant leaf and our trained
    model will analyze it and predict the most likely
    disease category.
    """
)

st.image(
    "assets/home_page.jpg",
    width=700
)

st.markdown("### 🚀 Get Started")

st.write(
    "Use the pages in the sidebar to learn about the project "
    "or detect a plant disease."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌿 Plant Categories", "15+")

with col2:
    st.metric("🦠 Disease Classes", "38")

with col3:
    st.metric("🖼️ Training Images", "70K+")