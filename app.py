from Converter import Core

print("\n-=-=-=-= Multi Converter V1.O =-=-=-=-\n\n")

core = Core()

print("Input Unit:")

inpUnit = core.openSelectionMenu(core.inputs)

while True:
    n = input("Number: ")
    if (n.isdecimal):
        n = float(n)
        break

print("\nOutput Unit:")

outUnit = core.openSelectionMenu(core.table[inpUnit])

convertedValue = core.convert(n, inpUnit, outUnit)

print(f"\n Result: {str(n)}|{inpUnit} -> {str(convertedValue)}|{outUnit}")
