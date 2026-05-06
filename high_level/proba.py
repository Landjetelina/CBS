from typing import NamedTuple

class Tocka(NamedTuple):
    x: int
    y: int

tocka = Tocka(1, 1)
tocka = tocka._replace(x=2)
print(tocka)