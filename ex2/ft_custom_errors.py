class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant_name, message):
        self.plant_name = plant_name
        super().__init__(f"The {plant_name} plant {message}!")


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(f"Not enough water in the tank! {message}")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        raise PlantError("tomato", "is wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        raise WaterError("Tank is almost empty")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("tomato", "is wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Tank is almost empty")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
