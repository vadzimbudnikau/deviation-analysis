# Импортируйте необходимые библиотеки
import pandas as pd
import matplotlib.pyplot as plt
import os


class Plotter:
    def draw_plots(self, json_file):
        df = pd.read_json(json_file)

        os.makedirs("plots", exist_ok=True)

        mean_deviation_histogram = df["Mean"].plot.hist()
        plt.title("Mean Deviation Histogram")
        plt.xlabel("Deviation (degrees)")
        plt.ylabel("Frequency")
        plt.savefig("plots/mean_deviation_histogram.png")
        plt.close()

        return [
            "plots/mean_deviation_histogram.png"
        ]


plotter = Plotter()

resulting_plots = plotter.draw_plots("deviation.json")

for plot_path in resulting_plots:
    print(f"Создан график: {plot_path}")
