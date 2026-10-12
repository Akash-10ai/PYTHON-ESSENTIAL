# Handling User Input (Traffic Light Simulator)

light_color = input("Enter the light color (red, yellow, green): ").lower()

if light_color == "red":
    print("Stop! Remaining stationary.")
elif light_color == "yellow":
    print("Slow down and prepare to stop.")
elif light_color == "green":
    print("Go! It is safe to proceed.")
else:
    print("Invalid color entered. Please check the traffic light.")