import streamlit as st

# Header with your name and roll number
st.title("Mechanical Unit Converter & Density Checker")
st.write("**Name:** Abdul Wahab Khan")
st.write("**Roll Number:** 25-ME-32")

# Unit Converter Section
st.header("Unit Converter")

conversion_options = {
    "Length (m to ft)": lambda x: x * 3.28084,
    "Length (ft to m)": lambda x: x / 3.28084,
    "Mass (kg to lb)": lambda x: x * 2.20462,
    "Mass (lb to kg)": lambda x: x / 2.20462,
    "Pressure (Pa to psi)": lambda x: x * 0.000145038,
    "Pressure (psi to Pa)": lambda x: x / 0.000145038,
}

conversion_choice = st.selectbox("Select Conversion Type", list(conversion_options.keys()))
value = st.number_input("Enter Value", min_value=0.0, format="%.5f")

if st.button("Convert"):
    result = conversion_options[conversion_choice](value)
    st.success(f"Converted Value: {result:.5f}")

# Density Checker Section
st.header("Density Checker")

mass = st.number_input("Enter Mass (kg)", min_value=0.0, format="%.5f")
volume = st.number_input("Enter Volume (m³)", min_value=0.0, format="%.5f")

if st.button("Check Density"):
    if volume == 0:
        st.error("Volume cannot be zero.")
    else:
        density = mass / volume
        st.success(f"Density: {density:.5f} kg/m³")
