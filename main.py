import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    """Διαβάζει το αρχείο CSV."""
    data = pd.read_csv("energy_data.csv")
    return data


def calculate_statistics(data):
    """Υπολογίζει και εμφανίζει βασικά στατιστικά."""

    total = data["Consumption_kWh"].sum()
    average = data["Consumption_kWh"].mean()
    maximum = data["Consumption_kWh"].max()
    minimum = data["Consumption_kWh"].min()

    max_index = data["Consumption_kWh"].idxmax()
    max_date = data.loc[max_index, "Date"]

    print("\n----- ΣΤΑΤΙΣΤΙΚΑ -----")
    print(f"Συνολική κατανάλωση: {total:.2f} kWh")
    print(f"Μέση κατανάλωση: {average:.2f} kWh")
    print(f"Μέγιστη κατανάλωση: {maximum:.2f} kWh")
    print(f"Ελάχιστη κατανάλωση: {minimum:.2f} kWh")
    print(f"Η μεγαλύτερη κατανάλωση έγινε στις: {max_date}")

    if average > 15:
        print("⚠️ Υψηλή μέση κατανάλωση")
    else:
        print("✅ Φυσιολογική μέση κατανάλωση")


def calculate_cost(data):
    """Υπολογίζει το συνολικό κόστος ενέργειας."""

    price_per_kwh = float(
        input("\nΔώσε την τιμή ανά kWh (€): ")
    )

    total_consumption = data["Consumption_kWh"].sum()
    total_cost = total_consumption * price_per_kwh

    print(f"Συνολικό κόστος: {total_cost:.2f} €")


def check_high_consumption(data):
    """Εμφανίζει τις ημέρες με κατανάλωση πάνω από 16 kWh."""

    print("\nΗμέρες με υψηλή κατανάλωση:")

    found = False

    for index, row in data.iterrows():
        if row["Consumption_kWh"] > 16:
            print(
                f"{row['Date']} -> "
                f"{row['Consumption_kWh']} kWh"
            )
            found = True

    if not found:
        print("Δεν βρέθηκαν ημέρες με υψηλή κατανάλωση.")


def plot_graph(data):
    """Εμφανίζει και αποθηκεύει γράφημα κατανάλωσης."""

    plt.figure(figsize=(8, 4))

    plt.plot(
        data["Date"],
        data["Consumption_kWh"],
        marker="o"
    )

    plt.title("Ημερήσια Κατανάλωση Ενέργειας")
    plt.xlabel("Ημερομηνία")
    plt.ylabel("kWh")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("energy_consumption_chart.png")

    plt.show()


def main():
    data = load_data()

    print(data)

    calculate_statistics(data)
    calculate_cost(data)
    check_high_consumption(data)
    plot_graph(data)


main()