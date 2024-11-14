from processor.EmailFinder import EmailFinder
from processor.PhoneNumberFinder import PhoneNumberFinder
from processor.UrlFinder import UrlFinder
from visualizer.BarPlotVisualizer import BarPlotVisualizer
from visualizer.ScatterPlotVisualizer import ScatterPlotVisualizer

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]

bar_plot = BarPlotVisualizer()
scatter_plot = ScatterPlotVisualizer()

# bar_plot.visualize_data(x, y)
# scatter_plot.visualize_data(x, y)

print("---------------------------------------------------------------------------------------------------------------")
text = """
Galite su mumis susisiekti: 
info@vcs.lt arba test@example.com.
Mūsų svetainės adresas: https://www.vilniuscoding.lt
+370(675)89568 arba +370(699)85236.
"""

email_finder = EmailFinder()
phone_finder = PhoneNumberFinder()
url_finder = UrlFinder()

processors = [email_finder, phone_finder, url_finder]

for processor in processors:
    print(processor.find_pattern(text))
