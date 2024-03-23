import requests # Import the ' requests' module for making HTTP requests.

def find_location():
    # Use the 'reäüests' module to get the public IP address of the machine using the ipify API.
    ipadd= requests.get("https://api.ipify.org").text
    # Construct the URL for obtaining geographic information based on the IP address using the geojs.io API.
    url = "https://get.geojs.io/v1/ip/geo/" + ipadd + ".json"
    #print(url)     # Print the constructed URL for debugging purposes.

    # Use 'requests' to send a GET request to the geojs.io API and get the geographic information in JSON format.
    geo = requests.get(url)
    geo_data = geo.json()

    #print(geo_data)     # Print the obtained geographic information in JSON format.

    # Extract relevant information from the JSON response.
    city = geo_data['city']
    country = geo_data['country']
    state = geo_data['region']
    latitude = geo_data['latitude']
    longitude = geo_data['longitude']
    timezone = geo_data['timezone']
    internet = geo_data['organization']

    # Print the extracted information in a formatted manner.
    #print(f"city = {city}\nstate = {state}\ncountry = {country}\n\nlatitude = {latitude}\nlongitude = {longitude}\ntimezone = {timezone}\ninternet = {internet}")

    # Return a formatted string containing the geographic information.
    return f"You are currently in {city} city of {state} state in {country}"

# your_locatiton = find_location()
# print(your_locatiton)