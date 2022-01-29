import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def City_Search(loc_name):
    df = pd.read_csv('airport_codes.csv')

    location_data = []
    for city, country, airport in zip(df['City name'], df['Country name'], df['Airport Name']):
        if loc_name.lower() in city.lower():
            location_data.append({'city': city, 'country': country, 'airport': airport})
        
        if loc_name.lower() in country.lower():
            location_data.append({'city': city, 'country': country, 'airport': airport})

        if loc_name.lower() in airport.lower():
            location_data.append({'city': city, 'country': country, 'airport': airport})
    
        if len(location_data) >= 20:
            break

    return location_data

# loc_name = "Delhi"
# data = City_Search(loc_name)
# print(data)
    