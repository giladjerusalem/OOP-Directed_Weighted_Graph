from src.Gui.Range import Range


class Range2D:
    def __init__(self, x: Range, y: Range):
        self._x_range: Range = x
        self._y_range: Range = y

    def get_portion(self, pos: tuple) -> tuple:
        x = self._x_range.get_portion(pos[0])
        y = self._y_range.get_portion(pos[1])
        return x, y, 0

    def from_portion(self, pos: tuple) -> tuple:
        x = self._x_range.from_portion(pos[0])
        y = self._y_range.from_portion(pos[1])
        return x, y, 0

    def get_x_range(self):
        return self._x_range

    def get_y_range(self):
        return self._y_range
