data =  [
            { "Estado": "Aguascalientes", "Extension Territorial (km^2)": 385, "Poblacion": 1425607 },
            { "Estado": "Baja California", "Extension Territorial (km^2)": 71450, "Poblacion": 3315766 },
            { "Estado": "Baja California Sur", "Extension Territorial (km^2)": 75675, "Poblacion": 712029 },
            { "Estado": "Campeche", "Extension Territorial (km^2)": 57924, "Poblacion": 928363 },
            { "Estado": "Puebla", "Extension Territorial (km^2)": 34251, "Poblacion": 6168883 },
        ]

for d in data:
    if d["Poblacion"] < 1000000:
        print(d)
        print("**********************************************************************************************")