# Import numpy
import numpy as np
height_in = [1.56,1.71,1.82,1.66,1.9]
weight_lb = [154,176,180.5,140,164.46]
# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / (np_height_m ** 2)

# Print out bmi
print(bmi)
