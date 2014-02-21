import collections
import itertools
import random

import au3bind


class Minesweeper():

    BOMBED, OK, WIN = tuple(range(3))

    def __init__(self, caption):

        self.caption = caption
        self.au3 = au3bind.autoit()

        self.au3.AU3_AutoItSetOption("SendKeyDelay", 50)
        self.au3.AU3_AutoItSetOption("SendKeyDownDelay", 50)
        self.au3.AU3_AutoItSetOption("SendCapslockMode", 0)
        self.au3.AU3_AutoItSetOption("WinTitleMatchMode", 2)
        self.au3.AU3_AutoItSetOption("MouseClickDownDelay", 25)
        self.au3.AU3_AutoItSetOption("MouseCoordMode", 2)
        self.au3.AU3_AutoItSetOption("PixelCoordMode", 2)

        self.size = 16
        self.x0 = 12
        self.y0 = 55

        self.blocks = {
            0xce783f7d: "closed",
            0xa463f89d: "flagged",
            0x4bf47e84: "bomb",
            0x96a1c9e5: "bomb",
            0x97e328df: 0,
            0xd5fcf6a8: 1,
            0x5a6db710: 2,
            0xa000db12: 3,
            0x55ebc6d0: 4,
            0xa9aeae50: 5,
            0x7291ced0: 6,
            0xa4c5c5d0: 7,
        }


    def run(self):

        self.au3.AU3_WinActivate(self.caption)

        width = self.au3.AU3_WinGetClientSizeWidth("")
        height = self.au3.AU3_WinGetClientSizeHeight("")

        self.xcount = (width - self.x0 + 1) // self.size
        self.ycount = (height - self.y0 + 1) // self.size

        self.clicked = []
        self.closed = list(itertools.product(range(self.xcount), range(self.ycount)))
        self.field = collections.defaultdict(lambda: 0)
        ret = Minesweeper.OK
        while ret == Minesweeper.OK:

            self.au3.AU3_WinWaitActive(self.caption)
            ret = self.step()

        return ret


    def new_game(self):

        self.au3.AU3_WinWaitActive(self.caption)
        self.au3.AU3_Send("{F2}")


    def refresh_field(self):

        nclosed = []
        for ix, iy in self.closed:

            px = self.x0 + ix * self.size
            py = self.y0 + iy * self.size

            crc = self.au3.AU3_PixelChecksum(px, py, px + self.size - 1, py + self.size - 1)
            if crc not in self.blocks:

                print(
                    str.format(
                        "crc '0x{:0>8x}' not in blocks (ix, iy) = ({}, {}), (px, py) = ({}, {})",
                        crc,
                        ix,
                        iy,
                        px,
                        py,
                    )
                )
                exit()

            v = self.blocks[crc]
            self.field[(ix, iy)] = v
            if v == "closed":

                nclosed.append((ix, iy))

        self.closed = nclosed


    def neighbour(self, x, y):

        for dx, dy in itertools.product(range(-1, 2), range(-1, 2)):

            if not (dx == 0 and dy == 0):

                yield x + dx, y + dy


    def gen_primary_sets(self, f):

        for x, y in itertools.product(range(self.xcount), range(self.ycount)):

            v = f[(x, y)]
            if isinstance(v, int) and v > 0:

                closed = set()
                flagged = 0
                for nx, ny in self.neighbour(x, y):

                    nv = f[(nx, ny)]
                    if nv == "closed":

                        closed.add((nx, ny))

                    elif nv == "flagged":

                        flagged += 1

                if closed:

                    yield v - flagged, closed


    def click(self, x, y, button="left"):

        px = self.x0 + x * self.size + self.size // 2
        py = self.y0 + y * self.size + self.size // 2
        self.au3.AU3_MouseClick(button, px, py, 1, 0)


    def gen_sets(self, sets):

        yield from iter(sets)

        for (ac, aset), (bc, bset) in itertools.combinations(sets, 2):

            if aset <= bset:

                yield bc - ac, bset - aset

            elif bset <= aset:

                yield ac - bc, aset - bset


    def step(self):

        changed = False

        if self.refresh_field() == Minesweeper.WIN:

            return Minesweeper.WIN

        if "bomb" in self.field.values():

            return Minesweeper.BOMBED

        sets = list(self.gen_primary_sets(self.field))

        flagged = []

        # checking obvious situation
        for count, closed in self.gen_sets(sets):

            if count == 0:

                for x, y in closed:

                    if (x, y) not in self.clicked:

                        self.click(x, y)
                        self.clicked.append((x, y))
                        changed = True

            elif count == len(closed):

                # mark all as bombs
                for x, y in closed:

                    if (x, y) not in flagged:

                        self.click(x, y, "right")
                        flagged.append((x, y))
                        changed = True


        # random click, huh
        if not changed and "closed" in self.field.values():

            x, y = random.choice(tuple(filter(lambda k: self.field[k] == "closed", self.field)))
            self.click(x, y)
            changed = True

        if changed:

            return Minesweeper.OK

        else:

            return Minesweeper.WIN


if __name__ == "__main__":

    import time

    # caption = input("Minesweeper caption (enter for 'Сапер'): ") or "Сапер"
    caption = "Сапер"
    ms = Minesweeper(caption)
    start = time.perf_counter()
    while True:

        if ms.run() == Minesweeper.WIN:

            print(
                str.format(
                    "Win! ({:.3f}s.)",
                    time.perf_counter() - start,
                )
            )
            time.sleep(5)

        else:

            print(
                str.format(
                    "Bombed! ({:.3f}s.)",
                    time.perf_counter() - start,
                )
            )

        ms.new_game()
        start = time.perf_counter()
