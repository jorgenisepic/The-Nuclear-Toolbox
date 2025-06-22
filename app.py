# app.py
# Nuclear Engineering Toolkit
# Created by Jorgen Eduard Olesen
# MIT License

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
import graphviz
from shielding.shielding_simulator import calculate_shielded_dose, shielding_factors
from isotopes_database.isotope_compare import compare_isotopes
from isotopes_database.isotope_search import isotope_searcher

# ----- Page Setup -----
st.set_page_config(page_title="The Nuclear Toolbox", layout="centered")
st.title("The Nuclear Toolbox")
st.caption("Created by Jorgen Eduard Olesen · MIT License")
st.markdown("![Status](https://img.shields.io/badge/Status-In_Development-yellow)")

# ----- Menu -----
menu = st.sidebar.radio("🔍 Select Module", [
    "🏠 Home",
    "📉 Radioactive Decay",
    "📟 Exposure Calculator",
    "📊 Radiation Dose Chart",
    "🔁 Radiation Unit Converter",
    "📋 Radiation Types",
    "🛡️ Shielding Simulation",    
    "🔍 Isotope Search",
    "⚖️ Compare Isotopes",
    "🔗 Decay Chain Viewer"

])

# ----- Home -----
if menu == "🏠 Home":
    st.header("📘 Welcome")
    st.markdown("""
This is a beginner-level toolkit designed for exploring core topics in nuclear engineering and radiation science:

### 🔬 Key Features:
- **Radioactive decay** — visualize and calculate half-lives and remaining isotopes.
- **Radiation exposure and cancer risk** — estimate dose impact and biological effect.
- **Dose classification** — understand dose categories from safe to hazardous.
- **Unit conversion** — convert between Sieverts, rem, Gray, and more.
- **Radiation type reference** — learn properties of alpha, beta, gamma, and neutron radiation.
- **Isotope Search & Comparison** — search nuclear isotopes and compare their properties.
- **Shielding Simulation** — model radiation shielding through various materials.

---

### 📌 About
This application is developed as part of **The Nuclear Toolbox**, a student-led initiative aimed at making nuclear science more accessible.

Built entirely with **Python** and **Streamlit**, this app is optimized for both learners and educators. Future versions aim to support researchers with deeper analysis tools and database integration.

📦 **Version:** 1.1.3  
Feel free to explore, experiment, and contribute to the project!
""")

# ----- Radioactive Decay -----
elif menu == "📉 Radioactive Decay":
    st.header("📉 Radioactive Decay Calculator")

    N0_input = st.text_input("Initial Quantity (N₀)", "1000")
    decay_const_input = st.text_input("Decay Constant (λ)", "0.01")
    time_input = st.text_input("Elapsed Time (t)", "10")

    def decay_remaining(N0, decay_constant, time):
        return N0 * math.exp(-decay_constant * time)

    def decay_half_life(decay_constant):
        return math.log(2) / decay_constant

    if st.button("Calculate"):
        try:
            N0 = float(N0_input)
            decay_const = float(decay_const_input)
            t = float(time_input)

            N = decay_remaining(N0, decay_const, t)
            half_life = decay_half_life(decay_const)

            st.success(f"📉 Remaining Quantity: {N:,.2f}")
            st.info(f"⏳ Half-life: {half_life:,.2f} time units")

            # Generate decay graph
            times = np.linspace(0, t, 100)
            quantities = N0 * np.exp(-decay_const * times)

            fig, ax = plt.subplots()
            ax.plot(times, quantities, color="darkgreen", linewidth=2)
            ax.set_xlabel("Time")
            ax.set_ylabel("Remaining Quantity")
            ax.set_title("Radioactive Decay Over Time")
            ax.grid(True)

            st.pyplot(fig)

        except ValueError:
            st.error("Please enter valid numbers.")


   # ----- Exposure Calculator -----
