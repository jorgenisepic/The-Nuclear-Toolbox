import streamlit as st
from pyvis.network import Network
import streamlit.components.v1 as components
import os

st.subheader("🧬 Decay Chain Viewer")

st.markdown("""
Visualize how radioactive isotopes decay step-by-step into stable elements.

- 🔴 Alpha (α) decay → red edges  
- 🔵 Beta (β⁻) decay → blue edges  
- Hover over nodes to view **Z**, **A**, and half-life.
""")

# Select isotope
isotope = st.selectbox("Select Isotope", [
    "Uranium-238", "Uranium-235", "Thorium-232",
    "Plutonium-239", "Neptunium-237"
])

chains = {
    "Uranium-238": [
        {"id": "U-238", "to": "Th-234", "mode": "α", "half_life": "4.47B y", "z": 92, "a": 238},
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
   
}

# Load selected decay chain
chain = chains[isotope]

# Build network
net = Network(height="900px", width="100%", directed=True)
net.barnes_hut()

# Options
net.set_options("""
const options = {
  "nodes": {
    "font": {"size": 20},
    "shape": "circle"
  },
  "layout": {
    "hierarchical": {
      "enabled": true,
      "direction": "UD",
      "sortMethod": "directed"
    }
  },
  "interaction": {
    "hover": true,
    "navigationButtons": true
  }
}
""")

# Add nodes and edges
for step in chain:
    tooltip = f"Z={step['z']}<br>A={step['a']}<br>Half-life: {step['half_life']}"
    net.add_node(step["id"], label=step["id"], title=tooltip)
    color = "red" if step["mode"] == "α" else "blue"
    net.add_edge(step["id"], step["to"], label=step["mode"], color=color)

# Save and show
net.save_graph("decay_chain_graph.html")
with open("decay_chain_graph.html", "r", encoding="utf-8") as f:
    html = f.read()
components.html(html, height=950, scrolling=True)
