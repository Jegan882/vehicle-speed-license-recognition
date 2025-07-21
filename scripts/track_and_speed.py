RED_LINE_Y = 300
BLUE_LINE_Y = 500
frame_rate = 30
pixel_to_meter = 0.05
frame_red = 10
frame_blue = 30

distance = (BLUE_LINE_Y - RED_LINE_Y) * pixel_to_meter
time_taken = (frame_blue - frame_red) / frame_rate
speed_kmph = (distance / time_taken) * 3.6
print(f"Estimated speed: {speed_kmph:.2f} km/h")
    # Placeholder: object tracking (use same vehicle ID)
    # Assume y=300 in frame 30, y=500 in frame 45 → speed = dist/time
    
    # Your actual tracking code goes here

# Estimate speed = (distance_in_meters) / (time_in_seconds)
# Example:
# speed = ((BLUE_LINE_Y - RED_LINE_Y) * pixel_to_meter) / ((frame45 - frame30)/frame_rate)
