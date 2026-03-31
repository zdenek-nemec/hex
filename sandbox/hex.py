class Hex(object):
    def __init__(self, value: str):
        self._value = int(value)

    def get_value(self, base: int = 10):
        if base == 2:
            return f"{self._value:b}"
        elif base == 10:
            return f"{self._value}"
        elif base == 16:
            return f"{self._value:x}".upper()
        else:
            raise ValueError(f"Base {base} is not supported")
