import streamlit as st
import graphviz

# Sample decay chains
decay_chains = {
    "Uranium-238": [
        ("U-238", "Th-234"),
        ("Th-234", "Pa-234"),
        ("Pa-234", "U-234"),
        ("U-234", "Th-230"),
        ("Th-230", "Ra-226"),
        ("Ra-226", "Rn-222"),
        ("Rn-222", "Po-218"),
        ("Po-218", "Pb-214"),
        ("Pb-214", "Bi-214"),
        ("Bi-214", "Po-214"),
        ("Po-214", "Pb-210"),
        ("Pb-210", "Bi-210"),
        ("Bi-210", "Po-210"),
        ("Po-210", "Pb-206 (Stable)")
    ],
    "Thorium-232": [
        ("Th-232", "Ra-228"),
        ("Ra-228", "Ac-228"),
        ("Ac-228", "Th-228"),
        ("Th-228", "Ra-224"),
        ("Ra-224", "Rn-220"),
        ("Rn-220", "Po-216"),
        ("Po-216", "Pb-212"),
        ("Pb-212", "Bi-212"),
        ("Bi-212", "Tl-208"),
        ("Tl-208", "Pb-208 (Stable)")
    ]
}

def show_decay_chain():
    st.header("🧬 Decay Chain Viewer")
    choice = st.selectbox("Select an Isotope:", list(decay_chains.keys()))

    st.markdown("### 📉 Visualized Decay Chain")

    # Build Graph
    graph = graphviz.Digraph()
    for parent, daughter in decay_chains[choice]:
        graph.edge(parent, daughter)

    st.graphviz_chart(graph)

    # Display list view
    with st.expander("🔬 View Steps in Text"):
        for i, (parent, daughter) in enumerate(decay_chains[choice], 1):
            st.write(f"{i}. {parent} → {daughter}")