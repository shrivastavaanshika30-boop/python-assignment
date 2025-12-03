#TITTLE: CAMPUS ENERGY USE DASHBOARD
#NAME: ANSHIKA SHRIVASTAVA
#DESCRIPTION: A Python-based dashboard that ingests monthly energy data, analyzes building-wise electricity usage, and generates clear visual and textual summaries for campus facilities in one automated script.


import os
import glob
import pandas as pd
import matplotlib.pyplot as plt



class MeterReading:
    def __init__(self, timestamp, kwh, peak_kwh):
        self.timestamp = timestamp
        self.kwh = kwh
        self.peak_kwh = peak_kwh


class Building:
    def __init__(self, name):
        self.name = name
        self.readings = []

    def add_reading(self, reading):
        self.readings.append(reading)

    def get_dataframe(self):
        df = pd.DataFrame([{
            "timestamp": r.timestamp,
            "kwh": r.kwh,
            "peak_kwh": r.peak_kwh
        } for r in self.readings])

        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df.set_index("timestamp")

    def daily_total(self):
        return self.get_dataframe().resample("D").sum()

    def weekly_total(self):
        return self.get_dataframe().resample("W").sum()



def load_csv_files(folder):
    buildings = {}

    for file in glob.glob(os.path.join(folder, "*.csv")):
        try:
            df = pd.read_csv(file)

            df = df.rename(columns={
                "Date": "timestamp",
                "Building": "building",
                "Consumption_kWh": "kwh",
                "PeakHour_kWh": "peak_kwh"
            })

        
            df = df.dropna(subset=["timestamp", "building", "kwh"])

            for _, row in df.iterrows():
                bname = row["building"]

                if bname not in buildings:
                    buildings[bname] = Building(bname)

                buildings[bname].add_reading(
                    MeterReading(row["timestamp"], row["kwh"], row["peak_kwh"])
                )

        except Exception as e:
            print(f"Skipping {file}: {e}")

    return buildings




def save_cleaned_data(buildings):
    rows = []

    for bname, b in buildings.items():
        df = b.get_dataframe().reset_index()
        df["building"] = bname

        if not df.empty:
            rows.append(df)

    if not rows:
        print("⚠ No data loaded — nothing to save.")
        return

    final = pd.concat(rows)
    final.to_csv("cleaned_energy_data.csv", index=False)
    print("✔ Cleaned CSV saved: cleaned_energy_data.csv")




def print_summary(buildings):
    print("\n=== EXECUTIVE SUMMARY ===")
    for name, b in buildings.items():
        df = b.get_dataframe()
        print(f"\nBuilding: {name}")
        print(f"  Total Consumption: {df['kwh'].sum():.2f} kWh")
        print(f"  Peak Hour Total: {df['peak_kwh'].sum():.2f} kWh")
        print(f"  Average Daily Use: {b.daily_total()['kwh'].mean():.2f} kWh")
        print(f"  Highest Consumption Day: {b.daily_total()['kwh'].idxmax().date()}")




def generate_charts(buildings):
    fig, axs = plt.subplots(3, 1, figsize=(12, 15))
    fig.suptitle("Campus Energy Dashboard", fontsize=18)

    for name, b in buildings.items():
        daily = b.daily_total()
        axs[0].plot(daily.index, daily["kwh"], label=name)

    axs[0].set_title("Daily Energy Trend")
    axs[0].set_ylabel("kWh")
    axs[0].legend()


    weekly_totals = {name: b.weekly_total()["kwh"].sum() for name, b in buildings.items()}
    axs[1].bar(weekly_totals.keys(), weekly_totals.values())
    axs[1].set_title("Weekly Total Consumption")
    axs[1].set_ylabel("kWh")


    for name, b in buildings.items():
        df = b.get_dataframe()
        df["hour"] = df.index.hour
        axs[2].scatter(df["hour"], df["peak_kwh"], label=name)

    axs[2].set_title("Peak Hour Energy Scatter")
    axs[2].set_xlabel("Hour")
    axs[2].set_ylabel("Peak kWh")
    axs[2].legend()

    plt.tight_layout()
    plt.savefig("energy_dashboard.png")
    plt.show()




if __name__ == "__main__":
    folder_path = r"C:\Users\Dell\Desktop\CAMPUS USE DASHBOARD"  
    buildings = load_csv_files(folder_path)

    save_cleaned_data(buildings)
    print_summary(buildings)
    generate_charts(buildings)

