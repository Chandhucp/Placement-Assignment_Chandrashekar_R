
import requests
import pandas as pd

def download_and_convert_data(url, output_file):
    # Download the data from the provided link
    response = requests.get(url)
    data = response.text

    # Convert the data into structured format (e.g., split by lines or separators)
    structured_data = data.split('\n')  # Split the data by lines, adjust the separator as per the data format

    # Create a DataFrame from the structured data
    df = pd.DataFrame(structured_data, columns=['Data'])  # Adjust column name as per the data structure

    # Save the DataFrame to Excel format
    df.to_excel(output_file, index=False)

    print("Data conversion completed. Output file:", output_file)

# Provide the URL of the data file to download
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Provide the desired output file path (including the .xlsx extension)
output_file = 'iris.xlsx'

# Call the function to download and convert the data
download_and_convert_data(url, output_file)
