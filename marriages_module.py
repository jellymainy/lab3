import pandas as pd
import matplotlib.pyplot as plt

from services.forecast_service import moving_average_forecast

class MarriagesModule:

    def __init__(self):
        self.data = None

    def load_data(self, path):
        self.data = pd.read_csv(path)
        
        print("\nТАБЛИЦА")
        print(self.data.to_string(index=False))

    def show_statistics(self):
        print("\nСТАТИСТИКА")
        
        male_marriage = self.data["male_peak_marriage_age"].mode()[0]
        female_marriage = self.data["female_peak_marriage_age"].mode()[0]
        male_divorce = self.data["male_peak_divorce_age"].mode()[0]
        female_divorce = self.data["female_peak_divorce_age"].mode()[0]
        
        print("Мужчины чаще женились:", male_marriage)
        print("Женщины чаще выходили замуж:", female_marriage)
        print("Мужчины чаще разводились:", male_divorce)
        print("Женщины чаще разводились:", female_divorce)
        
    def build_marriages_graph(self, window=3, steps=5):
        years = self.data["year"].tolist()
        values = self.data["marriages_total"].tolist()
        
        forecast = moving_average_forecast(values, window, steps)
        future_years = list(range(years[-1] + 1, years[-1] + 1 + steps))
        all_years = years + future_years
        
        plt.figure(figsize=(12, 6))
        
        # факт
        plt.plot(years, values, marker='o', linewidth=2, label='Браки (факт)')
        # прогноз
        plt.plot([years[-1]] + future_years, [values[-1]] + forecast, marker='o', linestyle='--', linewidth=2, label='Браки (прогноз)')
        plt.title("Браки в России")
        plt.xlabel("Год")
        plt.ylabel("Количество")
        plt.legend()
        plt.grid(True)
        plt.xticks(all_years, rotation=45)
        plt.tight_layout()
        plt.show()