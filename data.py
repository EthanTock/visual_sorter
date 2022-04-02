class Data:

    def __init__(self, data: list):
        # Original
        self.original_data = data
        self.original_ceiling = max(self.original_data)
        self.original_floor = min(self.original_data)
        self.original_data_range = self.original_ceiling - self.original_floor
        self.original_length = len(self.original_data)
        # Temp
        self.data_range = self.original_data_range
        # Processed
        self.data = [{"val": val / self.data_range, "selected": False, "correct": False} for val in self.original_data]
        self.values = [item["val"] for item in self.data]
        self.ceiling = max(self.values)
        self.floor = min(self.values)
        self.data_range = self.ceiling - self.floor
        self.length = len(self.data)

    def multiply_data(self, multiplier):
        for item in self.data:
            item.update({"val": item["val"] * multiplier})
        self.update_data_stats()

    def truncate_data(self):
        for item in self.data:
            item.update({"val": round(item["val"])})
        self.update_data_stats()

    def update_data_stats(self):
        self.values = [item["val"] for item in self.data]
        self.ceiling = max(self.values)
        self.floor = min(self.values)
        self.data_range = self.ceiling - self.floor
        self.length = len(self.data)
