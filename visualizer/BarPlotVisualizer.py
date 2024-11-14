import matplotlib.pyplot as plt

from visualizer.DataVisualizer import DataVisualizer


class BarPlotVisualizer(DataVisualizer):
    def visualize_data(self, x, y):
        plt.bar(x, y, color='red')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.title('Bar Plot Visualization')
        plt.show()
