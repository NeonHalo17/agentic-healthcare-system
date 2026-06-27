import time


class PerformanceLogger:

    def __init__(self):
        self.timings = {}

    def start(self, module):
        self.timings[module] = {
            "start": time.perf_counter()
        }

    def stop(self, module):
        self.timings[module]["end"] = (time.perf_counter())

    def results(self):
        output = {}
        for module, values in self.timings.items():
            output[module] = round((values["end"] - values["start"]) * 1000,2)

        return output
