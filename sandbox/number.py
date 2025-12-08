class Number(object):
    def __init__(self, value: str, base: int = 10):
        super(Number, self).__init__()
        self._validate(value, base)
        self._str_value = value
        self._base = base
        self._int_value = int(value, base)

    def __str__(self):
        return f"{self._str_value} base {self._base}"

    @staticmethod
    def _validate(value: str, base: int):
        if base < 2 or base > 16:
            raise ValueError("Base must be between 2 and 16")
        allowed_characters = "0123456789ABCDEF"[:base]
        if any(c.upper() not in allowed_characters for c in value):
            raise ValueError(f"Value {value} is not valid for base {base}")

    def get(self, base: int = 10):
        return str(self._int_value)  # TODO: Implement base conversion


def main():
    print("Hello, Numbers!")
    my_number = Number("123", 4)
    print(my_number)
    print(my_number.get())


if __name__ == "__main__":
    main()
