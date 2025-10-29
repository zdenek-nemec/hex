class Number(object):
    def __init__(self, value: str, base: int = 10):
        super(Number, self).__init__()
        # self._validate(value, base)  # TODO: Validate that the string value could be a number in the given base
        self._str_value = value
        self._base = base
        self._int_value = int(value, base)

    def __str__(self):
        return f"{self._str_value} base {self._base}"

    def get(self, base: int = 10):
        return str(self._int_value)  # TODO


def main():
    print("Hello, Numbers!")
    my_number = Number("123", 4)
    print(my_number)
    print(my_number.get())


if __name__ == "__main__":
    main()
