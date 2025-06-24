import streamlit as st
import numpy as np
import math
import graphviz

st.subheader("⚛️ Criticality Calculator")

st.markdown("""
This tool estimates the **effective neutron multiplication factor** ($k_{eff}$) in a nuclear reactor core using:

$$ k_{eff} = \\frac{\\nu \\cdot \\Sigma_f}{\\Sigma_f + \\Sigma_a} $$

Where:  
- $\\nu$ = average neutrons per fission  
- $\\Sigma_f$ = macroscopic fission cross-section  
- $\\Sigma_a$ = macroscopic absorption cross-section  
""")

# Inputs
nu = st.slider("Average neutrons per fission (ν)", 1.5, 3.5, 2.43, step=0.01)
sigma_f = st.number_input("Macroscopic fission cross-section (Σf, cm⁻¹)", value=0.12)
sigma_a = st.number_input("Macroscopic absorption cross-section (Σa, cm⁻¹)", value=0.20)

# Calculation
try:
    k_eff = (nu * sigma_f) / (sigma_f + sigma_a)
    k_eff_display = round(k_eff, 4)

    if k_eff < 1:
        status = "🔵 Subcritical"
        color = "blue"
    elif k_eff == 1:
        status = "🟢 Critical"
        color = "green"
    else:
        status = "🔴 Supercritical"
        color = "red"

    st.markdown(f"### k-effective: `{k_eff_display}` → **{status}**")

    # Neutron cycle graph
    g = graphviz.Digraph()
    g.attr(rankdir="LR", size="6")
    g.node("Fission", f"Fission Neutrons\nν = {nu}", shape="box", style="filled", fillcolor="#f9f9f9")
    g.node("Absorption", f"Absorption\nΣa = {sigma_a}", fillcolor="#fdd", style="filled")
    g.node("Fission2", f"Fission Events\nΣf = {sigma_f}", fillcolor="#dfd", style="filled")

    g.edge("Fission", "Absorption", label="Losses", color="gray")
    g.edge("Fission", "Fission2", label="Induced Fission", color="orange")
    g.edge("Fission2", "Fission", label=f"k = {k_eff_display}", color=color)

    st.graphviz_chart(g)

except ZeroDivisionError:
    st.error("Invalid input: division by zero.")
