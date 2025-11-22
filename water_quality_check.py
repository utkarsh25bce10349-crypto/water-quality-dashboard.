import csv
import matplotlib.pyplot as plt

def calculate_wqi(pH, turbidity, dissolved_oxygen):
    w_ph = 0.3
    w_turbidity = 0.3
    w_do = 0.4

    # Calculate pH score
    if 6.5 <= pH <= 8.5:
        pH_score = 100
    else:
        pH_score = max(0, 100 - abs(pH - 7)*20)

    # Calculate turbidity score
    if turbidity <= 5:
        turbidity_score = 100
    else:
        turbidity_score = max(0, 100 - (turbidity - 5)*10)

    # Calculate dissolved oxygen score
    if dissolved_oxygen >= 5:
        do_score = 100
    else:
        do_score = max(0, 20 * dissolved_oxygen)

    # Weighted WQI calculation
    wqi = (pH_score * w_ph) + (turbidity_score * w_turbidity) + (do_score * w_do)
    return round(wqi, 2)

def categorize_wqi(wqi):
    if wqi >= 80:
        return "Good"
    elif 50 <= wqi < 80:
        return "Fair"
    elif 25 <= wqi < 50:
        return "Poor"
    else:
        return "Very Poor"

def get_sample_inputs():
    samples = []
    try:
        n = int(input("Enter number of water samples: "))
    except ValueError:
        print("Please enter a valid integer.")
        return None

    for i in range(n):
        print(f"\nSample {i+1}:")
        try:
            pH = float(input("  Enter pH (0-14): "))
            turbidity = float(input("  Enter turbidity (NTU): "))
            dissolved_oxygen = float(input("  Enter dissolved oxygen (mg/L): "))
        except ValueError:
            print("  Invalid input. Please enter numeric values.")
            return None
        if not (0 <= pH <= 14):
            print("  pH must be between 0 and 14.")
            return None
        if turbidity < 0 or dissolved_oxygen < 0:
            print("  Turbidity and dissolved oxygen cannot be negative.")
            return None
        samples.append((pH, turbidity, dissolved_oxygen))
    return samples

def save_results_to_csv(results, filename="WQI_results.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Sample", "pH", "Turbidity (NTU)", "Dissolved Oxygen (mg/L)", "WQI", "Category"])
        for idx, r in enumerate(results, start=1):
            writer.writerow([idx, r['pH'], r['turbidity'], r['dissolved_oxygen'], r['wqi'], r['category']])
    print(f"\nResults saved to {filename}")

def plot_wqi(results):
    if not results:
        print("No data to plot.")
        return
    samples = list(range(1, len(results) + 1))
    wqi_values = [r['wqi'] for r in results]

    plt.plot(samples, wqi_values, marker='o')
    plt.title("Water Quality Index (WQI) Over Samples")
    plt.xlabel("Sample Number")
    plt.ylabel("WQI")
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()

def main():
    samples = get_sample_inputs()
    if samples is None:
        return

    results = []
    for pH, turbidity, dissolved_oxygen in samples:
        wqi = calculate_wqi(pH, turbidity, dissolved_oxygen)
        category = categorize_wqi(wqi)
        results.append({
            "pH": pH,
            "turbidity": turbidity,
            "dissolved_oxygen": dissolved_oxygen,
            "wqi": wqi,
            "category": category
        })

    print("\nWater Quality Results:")
    for i, res in enumerate(results, start=1):
        print(f" Sample {i}: WQI = {res['wqi']}, Category = {res['category']}")

    save_results_to_csv(results)
    plot_wqi(results)

if __name__ == "__main__":
    main()
