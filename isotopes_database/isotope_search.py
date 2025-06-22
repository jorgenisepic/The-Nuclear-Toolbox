import streamlit as st
from isotopes_database.isotope_database import isotope_data

def isotope_searcher():
    st.header("🔍 Isotope Database Search")

    query = st.text_input("Enter isotope name or symbol (e.g., Cs-137, Iodine)").strip().lower()

    if query:
        found = [i for i in isotope_data if query in i['name'].lower() or query in i['symbol'].lower()]
        
        if found:
            for iso in found:
                st.markdown(f"### {iso['name']} ({iso['symbol']})")
                st.write(f"**Half-life:** {iso['half_life']}")
                st.write(f"**Decay Mode:** {iso['decay_mode']}")
                st.write(f"**Decay Energy:** {iso['energy']}")
                st.markdown("---")
        else:
            st.warning("No matching isotope found.")
    else:
        st.info("Start typing to search the isotope database.")
