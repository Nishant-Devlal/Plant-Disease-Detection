import streamlit as st
from utils.prediction import model_prediction
from utils.classes import CLASS_NAMES

st.set_page_config(
    page_title="Disease Detection | PlantGuard AI",
    page_icon="🌿",
    layout="wide"
)

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.detection-header {
    text-align: center;
    padding: 1.5rem 0 2rem 0;
}

.detection-header h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

.detection-header span {
    color: #22c55e;
}

.detection-header p {
    color: #94a3b8;
    font-size: 1.1rem;
}

.upload-container {
    padding: 1.5rem;
    border-radius: 15px;
    border: 1px solid rgba(128, 128, 128, 0.25);
    background: rgba(128, 128, 128, 0.04);
}

.result-card {
    padding: 1.5rem;
    border-radius: 15px;
    border: 1px solid rgba(128, 128, 128, 0.25);
    background: rgba(128, 128, 128, 0.04);
    margin-top: 1rem;
}

.result-title {
    font-size: 1rem;
    color: #94a3b8;
    margin-bottom: 0.3rem;
}

.result-disease {
    font-size: 1.8rem;
    font-weight: 700;
}

.info-card {
    padding: 1.3rem;
    border-radius: 15px;
    border: 1px solid rgba(128, 128, 128, 0.25);
    background: rgba(128, 128, 128, 0.04);
    min-height: 250px;
}

.info-card-thin {
    padding: 1.3rem;
    border-radius: 15px;
    border: 1px solid rgba(128, 128, 128, 0.25);
    background: rgba(128, 128, 128, 0.04);
    min-height: 150px;
}

.info-card h3 {
    margin-bottom: 0.5rem;
}

.info-card p {
    color: #94a3b8;
    line-height: 1.6;
}

