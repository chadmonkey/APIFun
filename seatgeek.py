import configparser
import requests

config = configparser.ConfigParser()
config.read("config.properties")

# SeatGeek API credentials
api_key = config.get("API_KEYS", "SEATGEEK_CLIENT_ID")
api_key = config.get("API_KEYS", "SEATGEEK_CLIENT_SECRET")

# Replace this with your target event ID (you can find it via search endpoint)
event_id = 1234567

# API endpoint for event details
url = f'https://api.seatgeek.com/2/events/{event_id}?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}'

response = requests.get(url)

if response.status_code == 200:
    event_data = response.json()

    print("Event:", event_data.get('title'))
    print("Date & Time:", event_data.get('datetime_local'))
    print("Venue:", event_data.get('venue', {}).get('name'))

    # Show ticket pricing info
    stats = event_data.get('stats', {})
    print("\nTicket Prices:")
    print(f"- Lowest Price: ${stats.get('lowest_price')}")
    print(f"- Highest Price: ${stats.get('highest_price')}")
    print(f"- Average Price: ${stats.get('average_price')}")

    # Show seating chart link (if available)
    if event_data.get('venue', {}).get('location'):
        print("\nSeating Map URL:", event_data.get('venue', {}).get('url'))

else:
    print("Error fetching event data:", response.status_code, response.text)
