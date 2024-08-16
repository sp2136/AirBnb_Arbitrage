import requests
from bs4 import BeautifulSoup

# Set the URL to the search results page on Zillow
url = "https://www.zillow.com/homes/for_rent/Chicago-IL_rb/"

# Set the search parameters
params = {
    "searchQueryState": {
        "pagination": {
            "currentPage": 1
        },
        # "mapBounds": {
        #     "west": -122.521,
        #     "east": -122.355,
        #     "south": 37.704,
        #     "north": 37.833
        # },
        "usersSearchTerm": "Chicago, IL"
    }
}

# Send the request and get the response
response = requests.get(url, params=params)

# Parse the response using Beautiful Soup
soup = BeautifulSoup(response.text, "html.parser")

# Find all of the sale listings on the page
listings = soup.find_all("article", class_="list-card")

# Loop through the listings
for listing in listings:
    # Extract the details of the listing
    price = listing.find("div", class_="list-card-price").text.strip()
    address = listing.find("div", class_="list-card-addr").text.strip()
    days_listed = listing.find("div", class_="list-card-tag").text.strip()

    # Print the details of the listing
    print(f"{price} - {address} - {days_listed}")