.section-title {
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.section-title h2 {
    font-size: 1.8rem;
}

.disclaimer {
    padding: 1rem 1.3rem;
    border-radius: 12px;
    border-left: 4px solid #f59e0b;
    background: rgba(245, 158, 11, 0.08);
    margin-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

def format_class_name(class_name):
    plant, disease = class_name.split("___")
    plant = plant.replace("_", " ")
    disease = disease.replace("_", " ")
    return plant, disease

def get_disease_info(disease):
    disease_info = {
        "Apple scab":
            "Remove infected leaves and fruit and avoid prolonged leaf wetness.",

        "Black rot":
            "Remove infected plant material and maintain good air circulation.",

        "Cedar apple rust":
            "Remove infected leaves and improve air circulation around the plant.",

        "Powdery mildew":
            "Improve air circulation and avoid excessive humidity around the leaves.",

        "Common rust":
            "Remove severely infected leaves and maintain good crop management.",

        "Northern Leaf Blight":
            "Remove heavily infected leaves and maintain proper field sanitation.",

        "Early blight":
            "Remove affected leaves and avoid overhead watering.",

        "Late blight":
            "Remove infected plant material and avoid prolonged leaf moisture.",

        "Bacterial spot":
            "Remove severely infected leaves and avoid working with wet foliage.",

        "Leaf Mold":
            "Improve ventilation and reduce humidity around the plant.",

        "Septoria leaf spot":
            "Remove affected leaves and avoid overhead irrigation.",

        "Spider mites Two-spotted spider mite":
            "Inspect the underside of leaves and maintain appropriate plant moisture.",

        "Target Spot":
            "Remove infected leaves and improve air circulation.",

        "Tomato Yellow Leaf Curl Virus":
            "Remove severely affected plants and control insect vectors such as whiteflies.",

        "Tomato mosaic virus":
            "Remove infected plants and disinfect tools after handling affected plants.",

        "Haunglongbing (Citrus greening)":
            "Remove affected plants where appropriate and manage insect vectors."
    }

    return disease_info.get(
        disease,
        "Monitor the plant closely and consider consulting an agricultural professional."
    )

st.markdown("""
<div class="detection-header">
    <h1>🔍 Plant <span>Disease Detection</span></h1>
    <p>
        Upload a clear image of a plant leaf and let
        our AI model analyze it.
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="section-title">
    <h2>📤 Upload Leaf Image</h2>
</div>
""", unsafe_allow_html=True)

st.write(
    "For best results, upload a clear image where the affected "
    "part of the leaf is visible."
)

test_image = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)

if test_image is not None:
    st.markdown("### 🖼️ Image Preview")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image(
            test_image,
            caption="Uploaded Leaf Image",
            use_container_width=True
        )

    if st.button(
        "🔍 Analyze Leaf",
        type="primary",
        use_container_width=True
    ):

        with st.spinner("Analyzing the leaf image..."):
            try:
                prediction_result = model_prediction(test_image)
                if isinstance(prediction_result, tuple):
                    result_index = prediction_result[0]
                    confidence = prediction_result[1]
                else:
                    result_index = prediction_result
                    confidence = None

                raw_class = CLASS_NAMES[result_index]
                plant_name, disease_name = format_class_name(
                    raw_class
                )

                st.markdown("""
                <div class="section-title">
                    <h2>🌱 Detection Result</h2>
                </div>
                """, unsafe_allow_html=True)

                result_col1, result_col2 = st.columns(2)

                with result_col1:
                    st.markdown(
                        f"""
                        <div class="result-card">
                            <div class="result-title">
                                Plant
                            </div>
                            <div class="result-disease">
                                🌿 {plant_name}
                            </div>
                            <br>
                            <div class="result-title">
                                Detection
                            </div>
                            <div class="result-disease">
                                {'✅' if disease_name.lower() == 'healthy'
                                else '⚠️'}
                                {disease_name}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with result_col2:
                    if confidence is not None:
                        confidence = float(confidence)
                        if confidence <= 1:
                            confidence *= 100
                        st.markdown(
                            """
                            <br>
                            """,
                            unsafe_allow_html=True
                        )

                        st.metric("🎯 Prediction Confidence", f"{confidence:.2f}%")

                        st.progress(min(confidence / 100, 1.0))

                        if confidence >= 80:
                            st.success( "High confidence prediction")

                        elif confidence >= 50:
                            st.warning("Moderate confidence prediction")

                        else:
                            st.error(
                                "Low confidence prediction. "
                                "Try uploading a clearer image."
                            )

                        st.markdown("</div>", unsafe_allow_html=True)

                    else:
                        st.info(
                            "Confidence score is not available. "
                            "Update prediction.py to return it."
                        )

                if disease_name.lower() == "healthy":
                    st.markdown("""
                                <div class="section-title">
                                <h2>💡 General Recommendation</h2>
                                </div>
                                """, unsafe_allow_html=True)

                    st.markdown("""
                    <div class="info-card-thin">
                        <h3>✅ Plant appears healthy</h3>
                        <p>
                            No disease category was detected for
                            this image. Continue monitoring the
                            plant regularly for changes.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                else:
                    recommendation = get_disease_info(disease_name)

                    st.markdown("""
                    <div class="section-title">
                        <h2>💡 General Recommendation</h2>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown(
                        f"""
                        <div class="info-card-thin">
                            <h3>🌱 Suggested Action</h3>
                            <p>
                                {recommendation}
                            </p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            except Exception as e:
                st.error(
                    "Unable to analyze this image. "
                    "Please make sure you uploaded a valid plant leaf image."
                )
                st.exception(e)

else:
    st.info("👆 Upload a JPG, JPEG, or PNG image to begin disease detection.")

st.markdown("""
<div class="section-title">
    <h2>Tips for Better Predictions</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>☀️ Good Lighting</h3>
        <p>
            Use a well-lit image where the leaf
            and its symptoms are clearly visible.
        </p>
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🍃 Clear Leaf</h3>
        <p>
            Try to capture the affected leaf without
            too much background or obstruction.
        </p>
    </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown("""
    <div class="info-card">
        <h3>📷 Good Quality</h3>
        <p>
            Avoid blurry or extremely low-resolution
            images for better predictions.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="disclaimer">
    <strong>⚠️ Important:</strong>
    This application is an educational AI project.
    Predictions should not be considered professional
    agricultural advice. For serious crop disease issues,
    consult a qualified agricultural professional.
</div>
""", unsafe_allow_html=True)