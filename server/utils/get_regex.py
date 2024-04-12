import re

def get_kode_dokumen(string):
    # Extract code from the input string
    match = re.search(r"/(\w+)-\d+|(\w+\.\d+\.\d+/\d+-\d+)|(\w+\.\d+\.\d+/\d+-\d+\.\d+)|(\w+\.\d+\.\d+)/", string)
    if match:
        # Return the code string
        return match.group(1) if match.group(1) else 'SD'
    else:
        # Return None if no match is found
        return None
    




def get_kode_klasifikasi(input_string):
    """
    Extracts substrings from the given string that match the specified regex pattern.
    
    Parameters:
        input_string (str): The input string to search through.
        
    Returns:
        str: Substring from input_string that matches the pattern.
    """
    # Define the initial regular expression pattern
    # if input like 393/SKet-75.100.UP.02.03/III/2024 the output UP.02.03
    pattern1 = r'75[^a-zA-Z]*([a-zA-Z][^/]*)'

    # if input like UP.01.03/300-75.300/VIII/2023 the output UP.01.03
    pattern2 = r'([a-zA-Z]+(?:\.\d+)*)(?=/\d+-75)'
    # Search for the pattern in the input string
    match = re.search(pattern2, input_string)

    # If a match is found with the initial pattern, print the result
    if match:
        result = match.group(1)
        return result
    else:
        # Define the alternate regular expression pattern
        

        # Search for the alternate pattern in the input string
        match = re.search(pattern1, input_string)

        # If a match is found with the alternate pattern, print the result
        if match:
            result = match.group(1)
            return result
        else:
            return None

 

def get_pengelola(input_string):
    # Define the regular expression pattern to match "UP." or any other code

    if isinstance(input_string, bytes):
        input_string = input_string.decode()

    pattern = r'([A-Z]+)\.'

    # Search for the pattern in the input string
    match = re.search(pattern, get_kode_klasifikasi(input_string))

    # If a match is found, return the result
    if match:
        return match.group(1)
    else:
        return None