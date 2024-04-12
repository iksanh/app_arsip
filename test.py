# import re

# # Your input string
# input_string = "393/SKet-75.100.UP.02.03/III/2024"
# input_string2 = 'UP.01.03/300-75.300/VIII/2023'

# # Define the initial regular expression pattern
# pattern1 = r'75[^a-zA-Z]*([a-zA-Z][^/]*)'
# pattern2 = r'([a-zA-Z]+(?:\.\d+)*)(?=/\d+-75)'

# # Search for the pattern in the input string
# match = re.search(pattern2, input_string2)

# # If a match is found with the initial pattern, print the result
# if match:
#     result = match.group(1)
#     print(result)
# else:
#     # Define the alternate regular expression pattern
    

#     # Search for the alternate pattern in the input string
#     match = re.search(pattern1, input_string2)

#     # If a match is found with the alternate pattern, print the result
#     if match:
#         result = match.group(1)
#         print(result)
#     else:
#         print("No match found.")


import re

# Your input string
input_string = "UT.01.03"

# Define the regular expression pattern to match "UP." or any other code
pattern = r'([A-Z]+)\.'

# Search for the pattern in the input string
match = re.search(pattern, input_string)

# If a match is found, print the result
if match:
    result = match.group(1)
    print(result)
else:
    print("No match found.")