import pandas as pd
from geopy.distance import distance

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel("BuidlingLocations.xlsx")

# Define a function to calculate the distance between two coordinates
def calculate_distance(coords1, coords2):
    lat1, lon1 = coords1.split(",")
    lat2, lon2 = coords2.split(",")
    return distance((lat1, lon1), (lat2, lon2)).meters

# Define a function to find the nearest building to a set of coordinates
def find_nearest_building(coords):
    distances = []
    for building_coords in df["Coordinates "]:
        try:
            distances.append(calculate_distance(coords, building_coords))
        except ValueError:
            # Skip invalid coordinates
            continue
    nearest_idx = distances.index(min(distances))
    return df.loc[nearest_idx, "Building"]

# Test the function with some example coordinates
input_coords = "50.7381217,-3.5305564"
nearest_building = find_nearest_building(input_coords)
print(f"The nearest building to ({input_coords}) is {nearest_building}.")
