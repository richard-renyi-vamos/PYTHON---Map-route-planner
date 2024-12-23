import folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_coordinates(address):
    """Get latitude and longitude for a given address."""
    geolocator = Nominatim(user_agent="map_route_planner")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        print(f"Could not find the location: {address}")
        return None

def plot_route(start_coords, end_coords):
    """Create a map with the route from start to end."""
    # Create a map centered at the midpoint between start and end
    midpoint = ((start_coords[0] + end_coords[0]) / 2, 
                (start_coords[1] + end_coords[1]) / 2)
    route_map = folium.Map(location=midpoint, zoom_start=13)
    
    # Add markers for start and destination
    folium.Marker(location=start_coords, popup="Start", icon=folium.Icon(color="green")).add_to(route_map)
    folium.Marker(location=end_coords, popup="Destination", icon=folium.Icon(color="red")).add_to(route_map)
    
    # Draw a line between the two points
    folium.PolyLine([start_coords, end_coords], color="blue", weight=5).add_to(route_map)
    
    # Save the map to an HTML file
    route_map.save("route_map.html")
    print("Map has been created! Open 'route_map.html' to view the route.")

def main():
    print("Welcome to the Python Map Route Planner!")
    
    # Get input addresses
    start_address = input("Enter the starting address: ")
    end_address = input("Enter the destination address: ")
    
    # Get coordinates for the addresses
    start_coords = get_coordinates(start_address)
    end_coords = get_coordinates(end_address)
    
    if start_coords and end_coords:
        # Calculate and display the distance
        distance = geodesic(start_coords, end_coords).kilometers
        print(f"The distance between the two locations is approximately {distance:.2f} km.")
        
        # Plot the route
        plot_route(start_coords, end_coords)
    else:
        print("Unable to create the route due to invalid addresses.")

if __name__ == "__main__":
    main()
