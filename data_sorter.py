import data_visualizer
import random


class DataSorter:

    def __init__(self, data_obj):
        self.data_obj = data_obj
        self.data = self.data_obj.data
        self.data_renderer = data_visualizer.DataRenderer(self.data_obj)

    def bogo_sort(self):
        self.data_renderer.bogo_setup()

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

        self.data_renderer.window.mainloop()

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
