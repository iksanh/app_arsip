import locale
from datetime import datetime

def convert_date(date_str):
    # Set the locale to Indonesian
    locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')

    # Define the format of the input date string with Indonesian month names
    input_format = "%d %B %Y"  # Example: "28 Maret 2024"

    # Parse the input date string
    date_object = datetime.strptime(date_str, input_format)

    # Define the desired output format
    output_format = "%d/%m/%Y"  # Example: "28/04/2024" or "2/01/2024"

    # Format the date object to the desired output format
    formatted_date = date_object.strftime(output_format)

    return formatted_date

# Example usage
date1 = "28 Maret 2024"
date2 = "2 Januari 2024"

converted_date1 = convert_date(date1)
converted_date2 = convert_date(date2)

print(converted_date1)  # Output: "28/04/2024"
print(converted_date2)  # Output: "02/01/2024"
