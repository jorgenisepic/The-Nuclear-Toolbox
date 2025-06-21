from graphviz import Digraph
import streamlit as st

def show_decay_chain_viewer():
    decay_chains = {
        "Uranium-238": [
            ("U-238", "α", "4.5 billion years"),
            ("Th-234", "β⁻", "24 days"),
            ("Pa-234", "β⁻", "1.2 minutes"),
            ("U-234", "α", "245,000 years"),
            ("Th-230", "α", "75,000 years"),
            ("Ra-226", "α", "1,600 years"),
            ("Rn-222", "α", "3.8 days"),
            ("Po-218", "α", "3.1 minutes"),
            ("Pb-214", "β⁻", "27 minutes"),
            ("Bi-214", "β⁻", "20 minutes"),
            ("Po-214", "α", "164 μs"),
            ("Pb-210", "β⁻", "22 years"),
            ("Bi-210", "β⁻", "5 days"),
            ("Po-210", "α", "138 days"),
            ("Pb-206", "stable", "-")
        ],
        "Thorium-232": [
            ("Th-232", "α", "14 billion years"),
            ("Ra-228", "β⁻", "5.75 years"),
            ("Ac-228", "β⁻", "6.1 hours"),
            ("Th-228", "α", "1.9 years"),
            ("Ra-224", "α", "3.6 days"),
            ("Rn-220", "α", "55 seconds"),
            ("Po-216", "α", "0.15 seconds"),
            ("Pb-212", "β⁻", "10.6 hours"),
            ("Bi-212", "β⁻/α", "60 minutes"),
            ("Po-212", "α", "0.3 μs"),
            ("Tl-208", "β⁻", "3 minutes"),
            ("Pb-208", "stable", "-")
        ]
    }

    st.header("🧬 Decay Chain Viewer")
    choice = st.selectbox("Select a decay chain:", list(decay_chains.keys()))

    chain = decay_chains[choice]
    dot = Digraph(comment=f'Decay Chain of {choice}')

    for i in range(len(chain) - 1):
        parent, decay_type, half_life = chain[i]
        child = chain[i + 1][0]
        label = f"{decay_type} ({half_life})"
        dot.edge(parent, child, label=label)

    # Final node (stable)
    stable = chain[-1][0]
    dot.node(stable, f"{stable}\n(stable)", shape="box", style="filled", fillcolor="lightgreen")

    st.graphviz_chart(dot)
