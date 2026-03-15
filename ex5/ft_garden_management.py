class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:

    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        try:
            if plant_name == "":
                raise PlantError("Plant name cannot be empty!")
            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening watering system")
        try:
            if len(self.plants) == 0:
                raise WaterError("No plants to water!")

            for plant in self.plants:
                print(f"Watering {plant} - success")

        except WaterError as e:
            print(f"Caught GardenError: {e}")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        try:
            if water_level < 1:
                raise ValueError(f"Water level {water_level} is too low (min 1)")
            if water_level > 10:
                raise ValueError(f"Water level {water_level} is too high (max 10)")

            if sunlight_hours < 2:
                raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
            if sunlight_hours > 12:
                raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")

            print(f"{plant_name}: healthy (water: {water_level}, sun: {sunlight_hours})")

        except ValueError as e:
            print(f"Error checking {plant_name}: {e}")


def test_garden_management():

    print("=== Garden Management System ===")

    manager = GardenManager()

    print("\nAdding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 8)

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()