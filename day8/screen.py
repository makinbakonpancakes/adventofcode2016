import numpy as np
import re


class Screen:
    """A dead screen Santa found."""

    def __init__(self, h, w):
        """Initialize with a height and a width."""
        self.pixles = np.zeros((h, w))

    def command(self, cmd):
        """Handles any of the three alloed commands."""
        ex = r'(rect|rotate row|rotate column) ((\d+)x(\d+)|.+=(\d+) by (\d+))'
        m = re.match(ex, cmd)
        m.group(3)
        if m:
            if m.group(1) == 'rect':
                self.rect(int(m.group(3)), int(m.group(4)))
            elif m.group(1) == 'rotate row':
                self.row_shift(int(m.group(5)), int(m.group(6)))
            else:
                self.col_shift(int(m.group(5)), int(m.group(6)))

    def rect(self, a, b):
        """Turn on AXB pixles starting from top left."""
        self.pixles[:b, :a] = 1

    def col_shift(self, a, b):
        """Shift all the pixles in column A down by B."""
        self.pixles[:, a] = np.roll(self.pixles[:, a], b)

    def row_shift(self, a, b):
        """Shift all the pixles in row A right by B."""
        self.pixles[a, :] = np.roll(self.pixles[a, :], b)

    def lights_on(self):
        """How many lights are on?"""
        return self.pixles.sum()

    def __str__(self):
        """Show the pixles."""
        return("\n".join(["".join(map(lambda x: "." if x == 0 else "#", line))
                          for line in self.pixles]))
