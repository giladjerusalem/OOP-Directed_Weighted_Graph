class Range:
    def __init__(self, _min, _max, _range=None):
        if _range is None:
            self._min = _min
            self._max = _max
        else:
            self._min = _range.get_min()
            self._max = _range.get_max()

    def get_max(self):
        return self._max

    def get_min(self):
        return self._min

    def get_length(self):
        return self._max - self._min

    def set_max(self, _max):
        self._max = _max

    def set_min(self, _min):
        self._min = _min

    def get_portion(self, d):
        d1 = d - self._min
        return d1 / self.get_length()

    def from_portion(self, p):
        return self._min + p * self.get_length()
