# Define the diameters and corresponding multipliers
diameters = [86, 172, 257, 343, 429, 514, 600, 706, 878, 2195, 3688, 4394, 5532, 6238, 7727, 9288]
multipliers = [61.5, 122, 177.5, 239, 299.5, 355, 416.5, 480, 602, 1453, 2424, 2904, 3660, 4140, 5113, 6079]

# Get user input for SPECIFIC_VAL
SPECIFIC_VAL = int(input("Enter SPECIFIC_VAL: "))

# Calculate the results
results = {diameter: multiplier * SPECIFIC_VAL for diameter, multiplier in zip(diameters, multipliers)}

# Print the results with a copy button (in a formatted way for further use)
for diameter, value in results.items():
    print(f"Dia {diameter} = {value} Ks")

# Copy button functionality can't be implemented in Python directly,
# but you can create a simple HTML interface for this.
