import streamlit as st
import graphviz

st.subheader("🧬 Decay Chain Viewer")

st.markdown("""
This interactive chart displays the full radioactive decay path for select isotopes:

**U-238**, **U-235**, **Th-232**, **Pu-239**, and **Np-237**.

You can trace how each isotope undergoes alpha (α) and beta (β⁻) decays until it stabilizes.

- 🔴 Alpha decay → red  
- 🔵 Beta decay → blue  
Hover over isotopes to see **half-life**, **Z**, and **mass number**.
""")

# Select isotope
isotope = st.selectbox("Select Isotope", ["Uranium-238", "Uranium-235", "Thorium-232", "Plutonium-239", "Neptunium-237"])

# All decay chains
chains = {
    "Uranium-238": [
        {"id": "U-238", "to": "Th-234", "mode": "α", "half_life": "4.47 billion y", "z": 92, "a": 238},
        {"id": "Th-234", "to": "Pa-234", "mode": "β", "half_life": "24.1 d", "z": 90, "a": 234},
        {"id": "Pa-234", "to": "U-234", "mode": "β", "half_life": "1.17 m", "z": 91, "a": 234},
        {"id": "U-234", "to": "Th-230", "mode": "α", "half_life": "245,500 y", "z": 92, "a": 234},
        {"id": "Th-230", "to": "Ra-226", "mode": "α", "half_life": "75,400 y", "z": 90, "a": 230},
        {"id": "Ra-226", "to": "Rn-222", "mode": "α", "half_life": "1,600 y", "z": 88, "a": 226},
        {"id": "Rn-222", "to": "Po-218", "mode": "α", "half_life": "3.82 d", "z": 86, "a": 222},
        {"id": "Po-218", "to": "Pb-214", "mode": "α", "half_life": "3.1 m", "z": 84, "a": 218},
        {"id": "Pb-214", "to": "Bi-214", "mode": "β", "half_life": "26.8 m", "z": 82, "a": 214},
        {"id": "Bi-214", "to": "Po-214", "mode": "β", "half_life": "19.9 m", "z": 83, "a": 214},
        {"id": "Po-214", "to": "Pb-210", "mode": "α", "half_life": "164 µs", "z": 84, "a": 214},
        {"id": "Pb-210", "to": "Bi-210", "mode": "β", "half_life": "22.3 y", "z": 82, "a": 210},
        {"id": "Bi-210", "to": "Po-210", "mode": "β", "half_life": "5.01 d", "z": 83, "a": 210},
        {"id": "Po-210", "to": "Pb-206", "mode": "α", "half_life": "138.4 d", "z": 84, "a": 210}
    ],

    "Uranium-235": [
        {"id": "U-235", "to": "Th-231", "mode": "α", "half_life": "704 million y", "z": 92, "a": 235},
        {"id": "Th-231", "to": "Pa-231", "mode": "β", "half_life": "25.5 h", "z": 90, "a": 231},
        {"id": "Pa-231", "to": "Ac-227", "mode": "α", "half_life": "32,760 y", "z": 91, "a": 231},
        {"id": "Ac-227", "to": "Th-227", "mode": "β", "half_life": "21.8 y", "z": 89, "a": 227},
        {"id": "Th-227", "to": "Ra-223", "mode": "α", "half_life": "18.7 d", "z": 90, "a": 227},
        {"id": "Ra-223", "to": "Rn-219", "mode": "α", "half_life": "11.4 d", "z": 88, "a": 223},
        {"id": "Rn-219", "to": "Po-215", "mode": "α", "half_life": "3.96 s", "z": 86, "a": 219},
        {"id": "Po-215", "to": "Pb-211", "mode": "α", "half_life": "1.78 ms", "z": 84, "a": 215},
        {"id": "Pb-211", "to": "Bi-211", "mode": "β", "half_life": "36.1 m", "z": 82, "a": 211},
        {"id": "Bi-211", "to": "Tl-207", "mode": "α", "half_life": "2.14 m", "z": 83, "a": 211},
        {"id": "Tl-207", "to": "Pb-207", "mode": "β", "half_life": "4.77 m", "z": 81, "a": 207}
    ],

    "Thorium-232": [
        {"id": "Th-232", "to": "Ra-228", "mode": "α", "half_life": "14.05 billion y", "z": 90, "a": 232},
        {"id": "Ra-228", "to": "Ac-228", "mode": "β", "half_life": "5.75 y", "z": 88, "a": 228},
        {"id": "Ac-228", "to": "Th-228", "mode": "β", "half_life": "6.15 h", "z": 89, "a": 228},
        {"id": "Th-228", "to": "Ra-224", "mode": "α", "half_life": "1.91 y", "z": 90, "a": 228},
        {"id": "Ra-224", "to": "Rn-220", "mode": "α", "half_life": "3.66 d", "z": 88, "a": 224},
        {"id": "Rn-220", "to": "Po-216", "mode": "α", "half_life": "55.6 s", "z": 86, "a": 220},
        {"id": "Po-216", "to": "Pb-212", "mode": "α", "half_life": "0.145 s", "z": 84, "a": 216},
        {"id": "Pb-212", "to": "Bi-212", "mode": "β", "half_life": "10.6 h", "z": 82, "a": 212},
        {"id": "Bi-212", "to": "Tl-208", "mode": "β", "half_life": "60.6 m", "z": 83, "a": 212},
        {"id": "Tl-208", "to": "Pb-208", "mode": "β", "half_life": "3.05 m", "z": 81, "a": 208}
    ],

    "Plutonium-239": [
        {"id": "Pu-239", "to": "U-235", "mode": "α", "half_life": "24,100 y", "z": 94, "a": 239},
        {"id": "U-235", "to": "Th-231", "mode": "α", "half_life": "704 million y", "z": 92, "a": 235}
        # Connects to U-235 chain
    ],

    "Neptunium-237": [
        {"id": "Np-237", "to": "Pa-233", "mode": "α", "half_life": "2.14 million y", "z": 93, "a": 237},
        {"id": "Pa-233", "to": "U-233", "mode": "β", "half_life": "27 d", "z": 91, "a": 233}
    ]
}

# Build Graph
g = graphviz.Digraph(format='png')
g.attr(rankdir='TB', size='1,25')

for step in chains[isotope]:
    tooltip = f"Z={step['z']}, A={step['a']}, Half-life: {step['half_life']}"
    g.node(step["id"], shape="circle", style="filled", fillcolor="#fefefe", tooltip=tooltip)
    color = "red" if step["mode"] == "α" else "blue"
    g.edge(step["id"], step["to"], label=step["mode"], color=color, fontcolor=color)

# Display
st.graphviz_chart(g, use_container_width=True)
