import streamlit as st

st.set_page_config(
    page_title="About | PlantGuard AI",
    page_icon="🌿",
    layout="wide"
)

def show_about():
    st.markdown("""
    <style>

    .about-header {
        text-align: center;
        padding: 2rem 0 1.5rem 0;
    }

    .about-header h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }

    .about-header span {
        color: #22c55e;
    }

    .about-header p {
        color: #94a3b8;
        font-size: 1.1rem;
    }

    .section-title {
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    .info-card {
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        background: rgba(128, 128, 128, 0.05);
        min-height: 250px;
    }

    .info-card h3 {
        margin-bottom: 0.7rem;
    }

    .info-card p {
        color: #94a3b8;
        line-height: 1.6;
    }

    .tech {
        padding: 0.8rem 1rem;
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        text-align: center;
        margin-bottom: 0.8rem;
    }

    .notice {
        margin-top: 2rem;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 4px solid #22c55e;
        background: rgba(34, 197, 94, 0.08);
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="about-header">
        <h1>🌿 About <span>PlantGuard AI</span></h1>
        <p>
            An AI powered plant disease detection system
            built using deep learning.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🌱 Project Overview")

    st.write("""
    PlantGuard AI is a plant disease detection application
    that uses a deep learning model to identify diseases
    from images of plant leaves.

    The user can upload an image of a plant leaf, and the
    trained model analyzes the image and predicts the most
    likely disease.

    The goal of this project is to demonstrate how computer
    vision and deep learning can be applied to agriculture
    to assist with early plant disease identification.
    """)

    st.markdown("## 📊 Dataset Used")

    st.write("""
    The model was trained using the New Plant Disease Dataset,
    which contains RGB images of healthy and diseased plant
    leaves.
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Images", "87K+")

    with col2:
        st.metric("Disease Classes", "38")

    with col3:
        st.metric("Training Images", "70,295")

    with col4:
        st.metric("Validation Images", "17,572")

    st.info("""
    The dataset contains multiple crop categories including
    Apple, Blueberry, Cherry, Corn, Grape, Peach, Pepper,
    Potato, Raspberry, Soybean, Squash and Tomato.
    """)

    st.markdown("## Machine Learning Model")

    st.write("""
    A deep learning image classification model is used to
    classify plant leaf images into one of 38 different
    categories.

    Before prediction, the uploaded image is resized to
    128 x 128 pixels so that it matches the input dimensions
    expected by the trained model.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>🖼️ Input</h3>
            <p>
                Plant leaf image resized to
                128 × 128 pixels.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>🧠 Processing</h3>
            <p>
                Deep learning model extracts visual
                features from the leaf image.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-card">
            <h3>🎯 Output</h3>
            <p>
                One of 38 plant disease or healthy
                leaf categories.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## 🛠️ Technology Stack")

    col1, col2, col3, col4 = st.columns(4)

    technologies = [
        ("🐍", "Python"),
        ("🧠", "TensorFlow"),
        ("📊", "NumPy"),
        ("🎨", "Streamlit")
    ]

    for column, (icon, name) in zip([col1, col2, col3, col4], technologies):
        with column:
            st.markdown(
                f"""
                <div class="tech">
                    <h3>{icon}</h3>
                    <strong>{name}</strong>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("## 🔄 Prediction Pipeline")

    st.code("""
User uploads leaf image
          ⇩
Image preprocessing
          ⇩
Resize to 128 x 128
          ⇩
Trained deep learning model
          ⇩
Prediction probabilities
          ⇩
Highest probability class
          ⇩
Disease / Healthy result
    """)

    st.markdown("## ✨ Features")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🔍 Disease Detection
        
        Upload a plant leaf image and receive
        a predicted disease category.
        """)

        st.markdown("""
        ### ⚡ Fast Prediction

        The trained model can analyze an image
        and return a prediction within seconds.
        """)

    with col2:
        st.markdown("""
        ### 📈 Confidence Score

        The application can display the model's
        prediction confidence.
        """)

        st.markdown("""
        ### 🌿 Multiple Plant Types

        The model supports multiple crop species
        and 38 different classification categories.
        """)

    st.markdown("## ⚠️ Limitations")

    st.warning("""
    This project is intended for educational and
    demonstration purposes.

    Model predictions can be affected by image quality,
    lighting, background, camera angle, and symptoms that
    may look similar across different diseases.

    The prediction should not be treated as professional
    agricultural or medical advice.
    """)

    st.markdown("## 🎯 Project Goal")

    st.markdown("""
    <div class="notice">

    <h3>🌱 Making AI Useful for Agriculture</h3>

    <p>
    This project demonstrates the use of computer vision
    and deep learning for agricultural applications.
    By automating the initial identification of plant
    diseases, AI can potentially help farmers and
    agricultural professionals detect problems earlier
    and make better informed decisions.
    </p>

    </div>
    """, unsafe_allow_html=True)

show_about()