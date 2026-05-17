import pandas as pd
import matplotlib.pyplot as plt

from services.forecast_service import moving_average_forecast

class DiseasesModule:

    def __init__(self):

        self.data = None

    # ---------------------------------

    def load_data(self, path):

        self.data = pd.read_csv(path)

        print("\n=== ТАБЛИЦА ===")

        print(self.data.to_string(index=False))

    # Что ты здесь анализируешь?

    def analyze(self):

        print("\n=== АНАЛИЗ ===")

        infections = {
            "tuberculosis_cases": "Туберкулез",
            "hiv_new_cases": "ВИЧ",
            "measles_cases": "Корь",
            "influenza_cases": "Грипп",
            "hepatitis_b_cases": "Гепатит B"
        }

        decrease = {}

        for column in infections:

            start = self.data[column].iloc[0]

            end = self.data[column].iloc[-1]

            decrease[column] = start - end

        max_decrease = max(
            decrease,
            key=decrease.get
        )

        min_decrease = min(
            decrease,
            key=decrease.get
        )

        print(
            "Максимальное снижение:",
            infections[max_decrease]
        )

        print(
            "Минимальное снижение:",
            infections[min_decrease]
        )

    # ---------------------------------
    # ГРАФИК + ПРОГНОЗ
    # ---------------------------------

    def build_graph(
        self,
        window=3,
        steps=5
    ):

        years = self.data["year"].tolist()

        infections = {
            "tuberculosis_cases": "Туберкулез",
            "hiv_new_cases": "ВИЧ",
            "measles_cases": "Корь",
            "influenza_cases": "Грипп",
            "hepatitis_b_cases": "Гепатит B"
        }

        plt.figure(figsize=(14, 7))

        future_years = list(
            range(
                years[-1] + 1,
                years[-1] + 1 + steps
            )
        )

        all_years = years + future_years

        for column, label in infections.items():

            values = self.data[column].tolist()

            forecast = moving_average_forecast(
                values,
                window,
                steps
            )

            # факт
            plt.plot(
                years,
                values,
                marker='o',
                linewidth=2,
                label=f"{label} (факт)"
            )

            # прогноз
            plt.plot(
                [years[-1]] + future_years,
                [values[-1]] + forecast,
                marker='o',
                linestyle='--',
                linewidth=2,
                label=f"{label} (прогноз)"
            )

        plt.title(
            "Инфекционные заболевания и прогноз"
        )

        plt.xlabel("Год")

        plt.ylabel("Количество случаев")

        plt.legend()

        plt.grid(True)

        plt.xticks(all_years, rotation=45)

        plt.tight_layout()

        plt.show()
