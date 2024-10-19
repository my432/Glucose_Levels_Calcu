import streamlit as st
import matplotlib.pyplot as plt

# Function to calculate estimated HbA1c based on average blood glucose level
def calculate_hba1c(avg_glucose):
    return (avg_glucose + 46.7) / 28.7

# Function to provide health advice based on glucose levels
def provide_health_advice(glucose):
    if glucose < 70:
        return "⚠️ Your blood glucose is too low (hypoglycemia). Consider eating something sugary."
    elif 70 <= glucose <= 99:
        return "✅ Your blood glucose is in the normal range. Keep it up!"
    elif 100 <= glucose <= 125:
        return "⚠️ You are in the prediabetic range. Consider consulting a doctor."
    else:
        return "⚠️ Your blood glucose is high (hyperglycemia). Seek medical advice."

# Streamlit app layout
def main():
    # Customizing the sidebar
    st.sidebar.title("Blood Glucose & HbA1c App")
    st.sidebar.write("Use this app to track your glucose levels and get insights on your health.")

    # Main title and description
    st.title("🩸 Blood Glucose & HbA1c Estimator")
    st.write("This app helps you track your **blood glucose levels**, provides **health advice**, and calculates your **estimated HbA1c**.")
    
    # Adding some visual elements
    st.image("https://images.unsplash.com/photo-1574169208507-843761748bbf", caption="Monitor your blood glucose", use_column_width=True)
    
    # User input for glucose levels
    glucose = st.slider("Select your blood glucose level (mg/dL):", min_value=0, max_value=400, value=100)

    # Calculate HbA1c based on the average glucose level
    avg_glucose = st.slider("Select your average blood glucose level (mg/dL):", min_value=0, max_value=400, value=100)

    # Buttons for interactivity
    if st.button("Get Health Advice"):
        advice = provide_health_advice(glucose)
        st.write(advice)

    if st.button("Calculate Estimated HbA1c"):
        estimated_hba1c = calculate_hba1c(avg_glucose)
        st.success(f"Your estimated HbA1c is: **{estimated_hba1c:.2f}%**")
        
        # Display an informative chart
        fig, ax = plt.subplots()
        ax.bar(['Glucose Level'], [glucose], color='lightblue')
        ax.set_ylim(0, 400)
        st.pyplot(fig)

    # Adding footer
    st.sidebar.write("Made with ❤️ using Streamlit")

if __name__ == "__main__":
    main()
