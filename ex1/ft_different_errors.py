def garden_operations():
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("Testing KeyError...")
    plants = {"rose": 25, "sunflower": 80}
    try:
        plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()

    print("Testing multiple errors together...")
    try:
        int("not_a_number")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
