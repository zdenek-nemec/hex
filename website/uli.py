SUPPORTED_ULI = ["01", "02", "04", "05", "06", "08", "10", "18", "19", "1A", "1C", "1E"]

class Uli(object):
    def __init__(self, uli: str):
        self._uli = uli

    def is_valid(self):
        if self._uli == "":
            return False
        elif not self._uli[0:2] in SUPPORTED_ULI:
            return False
        else:
            return True

    def get_formatted_uli(self):
        return self._uli + " ...X"

    def get_uli_details(self):
        return ["a", "b"]
