import geocoder

# def get_gps_coordinates():
#     try:
#         location = geocoder.ip('me')
#         latitude, longitude = location.latlng
#         return latitude, longitude
#     except Exception as e:
#         print(f"Error: {e}")
#         return None
#
# def main():
#     coordinates = get_gps_coordinates()
#
#     if coordinates:
#         latitude, longitude = coordinates
#         print(f"Our GPS coordinates are:\nLatitude: {latitude}\nLongitude: {longitude}")
#     else:
#         print("Unable to retrieve GPS coordinates.")

if __name__ == "__main__":
    # main()
    g = geocoder.ip('me')
    g.address