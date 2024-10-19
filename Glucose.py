import streamlit as st

# Function to calculate estimated HbA1c based on average blood glucose level
def calculate_hba1c(avg_glucose):
    # Formula for estimating HbA1c: (average glucose + 46.7) / 28.7
    return (avg_glucose + 46.7) / 28.7

# Function to provide health advice based on glucose levels
def provide_health_advice(glucose):
    if glucose < 70:
        return "Your blood glucose is too low (hypoglycemia). Consider eating something sugary."
    elif 70 <= glucose <= 99:
        return "Your blood glucose is normal."
    elif 100 <= glucose <= 125:
        return "You are in the prediabetic range. Consider consulting a doctor."
    else:
        return "Your blood glucose is high (hyperglycemia). You should seek medical advice."

# Streamlit app layout
def main():
    st.title("Blood Glucose & HbA1c Calculator")
    st.write("This app helps you track your blood glucose levels, provides health advice, and calculates your estimated HbA1c.")

    # User input for glucose levels
    glucose = st.number_input("Enter your blood glucose level (mg/dL):", min_value=0)

    # Calculate HbA1c based on the average glucose level (optional: you can ask for average glucose over days or use one input)
    avg_glucose = st.number_input("Enter your average blood glucose level (mg/dL):", min_value=0)

    if st.button("Get Health Advice"):
        advice = provide_health_advice(glucose)
        st.write(advice)

    if st.button("Calculate Estimated HbA1c"):
        estimated_hba1c = calculate_hba1c(avg_glucose)
        st.write(f"Your estimated HbA1c is: {estimated_hba1c:.2f}%")

if __name__ == "__main__":
    main()
