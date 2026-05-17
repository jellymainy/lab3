import pandas as pd
import matplotlib.pyplot as plt

from services.forecast_service import moving_average_forecast

class HousingModule:

    def __init__(self):

        self.data = None

    # ---------------------------------

    def load_data(self, path):

        self.data = pd.read_csv(path)

        print("\n=== ТАБЛИЦА ===")

        print(self.data.to_string(index=False))

    # ---------------------------------

    def calculate_changes(self):

        print("\n=== АНАЛИЗ ===")

        columns = {
            "studio_price_per_sqm": "Студии",
            "one_room_price_per_sqm": "1-комнатные",
            "two_room_price_per_sqm": "2-комнатные",
            "three_room_price_per_sqm": "3-комнатные"
        }

        growth = {}

        for column in columns:

            start = self.data[column].iloc[0]

            end = self.data[column].iloc[-1]

            growth[column] = end - start

        max_growth = max(
            growth,
            key=growth.get
        )

        min_growth = min(
            growth,
            key=growth.get
        )

        print(
            "Сильнее всего подорожали:",
            columns[max_growth]
        )

        print(
            "Минимальный рост:",
            columns[min_growth]
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

        columns = {
            "studio_price_per_sqm": "Студии",
            "one_room_price_per_sqm": "1-комнатные",
            "two_room_price_per_sqm": "2-комнатные",
            "three_room_price_per_sqm": "3-комнатные"
        }

        plt.figure(figsize=(14, 7))

        future_years = list(
            range(
                years[-1] + 1,
                years[-1] + 1 + steps
            )
        )

        all_years = years + future_years

        for column, label in columns.items():

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
            "Цены на первичное жилье и прогноз"
        )

        plt.xlabel("Год")

        plt.ylabel("Цена за м²")

        plt.legend()

        plt.grid(True)

        plt.xticks(all_years, rotation=45)

        plt.tight_layout()

        plt.show()
