import streamlit as st
from isotopes_database.isotope_database import isotope_data
import pandas as pd

def compare_isotopes():
    st.header("⚖️ Compare Isotopes")

    # Sort for better UX
    isotope_names = sorted([f"{i['symbol']} ({i['name']})" for i in isotope_data])

    selected = st.multiselect("Select isotopes to compare:", isotope_names, max_selections=5)

    if selected:
        # Map back to data
        filtered = []
        for choice in selected:
            sym = choice.split(" ")[0]
            match = next((iso for iso in isotope_data if iso['symbol'] == sym), None)
            if match:
                filtered.append(match)

        df = pd.DataFrame(filtered)
        st.subheader("🔬 Isotope Comparison Table")
        st.dataframe(df.set_index("symbol"), use_container_width=True)

        # Optional chart
        st.subheader("📊 Decay Energy Comparison")
        chart_data = pd.DataFrame({
            "Isotope": [f"{i['symbol']}" for i in filtered],
            "Decay Energy (MeV)": [float(i['energy'].split()[0]) for i in filtered],
        })
        st.bar_chart(chart_data.set_index("Isotope"))

    else:
        st.info("Select up to 5 isotopes from the list to compare.")

