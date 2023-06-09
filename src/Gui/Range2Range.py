from src.Gui.Range2D import Range2D


class Range2Range:
    def __init__(self, w: Range2D, f: Range2D):
        self._world = w
        self._frame = f

    def world2frame(self, pos: tuple):
        new_pos = self._world.get_portion(pos)
        return self._frame.from_portion(new_pos)

    def frame2world(self, pos: tuple):
        new_pos = self._frame.get_portion(pos)
        return self._world.from_portion(new_pos)

    def get_world(self):
        return self._world

    def get_frame(self):
        return self._frame
