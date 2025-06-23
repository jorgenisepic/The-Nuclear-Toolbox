import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def reactor_designer_tool():
    st.subheader("🧱 Reactor Core Designer")
    st.markdown("""
Design a simple nuclear reactor core by adjusting:
- Fuel enrichment  
- Control rod insertion  
- Core size and layout  
This is a simplified visual simulator.
""")
    
 # Parameters
    enrichment = st.slider("Fuel Enrichment (%)", 0.7, 5.0, 3.0, step=0.1)
    control_rod_level = st.slider("Control Rod Insertion (%)", 0, 100, 50, step=5)
    core_radius = st.slider("Core Radius (cells)", 3, 10, 5)

    # Core grid simulation
    grid_size = core_radius * 2 + 1
    core = np.zeros((grid_size, grid_size))

    # Fill with fuel (high = enriched), low = rods
    for i in range(grid_size):
        for j in range(grid_size):
            distance = np.sqrt((i - core_radius) ** 2 + (j - core_radius) ** 2)
            if distance <= core_radius:
                fuel_effectiveness = enrichment * (1 - control_rod_level / 100)
                core[i, j] = fuel_effectiveness

    # Visualization
    fig, ax = plt.subplots(figsize=(6, 6))
    c = ax.imshow(core, cmap='hot', interpolation='nearest')
    fig.colorbar(c, label="Relative Reactivity")
    ax.set_title("Core Reactivity Map")
    ax.axis("off")
    st.pyplot(fig)

    # Summary
    k_eff_estimate = round((enrichment / 5) * (1 - control_rod_level / 100), 3)
    st.markdown(f"### 🔢 Estimated k-effective: `{k_eff_estimate}`")

    if k_eff_estimate < 0.95:
        st.info("🧊 Subcritical")
    elif 0.95 <= k_eff_estimate <= 1.05:
        st.success("⚖️ Critical")
    else:
        st.warning("🔥 Supercritical")
