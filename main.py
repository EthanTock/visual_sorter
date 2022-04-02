from data_visualizer import DataRenderer
from data import Data
from data_sorter import DataSorter
import random
import math

print(math.factorial(7))

LIST_LENGTH = 1000
input_data = list(range(1, LIST_LENGTH + 1))
random.shuffle(input_data)

processed_data = Data(input_data)
data_renderer = DataRenderer(processed_data)
# data_renderer.static()
data_renderer.bogo_sort()
data_renderer.correct_end()
