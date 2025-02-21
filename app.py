import streamlit as st
import pandas as pd 

# Title & Description
st.title("BMI Calculator 🏋️‍♂️")
st.write("Calculate your Body Mass Index (BMI) to check if you're underweight, normal, overweight, or obese. "
         "Use the unit converter or slider to input your height and weight. Maintain a healthy balance! 💪")

# Define BMI categories
bmi_categories = pd.DataFrame({
    "Category": ["Underweight", "Normal weight", "Overweight", "Obesity"],
    "BMI Range": ["Less than 18.5", "18.5 - 24.9", "25 - 29.9", "30 or greater"]
})

# Add index starting from 1
bmi_categories.index = bmi_categories.index + 1

# Display BMI category table
st.table(bmi_categories)

# --- Input Section ---

# Create two columns for better layout
col1, col2 = st.columns(2)

# Height Input (Left Column)
with col1:
    st.subheader("Height 📏")
    height_unit = st.selectbox("Select height unit:", ["Meters", "Centimeters", "Inches", "Feet"])
    height_input = st.number_input("Enter your height:", min_value=00, format="%.2f")

    # Convert height based on selected unit
    if height_unit == "Centimeters":
        height = height_input / 100  # Convert cm to meters
    elif height_unit == "Inches":
        height = height_input * 0.0254  # Convert inches to meters
    elif height_unit == "Feet":
        height = height_input * 0.3048  # Convert feet to meters
    else:
        height = height_input  # Already in meters

    # Height Slider (linked to conversion result)
    height_slider = st.slider("Adjust height (in meters):", 0.5, 2.5, height, step=0.01)

# Weight Input (Right Column)
with col2:
    st.subheader("Weight ⚖️")
    weight_unit = st.selectbox("Select weight unit:", ["Kilograms", "Pounds"])
    weight_input = st.number_input("Enter your weight:", min_value=00, format="%.2f")

    # Convert weight based on selected unit
    if weight_unit == "Pounds":
        weight = weight_input * 0.453592  # Convert pounds to kg
    else:
        weight = weight_input  # Already in kg

    # Weight Slider (linked to conversion result)
    weight_slider = st.slider("Adjust weight (in kg):", 20.0, 200.0, weight, step=0.5)

# --- BMI Calculation ---
if height_slider > 0 and weight_slider > 0:  # Ensure valid input
    bmi = weight_slider / (height_slider ** 2)
    st.write(f"### Your BMI is: **{bmi:.2f}**")

    # Categorizing BMI with Emojis
    if bmi < 18.5:
        st.info("⚠️ **Underweight** – You may need to gain some healthy weight. 🍽️")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ **Normal Weight** – You are in a healthy range! Keep it up! 🏆")
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ **Overweight** – Consider a balanced diet and regular exercise. 🏃‍♂️")
    else:
        st.error("🚨 **Obesity** – Maintaining a healthier lifestyle is recommended. 🏋️‍♂️")
else:
    st.warning("Please enter valid height and weight values. ⚠️")

# #

# import streamlit as st
# import pandas as pd 

# st.title("BMI Calculator")

# # Define BMI categories as a DataFrame
# bmi_categories = pd.DataFrame({
#     "Category": ["Underweight", "Normal weight", "Overweight", "Obesity"],
#     "BMI Range": ["Less than 18.5", "18.5 - 24.9", "25 - 29.9", "30 or greater"]
# })

# # Add a new index starting from 1
# bmi_categories.index = bmi_categories.index + 1

# # Display as a table
# st.table(bmi_categories)

# height = st.slider("Enter your height (in inches):",12,100,65)
# weight = st.slider("Enter your weight (in kg):",30,200,50)

# bmi = weight / (( height * 0.0254 ) ** 2) 

# st.write(f"### Your BMI is {bmi:.2f}")

    
# if bmi < 18.5:
#     st.info("You are underweight.")
# elif 18.5 <= bmi < 24.9:  # Fixed the syntax here
#     st.success("You have a normal weight.")
# elif 25 <= bmi < 29.9:  # Fixed the syntax here
#     st.success("You are overweight.")
# else:
#     st.error("You are obese.")

# #
