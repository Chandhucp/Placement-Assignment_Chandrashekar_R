import requests
import pandas as pd
import json

def download_and_convert_data(url, output_file):
    # Download the data from the provided link
    response = requests.get(url)
    data = response.json()

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)

    print("Data conversion completed. Output file:", output_file)

# Provide the URL of the data file to download
url = 'https://data.nasa.gov/resource/y77d-th95.json'

# Provide the desired output file path (including the .csv extension)
output_file = 'output.csv'

# Call the function to download and convert the data
download_and_convert_data(url, output_file)
