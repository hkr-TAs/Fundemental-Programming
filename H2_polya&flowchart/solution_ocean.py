"""Use polyas problem solving techniques (including a flowchart)"""
# 237 Ex 9. Ocean levels

import math

ocean_level_rise = 1.6
num_of_years = int(input("\nEnter number of years to calculate >> "))
result = 0

for digit in range(num_of_years):
    result += ocean_level_rise

print(f"\nOcean level rise in {num_of_years} years -> {math.floor(result)}mm")