elif menu == "📟 Exposure Calculator":
    st.header("📟 Radiation Exposure Calculator")

    hours = st.slider("Hours exposed per day", min_value=0.0, max_value=24.0, step=0.5, value=2.0)
    uSv_hour = st.slider("Radiation rate (µSv/hour)", min_value=0.0, max_value=10.0, step=0.1, value=0.5)

    def annual_dose(hpd, rate):
        return hpd * 365 * rate / 1000  # in mSv

    def cancer_risk(dose_mSv):
        return dose_mSv * 0.005

    def categorize_dose(dose_mSv):
        if dose_mSv <= 0.1:
            return "🟢 Very Low", "No health risk."
        elif dose_mSv <= 10:
            return "🟡 Low", "Low probability of long-term effects."
        elif dose_mSv <= 100:
            return "🟠 Moderate", "Mild increase in cancer risk."
        elif dose_mSv <= 1000:
            return "🔴 High", "Significant biological damage possible."
        else:
            return "☠️ Extreme", "Potentially lethal dose."

    if st.button("Estimate Risk"):
        dose = annual_dose(hours, uSv_hour)
        risk = cancer_risk(dose)
        label, desc = categorize_dose(dose)

        st.success(f"Annual Dose: {dose:,.3f} mSv")
        st.markdown(f"**Cancer Risk:** {risk:.2%}")
        st.markdown(f"**Risk Level:** {label}")
        st.caption(desc)

        # Create dose chart
        exposure_range = np.linspace(0, 24, 50)
        dose_values = [annual_dose(h, uSv_hour) for h in exposure_range]

        fig, ax = plt.subplots()
        ax.plot(exposure_range, dose_values, color="red", linewidth=2)
        ax.set_xlabel("Hours per Day")
        ax.set_ylabel("Annual Dose (mSv)")
        ax.set_title("Annual Radiation Dose vs. Exposure Time")
        ax.grid(True)

        st.pyplot(fig)

# ----- Radiation Dose Comparison Chart -----
elif menu == "📊 Radiation Dose Chart":
    st.header("📊 Radiation Dose Comparison Chart")
    st.markdown("""
This chart helps visualize the scale of different radiation doses — from everyday background exposure to serious nuclear incidents.  
All doses are in **millisieverts (mSv)** and are based on public safety, medical use, and known accident data.
""")
    dose_data = {
        "Dental X-ray": 0.005,
        "NY-Tokyo Flight": 0.2,
        "Chest X-ray": 0.1,
        "CT Scan": 7,
        "Annual Background": 2.4,
        "Nuclear Worker Limit": 50,
        "Chernobyl Worker": 1000,
        "Lethal Dose (LD50)": 4000
    }

    def get_color(dose):
        if dose <= 0.1:
            return "green"
        elif dose <= 10:
            return "gold"
        elif dose <= 100:
            return "orange"
        elif dose <= 1000:
            return "red"
        else:
            return "darkred"

    labels = list(dose_data.keys())
    values = list(dose_data.values())
    colors = [get_color(d) for d in values]

    fig, ax = plt.subplots()
    ax.barh(labels, values, color=colors)
    ax.set_xscale("log")
    ax.set_xlabel("Dose in mSv (log scale)")
    ax.set_title("Radiation Exposure Levels by Event")
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)

    st.pyplot(fig)

    st.caption("""
This chart compares various radiation exposure levels using a logarithmic scale.

- **0.005 mSv** – Dental X-ray  
- **0.2 mSv** – Flight from New York to Tokyo  
- **2.4 mSv** – Average annual background radiation  
- **7 mSv** – CT scan  
- **50 mSv** – Annual occupational limit (nuclear worker)  
- **1000 mSv** – Chernobyl emergency worker  
- **4000 mSv** – Approximate Lethal Dose (LD50)

📌 *Colors indicate severity: Green = Low, Red = High*
""")

