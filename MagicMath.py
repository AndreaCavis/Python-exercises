class MagicMath:
    def __init__(self) -> None:
        pass

    def set(self, x: int) -> None:
        self.x = x

    def __add__(self, other):
        return 36