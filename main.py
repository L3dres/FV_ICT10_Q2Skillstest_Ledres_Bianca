from pyscript import document
#non metal elements
#Dictionary w info about non metals 
# planet name: Symbol, name, number, mass

nonmetals = {"Xenon": ("Xe", 54, 131.29),
           "Hydrogen": ("H", 1, 1.00784),
           "Carbon": ("C", 6, 12.011),
           "Nitrogen": ("N", 7, 14.007),
           "Phosphorus": ("P", 15, 30.974),
           "Oxygen": ("O", 8, 15.999),
           "Sulfur": ("S", 16, 32.06),
           "Selenium": ("Se", 34, 78.971),
           "Fluorine": ("F", 9, 18.998),
           "Chlorine": ("Cl", 17, 35.4527),
           "Bromine": ("Br", 35, 79.904),
           "Iodine": ("I", 53, 126.904),
           "Helium": ("He", 2, 4.0026),
           "Neon": ("Ne", 10, 20.18),
           "Argon": ("Ar", 18, 39.948),
           "Krypton": ("Kr", 36, 83.798),
           "Radon": ("Rn", 86, 222)
           }


# Create a function to search a planet
def search_nonmetal(e):
    #get the input from HTML
    nonmetal1 = document.getElementById("nonmetal1").value
    #retrieve information from the dictionary
    result = nonmetals.get(nonmetal1, ("Nonmetal not found", "-", "-"))
    # for fallback ^
    # display of result 
    document.getElementById("name").innerText = nonmetal1
    document.getElementById("symbol").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]

#display