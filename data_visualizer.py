import tkinter as tk
from data import Data
import time
import random

WINDOW_BG_COLOR = "#222222"
CANVAS_COLOR = "#000000"
COLUMN_COLOR = "#FFFFFF"
COLUMN_CORRECT_COLOR = "#00FF00"
COLUMN_SELECTED_COLOR = "#FF0000"

FRAME_LENGTH = 0.1


class DataRenderer:

    def __init__(self, data: Data):
        self.data_obj = data
        self.data = self.data_obj.data
        if self.data_obj.length > 500:
            self.canvas_width = self.data_obj.length
        else:
            self.canvas_width = 500
        self.canvas_height = round(self.canvas_width * 3 / 5)

        if abs(self.data_obj.ceiling) < abs(self.data_obj.floor):
            multiplier = self.canvas_height / abs(self.data_obj.floor)
        else:
            multiplier = self.canvas_height / abs(self.data_obj.ceiling)
        self.data_obj.multiply_data(multiplier)
        self.data_obj.truncate_data()

        self.data_values = data.values
        self.window = tk.Tk()
        self.window.title("Data Visualizer")
        self.window.config(bg=WINDOW_BG_COLOR)
        self.data_canvas = tk.Canvas(
            self.window,
            width=self.canvas_width,
            height=self.canvas_height,
            bg=CANVAS_COLOR,
            highlightthickness=0
        )
        self.data_canvas.grid(row=0, column=0)

    def render_tkinter_frame(self):
        self.data_canvas.delete("all")

        column_width = round(self.canvas_width / self.data_obj.length)
        self.canvas_width = column_width * self.data_obj.length
        self.data_canvas.config(width=self.canvas_width)
        if self.data_obj.ceiling <= 0:
            column_baseline_y = 0
        elif self.data_obj.floor >= 0:
            column_baseline_y = self.canvas_height
        else:
            column_baseline_y = self.canvas_height / 2

        column_pos = 0
        for column in self.data:
            column_height = column["val"]
            column_rectangle_points = column_pos, \
                column_baseline_y, \
                column_pos + column_width, \
                column_baseline_y - column_height
            if column["correct"]:
                color = COLUMN_CORRECT_COLOR
            elif column["selected"]:
                color = COLUMN_SELECTED_COLOR
            else:
                color = COLUMN_COLOR
            self.data_canvas.create_rectangle(column_rectangle_points, fill=color, width=0)
            column_pos += column_width

        self.window.update()

    def bogo_sort(self):
        self.window.title("Data Visualizer: bogo_sort")

        sorted_data = self.data_values.copy()
        sorted_data.sort()

        frame = 0
        while self.data_values != sorted_data:
            print(self.data_values)
            random.shuffle(self.data)
            self.data_values = [item["val"] for item in self.data]
            self.render_tkinter_frame()
            time.sleep(FRAME_LENGTH)
            frame += 1

        self.correct_end()

        self.window.mainloop()

    def static(self):
        self.render_tkinter_frame()
        self.window.mainloop()

    def correct_end(self):
        frames = 30
        slice_length = round(self.data_obj.length / frames)
        for frame_num in range(frames):
            for item in self.data[frame_num * slice_length:(frame_num + 1) * slice_length]:
                item["correct"] = True
            self.render_tkinter_frame()
        self.window.mainloop()
