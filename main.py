from pyscript import document

# Dictionary storing non-metal elements: Symbol -> (Name, Atomic Number, Atomic Mass)
non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.003),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.95),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222.00)
}

def element_checker(e):
    # Get user input 
    symbol_input = document.getElementById("element_name").value.strip()
    
    result_div = document.getElementById("result")
    
    # Check the symbol
    if symbol_input in non_metals:
        data = non_metals[symbol_input]
        name = data[0]
        atomic_num = data[1]
        atomic_mass = data[2]
        
        result_div.innerHTML = f"""
            <div>
                <b>Symbol:</b> {symbol_input}<br>
                <b>Element Name:</b> {name}<br>
                <b>Atomic Number:</b> {atomic_num}<br>
                <b>Atomic Mass:</b> {atomic_mass}
            </div>
        """
    else:
        result_div.innerHTML = f"""
            <span class="text-danger">
                <i class="bi bi-exclamation-triangle-fill"></i> 
                Sorry, <b>"{symbol_input}"</b> does not exist in the non-metals list or is an invalid symbol.
            </span>
        """