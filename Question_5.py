import requests
import json

def download_and_extract_data(api_url):
    # Download data from the API
    response = requests.get(api_url)
    data = response.json()

    # Extract relevant data
    show_name = data['name']
    premiered = data['premiered']
    language = data['language']
    genres = data['genres']
    summary = data['summary']
    episodes = data['_embedded']['episodes']

    # Format the extracted data
    formatted_data = f"Show Name: {show_name}\n"
    formatted_data += f"Premiered: {premiered}\n"
    formatted_data += f"Language: {language}\n"
    formatted_data += f"Genres: {', '.join(genres)}\n"
    formatted_data += f"Summary: {summary}\n"

    formatted_data += "\nEpisode List:\n"
    for episode in episodes:
        episode_name = episode['name']
        season_number = episode['season']
        episode_number = episode['number']
        formatted_data += f"Season {season_number} Episode {episode_number}: {episode_name}\n"

    return formatted_data

# Provide the API URL
api_url = 'http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes'

# Call the function to download and extract the data
extracted_data = download_and_extract_data(api_url)

# Print or save the extracted data as per your requirement
print(extracted_data)
