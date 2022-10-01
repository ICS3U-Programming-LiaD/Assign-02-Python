
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Oct. 1st, 2022
# This program asks the user for the length of the Pentagon
# It calculates and displays the area and perimeter.

import math

# Input
side_len = float(input("What is the side length of the pentagon? = "))

# Process
pentagon_area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(side_len, 2)) / 4.0

pentagon_perimeter = 5 * side_len

# output
print("The pentagon's area is ", pentagon_area)
print("and the pentagon's perimeter is ", pentagon_perimeter)
