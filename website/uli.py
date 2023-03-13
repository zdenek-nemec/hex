class Uli(object):
    def __init__(self, uli: str):
        self._uli = uli

    def get_uli_readable(self):
        return self._uli + " ...X"
