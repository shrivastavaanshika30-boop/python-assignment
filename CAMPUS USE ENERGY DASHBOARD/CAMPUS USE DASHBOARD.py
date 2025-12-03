#TITTLE: CAMPUS ENERGY USE DASHBOARD
#NAME: ANSHIKA SHRIVASTAVA
#DESCRIPTION: A Python-based dashboard that ingests monthly energy data, analyzes building-wise electricity usage, and generates clear visual and textual summaries for campus facilities in one automated script.


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df = pd.read_csv("JAN.csv")   


df["Date"] = pd.to_datetime(df["Date"])


start_date = df["Date"].min().strftime("%d-%b-%Y")
end_date = df["Date"].max().strftime("%d-%b-%Y")
total_buildings = df["Building"].nunique()


daily_consumption = df.groupby("Date")["Consumption_kWh"].sum()

building_totals = df.groupby("Building")["Consumption_kWh"].sum()


df_sorted = df.sort_values("Date")


fig, axs = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Electricity Consumption Dashboard", fontsize=18, fontweight="bold")


axs[0, 0].plot(daily_consumption.index, daily_consumption.values, linewidth=2)
axs[0, 0].set_title("Daily Electricity Consumption")
axs[0, 0].set_xlabel("Date")
axs[0, 0].set_ylabel("Consumption (kWh)")
axs[0, 0].xaxis.set_major_formatter(mdates.DateFormatter("%d-%b"))
axs[0, 0].grid(True, alpha=0.3)


axs[0, 1].axis("off")  

summary_text = (
    f"Total Buildings : {total_buildings}\n"
    f"Start Date       : {start_date}\n"
    f"End Date         : {end_date}\n"
)

axs[0, 1].text(
    0.05, 0.8, "SUMMARY", fontsize=16, fontweight="bold"
)
axs[0, 1].text(
    0.05, 0.55,
)
