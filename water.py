import csv

# Function to check pH and Turbidity status
def check_thresholds(ph, turbidity):
    status = []

    # pH check
    if ph < 6.5:
        status.append("Low pH")
    elif ph > 8.5:
        status.append("High pH")
    else:
        status.append("Safe pH")

    # Turbidity check
    if turbidity > 5:
        status.append("High Turbidity")
    else:
        status.append("Safe Turbidity")

    return ", ".join(status)


# Function to get water quality of a specific area
def get_water_quality(area_name, filename):
    found = False

    try:
        with open("row1.csv", "r") as file:
            reader = csv.reader(file)

            # Skip header row
            header = next(reader)

            for row in reader:
                # Expected format: [Area, pH, Turbidity]
                if len(row) < 3:
                    continue

                area = row[0].strip()
                ph = float(row[1])
                turbidity = float(row[2])

                if area.lower() == area_name.strip().lower():
                    status = check_thresholds(ph, turbidity)

                    print("\n Water Quality Report ")
                    print("Area:", area)
                    print("pH:", ph)
                    print("Turbidity:", turbidity)
                    print("Status:", status)

                    found = True
                    break

        if not found:
            print(f"\nArea '{area_name}' not found in the dataset.")

    except FileNotFoundError:
        print("Error: CSV file not found.")
    except ValueError:
        print("Error: Invalid numeric data in CSV.")


# ---------- MAIN PROGRAM ----------
print(" Water Quality Monitoring System ")

area_input = input("Enter the area name: ")
get_water_quality(area_input, "row1.csv")
