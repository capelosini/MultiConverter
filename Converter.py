class Core:
    def __init__(self):
        self.table = {
            # --- Comprimento ---
            "Meters": {"Yards": 1.094, "KMs": 0.001, "Feets": 3.281, "Miles": 1/1609.34, "Centimeters": 100, "Inches": 39.37},
            "Yards": {"Meters": 0.9144, "KMs": 0.0009144, "Feets": 3, "Miles": 1/1760, "Centimeters": 91.44, "Inches": 36},
            "KMs": {"Meters": 1000, "Yards": 1093.61, "Feets": 3280.84, "Miles": 0.621371, "Centimeters": 100000, "Inches": 39370.1},
            "Feets": {"Meters": 0.3048, "Yards": 1/3, "KMs": 0.0003048, "Miles": 1/5280, "Centimeters": 30.48, "Inches": 12},
            "Miles": {"Meters": 1609.34, "Yards": 1760, "KMs": 1.60934, "Feets": 5280, "Centimeters": 160934, "Inches": 63360},
            "Centimeters": {"Meters": 0.01, "Yards": 1/91.44, "KMs": 1e-5, "Feets": 1/30.48, "Miles": 1/160934, "Inches": 1/2.54},
            "Inches": {"Meters": 0.0254, "Yards": 1/36, "KMs": 2.54e-5, "Feets": 1/12, "Miles": 1/63360, "Centimeters": 2.54},

            # --- Massa / Peso ---
            "Kilograms": {"Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274, "Metric Tons": 0.001},
            "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
            "Pounds": {"Kilograms": 0.453592, "Grams": 453.592, "Ounces": 16},
            "Ounces": {"Kilograms": 0.0283495, "Grams": 28.3495, "Pounds": 1/16},
            "Metric Tons": {"Kilograms": 1000, "Pounds": 2204.62},

            # --- Volume Líquido (Unidades Comuns dos EUA) ---
            "Liters": {"Milliliters": 1000, "US Gallons": 0.264172, "US Quarts": 1.05669, "US Pints": 2.11338, "US Fluid Ounces": 33.814},
            "Milliliters": {"Liters": 0.001, "US Fluid Ounces": 0.033814},
            "US Gallons": {"Liters": 3.78541, "US Quarts": 4, "US Pints": 8, "US Fluid Ounces": 128},
            "US Quarts": {"Liters": 0.946353, "US Gallons": 1/4, "US Pints": 2, "US Fluid Ounces": 32},
            "US Pints": {"Liters": 0.473176, "US Gallons": 1/8, "US Quarts": 1/2, "US Fluid Ounces": 16},
            "US Fluid Ounces": {"Liters": 0.0295735, "Milliliters": 29.5735, "US Gallons": 1/128},

            # --- Armazenamento de Dados (Base 1024) ---
            "Bytes": {"Kilobytes": 1/1024, "Megabytes": 1/(1024**2), "Gigabytes": 1/(1024**3)},
            "Kilobytes": {"Bytes": 1024, "Megabytes": 1/1024, "Gigabytes": 1/(1024**2)},
            "Megabytes": {"Bytes": 1024**2, "Kilobytes": 1024, "Gigabytes": 1/1024, "Terabytes": 1/(1024**2)},
            "Gigabytes": {"Bytes": 1024**3, "Kilobytes": 1024**2, "Megabytes": 1024, "Terabytes": 1/1024},
            "Terabytes": {"Gigabytes": 1024, "Megabytes": 1024**2},

            # --- Tempo ---
            "Seconds": {"Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400},
            "Minutes": {"Seconds": 60, "Hours": 1/60, "Days": 1/1440},
            "Hours": {"Seconds": 3600, "Minutes": 60, "Days": 1/24},
            "Days": {"Seconds": 86400, "Minutes": 1440, "Hours": 24}
        }
        self.inputs = self.listUnitsInTable(self.table)
        
    def listUnitsInTable(self, table: dict):
        return list(dict.keys(table))
    
    def openSelectionMenu(self, lst: list) -> str:
        if type(lst) == dict:
            lst = list(dict.keys(lst))
        
        for e in enumerate(lst):
            print(f"{str(e[0])}: {str(e[1])}")
        
        while True:
            inp = input("\n$ ")
            try: inp = int(inp)
            except: continue
            inp %= len(lst)
            choice = str(lst[inp])
            print(f"'{choice}' Selected!")
            return choice
        
    def convert(self, n: float, inpUnit: str, outUnit: str):
        try:
            return n * self.table[inpUnit][outUnit]
        except:
            print("Error on converting the value!")
            exit()