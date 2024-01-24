import ephem
import math

# Example ephem angle in radians
ephem_angle_radians = ephem.degrees('96:40:34.5')

# Convert ephem angle to degrees
degrees_value = math.degrees(ephem_angle_radians)

print("Ephem Angle (Radians):", ephem_angle_radians)
print("Degrees:", degrees_value)
