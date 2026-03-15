def check_temperature(temp_str):
    try:
        temp = int(temp_str)

        if temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

        if temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

        return temp

    except ValueError:
        if not temp_str.lstrip("-").isdigit():
            raise ValueError(f"'{temp_str}' is not a valid number")
        else:
            raise


def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]

    for value in tests:
        print(f"Testing temperature: {value}")

        try:
            temp = check_temperature(value)
            print(f"Temperature {temp}°C is perfect for plants!")
        except ValueError as e:
            print(f"Error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