# ----- Unit Converter -----
elif menu == "🔁 Radiation Unit Converter":
    st.header("🔁 Radiation Unit Converter")

    units = ["mSv", "Sv", "rem", "Gy"]
    from_unit = st.selectbox("From", units, index=0)
    to_unit = st.selectbox("To", units, index=1)
    value = st.number_input("Value to Convert", value=1.0)

    def convert_units(val, f_unit, t_unit):
        base_sv = {
            "Sv": 1,
            "mSv": 0.001,
            "rem": 0.01,
            "Gy": 1  # assuming biological equivalence
        }
        return val * base_sv[f_unit] / base_sv[t_unit]

    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:,.4f} {to_unit}")

# ----- Radiation Types -----
elif menu == "📋 Radiation Types":
    st.header("📋 Types of Ionizing Radiation")
    data = {
        "Alpha": {
            "Charge": "+2",
            "Mass": "Heavy",
            "Penetration": "Low",
            "Shielding": "Paper / Skin",
            "Danger": "High if inhaled"
        },
        "Beta": {
            "Charge": "-1",
            "Mass": "Light",
            "Penetration": "Medium",
            "Shielding": "Aluminum",
            "Danger": "Can burn skin"
        },
        "Gamma": {
            "Charge": "0",
            "Mass": "Wave (no mass)",
            "Penetration": "High",
            "Shielding": "Lead / Concrete",
            "Danger": "Deep tissue damage"
        },
        "Neutron": {
            "Charge": "0",
            "Mass": "Neutral Particle",
            "Penetration": "Very High",
            "Shielding": "Water / Borated Concrete",
            "Danger": "Can activate other materials"
        }
    }

    for name, props in data.items():
        st.subheader(name)
        for key, val in props.items():
            st.markdown(f"**{key}:** {val}")
        st.markdown("---")



        #----SHIELDING----
elif menu == "🛡️ Shielding Simulation":
    st.title("🛡️ Shielding Simulator")
    st.markdown("Estimate how much radiation passes through different shielding materials.")

    dose_input = st.number_input("Initial Radiation Dose (μSv)", min_value=0.0, step=0.1)
    material_choice = st.selectbox("Shielding Material", list(shielding_factors.keys()))

    if st.button("Calculate"):
        remaining, blocked = calculate_shielded_dose(dose_input, material_choice)

        st.success(f"🛑 Blocked: {blocked * 100:.1f}%")
        st.info(f"☢️ Remaining Dose: {remaining:,.2f} μSv")

        st.bar_chart({
            "Dose (μSv)": {
                "Initial": dose_input,
                "Remaining": remaining
            }
        })

        # 📊 Graphviz visual
        st.markdown("### 📉 Shielding Path")
        g = graphviz.Digraph()

        g.node("A", f"{dose_input:.2f} μSv", shape="circle", color="orange", style="filled")
        g.node("B", material_choice, shape="box", color="lightblue", style="filled")
        g.node("C", f"{remaining:,.2f} μSv", shape="circle", color="green", style="filled")

        g.edge("A", "B", label="Shielding")
        g.edge("B", "C", label="Transmitted")

        st.graphviz_chart(g) 

        #--- ISOTOPE SECTION

elif menu == "🔍 Isotope Search":
    isotope_searcher()


        #----- isotope compare

elif menu == "⚖️ Compare Isotopes":
    compare_isotopes()


    #--- Decay chain viewer

elif menu == "🔗 Decay Chain Viewer":
    st.header("🔗 Decay Chain Viewer")
    st.markdown("""
This interactive chart displays the full radioactive decay path for select isotopes like **U-238**, **U-235**, and **Th-232**.

You can trace how each isotope undergoes alpha (α) and beta (β⁻) decays until it stabilizes.

🔴 Red = Alpha decay  
🔵 Blue = Beta decay  
""")

    isotope_selected = st.selectbox("Select Isotope", ["Uranium-238", "Thorium-232", "Uranium-235"])
    display_decay_chain(isotope_selected)