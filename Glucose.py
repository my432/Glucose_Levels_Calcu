import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

# Load a medical-themed image from the internet
def load_medical_image():
    url = "https://image.shutterstock.com/image-photo/medical-background-with-flat-design-260nw-1213842439.jpg"
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Function to calculate estimated HbA1c based on average blood glucose level
def calculate_hba1c(avg_glucose):
    return (avg_glucose + 46.7) / 28.7

# Function to provide health advice based on glucose levels
def provide_health_advice(glucose):
    if glucose < 70:
        return "🛑 **Hypoglycemia Warning:** Your blood glucose is too low. Eat something sugary immediately."
    elif 70 <= glucose <= 99:
        return "✅ **Normal Range:** Your blood glucose is within a healthy range."
    elif 100 <= glucose <= 125:
        return "⚠️ **Prediabetic Range:** Your blood glucose indicates prediabetes. Consider consulting a healthcare professional."
    else:
        return "🛑 **Hyperglycemia Alert:** Your blood glucose is too high. Seek medical attention if it remains elevated."

# Custom CSS for a clean medical-themed design
def custom_css():
    st.markdown("""
        <style>
            .main {
                background-color: #f7f9fc;
            }
            .sidebar .sidebar-content {
                background-color: #f0f4f7;
            }
            .stButton>button {
                background-color: #007acc;
                color: white;
                border-radius: 10px;
                font-size: 16px;
                padding: 8px 16px;
            }
            .stButton>button:hover {
                background-color: #005f99;
                color: white;
            }
            h1, h2, h3 {
                color: #004b70;
            }
            .footer {
                position: fixed;
                bottom: 0;
                width: 100%;
                background-color: #004b70;
                color: white;
                text-align: center;
                padding: 10px;
            }
        </style>
        """, unsafe_allow_html=True)

# Streamlit app layout
def main():
    custom_css()  # Apply the custom CSS for the medical theme
    
    # Sidebar with medical-themed design
    st.sidebar.title("🔬 Medical Health App")
    st.sidebar.write("Use this app to track your blood glucose and get medical advice.")

    # Title and description
    st.title("🩸 Blood Glucose & HbA1c Estimator")
    st.subheader("Monitor your blood glucose levels and estimate your HbA1c for a healthier life.")

    # Display medical-themed image (from an online source)
    image = load_medical_image()
    st.image(image, use_column_width=True, caption="Track your blood glucose for better health.")

    # User input for glucose levels with sliders
    glucose = st.slider("Select your current blood glucose level (mg/dL):", min_value=50, max_value=400, value=100, step=1)
    avg_glucose = st.slider("Select your average blood glucose level over the last 90 days (mg/dL):", min_value=50, max_value=400, value=120, step=1)

    # Get Health Advice button
    if st.button("Get Health Advice"):
        advice = provide_health_advice(glucose)
        st.info(advice)

    # Calculate Estimated HbA1c button
    if st.button("Calculate Estimated HbA1c"):
        estimated_hba1c = calculate_hba1c(avg_glucose)
        st.success(f"Your estimated HbA1c is: **{estimated_hba1c:.2f}%**")
        
        # Display informative chart for the user's glucose level
        fig, ax = plt.subplots()
        ax.bar(['Your Glucose Level'], [glucose], color='#4db8ff')
        ax.set_ylim(0, 400)
        ax.set_ylabel('mg/dL')
        ax.set_title("Your Current Glucose Level")
        st.pyplot(fig)

    # Footer
    st.markdown("<div class='footer'>Made with ❤️ by [Your Name] | Powered by Streamlit</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
