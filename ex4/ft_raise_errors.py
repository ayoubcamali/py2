def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name or not isinstance(plant_name, str):
        raise ValueError("Plant name cannot be empty!")
    
    if not isinstance(water_level, int) or water_level < 1 or water_level > 10:
        if water_level > 10:
            msg = f"Water level {water_level} is too high (max 10)"
        else:
            msg = f"Water level {water_level} is too low (min 1)"
        raise ValueError(msg)
    
    if not isinstance(sunlight_hours, int) or sunlight_hours < 2 or sunlight_hours > 12:
        if sunlight_hours > 12:
            msg = f"Sunlight hours {sunlight_hours} is too high (max 12)"
        else:
            msg = f"Sunlight hours {sunlight_hours} is too low (min 2)"
        raise ValueError(msg)
    
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    
    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 6, 8)
        print(result)
    except ValueError as e:
        print("Unexpected error:", e)
    
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 7)
    except ValueError as e:
        print("Error:", e)
    
    print("\nTesting bad water level...")
    try:
        check_plant_health("rose", 15, 9)
    except ValueError as e:
        print("Error:", e) 
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("basil", 4, 0)
    except ValueError as e:
        print("Error:", e)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()