import matplotlib.pyplot as plt

from visualizer.DataVisualizer import DataVisualizer


class ScatterPlotVisualizer(DataVisualizer):
    def visualize_data(self, x, y):
        plt.scatter(x, y, color='blue')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.title('Scatter Plot Visualization')
        plt.show()
