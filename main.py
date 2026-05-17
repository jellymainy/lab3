from modules.marriages_module import MarriagesModule
from modules.housing_module import HousingModule
from modules.diseases_module import DiseasesModule

import pandas as pd
import matplotlib.pyplot as plt

def main():

    isExit = 0
    while isExit == 0:
        
        print("1 - Браки и разводы")
        print("2 - Жилье")
        print("3 - Заболевания")
        print("4 - Выйти")

        choice = input(
            "Выберите модуль: "
        )

        # ---------------------------------

        if choice == "1":

            module = MarriagesModule()

            module.load_data(
                "marriages.csv"
            )

            module.show_statistics()

            module.build_marriages_graph()

            module.build_divorces_graph()

        # ---------------------------------

        elif choice == "2":

            module = HousingModule()

            module.load_data(
                "housing.csv"
            )

            module.calculate_changes()

            module.build_graph()

        # ---------------------------------

        elif choice == "3":

            module = DiseasesModule()

            module.load_data(
                "diseases.csv"
            )

            module.analyze()

            module.build_graph()
        
        # ---------------------------------
        
        elif choice == "4":
            isExit = 1

        # ---------------------------------

        else:

            print("Неверный выбор")


if __name__ == "__main__":

    main()


