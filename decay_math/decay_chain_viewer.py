from graphviz import Digraph

decay_chains = {
    "U-238": ["U-238", "Th-234", "Pa-234", "U-234", "Th-230", "Ra-226", "Rn-222"],
    "Th-232": ["Th-232", "Ra-228", "Ac-228", "Th-228", "Ra-224", "Rn-220"],
    "Pu-239": ["Pu-239", "U-235", "Th-231", "Pa-231"]
}

def draw_decay_chain(isotope_name):
    if isotope_name not in decay_chains:
        print(f"⚠️ Isotope '{isotope_name}' not found.")
        return

    chain = decay_chains[isotope_name]
    dot = Digraph(comment=f'Decay Chain of {isotope_name}')

    for i in range(len(chain) - 1):
        dot.node(chain[i])
        dot.node(chain[i + 1])
        dot.edge(chain[i], chain[i + 1])

    filename = f"{isotope_name.replace('-', '_')}_decay_chain"
    dot.render(filename=filename, format='png', cleanup=True)
    print(f"✅ Decay chain saved as '{filename}.png'")

def decay_chain_viewer():
    print("🔗 Decay Chain Viewer (Graphviz Edition)")
    print("----------------------------------------")

    while True:
        isotope = input("Enter isotope (e.g. U-238), or 'exit' to quit: ").strip()
        if isotope.lower() == 'exit':
            break
        draw_decay_chain(isotope)
