import streamlit as st
import graphviz

def display_decay_chain(isotope):
    chains = {
        "Uranium-238": [
            ("U-238", "Th-234", "α"),
            ("Th-234", "Pa-234", "β⁻"),
            ("Pa-234", "U-234", "β⁻"),
            ("U-234", "Th-230", "α"),
            ("Th-230", "Ra-226", "α"),
            ("Ra-226", "Rn-222", "α"),
            ("Rn-222", "Po-218", "α"),
            ("Po-218", "Pb-214", "α"),
            ("Pb-214", "Bi-214", "β⁻"),
            ("Bi-214", "Po-214", "β⁻"),
            ("Po-214", "Pb-210", "α"),
            ("Pb-210", "Bi-210", "β⁻"),
            ("Bi-210", "Po-210", "β⁻"),
            ("Po-210", "Pb-206", "α")
        ],
        "Thorium-232": [
            ("Th-232", "Ra-228", "α"),
            ("Ra-228", "Ac-228", "β⁻"),
            ("Ac-228", "Th-228", "β⁻"),
            ("Th-228", "Ra-224", "α"),
            ("Ra-224", "Rn-220", "α"),
            ("Rn-220", "Po-216", "α"),
            ("Po-216", "Pb-212", "α"),
            ("Pb-212", "Bi-212", "β⁻"),
            ("Bi-212", "Po-212", "β⁻"),
            ("Po-212", "Pb-208", "α")
        ],
        "Uranium-235": [
            ("U-235", "Th-231", "α"),
            ("Th-231", "Pa-231", "β⁻"),
            ("Pa-231", "Ac-227", "β⁻"),
            ("Ac-227", "Th-227", "β⁻"),
            ("Th-227", "Ra-223", "α"),
            ("Ra-223", "Rn-219", "α"),
            ("Rn-219", "Po-215", "α"),
            ("Po-215", "Pb-211", "α"),
            ("Pb-211", "Bi-211", "β⁻"),
            ("Bi-211", "Tl-207", "α"),
            ("Tl-207", "Pb-207", "β⁻")
        ]
    }

    chain = chains.get(isotope)
    if not chain:
        st.warning("Isotope not available.")
        return

    g = graphviz.Digraph(format='svg')
    g.attr(rankdir='LR', size='10')

    for parent, child, decay_type in chain:
        color = "crimson" if decay_type == "α" else "deepskyblue"
        label = f"{decay_type}-decay"
        g.edge(parent, child, label=label, color=color)

    st.graphviz_chart(g)