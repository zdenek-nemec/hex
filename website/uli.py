class Uli(object):
    def __init__(self, uli: str):
        self._uli = uli
        self._valid = True
        self._uli_type = None
        self._fields = None
        try:
            self._parse_uli()
        except:
            self._valid = False

    def is_valid(self):
        return self._valid

    def _parse_uli(self):
        uli = self._uli
        if len(uli) < 2:
            self._valid = False
            return
        self._uli_type = uli[0:2]
        self._fields = self._get_fields(self._uli_type)

    def _get_fields(self, uli_type):
        fields = []
        if uli_type[0] == "1":
            fields.append("ECGI")
        right = f"{int(uli_type[1], 16):04b}"
        if right[0] == "1":
            fields.append("TAI")
        if right[1] == "1":
            fields.append("RAI")
        if right[2] == "1":
            fields.append("SAI")
        if right[3] == "1":
            fields.append("CGI")
        return fields

    def _get_type_description(self):
        return " ".join(self._fields)

    def get_formatted_uli(self):
        parsed = []
        if self._uli_type:
            parsed.append(self._uli_type)
        parsed.append("...")
        return self._uli + " = " + " ".join(parsed)

    def get_uli_details(self):
        details = []
        if self._uli_type:
            details.append(f"ULI type {self._uli_type} = {self._get_type_description()}")
        return details
