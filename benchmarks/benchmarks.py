# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.
# import numpy as np
# import scqubits as scq
from asv_tester import bar

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.d = {}
        for x in range(500):
            self.d[x] = None

    def time_keys(self):
        for key in self.d.keys():
            pass

    def time_values(self):
        for value in self.d.values():
            pass

    def time_range(self):
        d = self.d
        for key in range(500):
            x = d[key]
    
    def time_slow_function(self):
        bar.slow_function()

    def time_has_packages(self):
        # np.arange(3)
        # tmon = scq.Transmon.create()
        bar.hello()


class MemSuite:
    def mem_list(self):
        return [0] * 256
