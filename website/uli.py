SUPPORTED_ULI_TYPES = ["01", "02", "04", "05", "06", "08", "10", "18", "19", "1A", "1C", "1E"]


class Uli(object):
    def __init__(self, uli: str):
        self._uli = uli
        self._uli_type = ""
        self._mcc_mnc = ""
        self._rest = ""
        if self.is_valid():
            self._parse_uli()

    def is_valid(self):
        uli = self._uli
        if uli == "" or len(uli) < 7:
            return False
        elif not uli[0:2] in SUPPORTED_ULI_TYPES:
            return False
        else:
            return True

    def _parse_uli(self):
        uli = self._uli
        self._uli_type = uli[0:2]
        self._mcc_mnc = uli[2:7]
        self._rest = uli[7:]

    def get_formatted_uli(self):
        return self._uli + " = " + self._uli_type + " " + self._mcc_mnc + " " + self._rest

    def get_uli_details(self):
        return [
            f"ULI type {self._uli_type} = {self._get_type_description(self._uli_type)}",
            f"MCC-MNC {self._mcc_mnc}"
        ]

    def _get_type_description(self, uli_type):
            if uli_type == "01":
                return "CGI"
            elif uli_type == "02":
                return "SAI"
            elif uli_type == "04":
                return "RAI"
            elif uli_type == "05":
                return "CGI and RAI"
            elif uli_type == "06":
                return "SAI and RAI"
            elif uli_type == "08":
                return "TAI"
            elif uli_type == "10":
                return "ECGI"
            elif uli_type == "18":
                return "TAI and ECGI"
            elif uli_type == "19":
                return "CGI, TAI and ECGI"
            elif uli_type == "1A":
                return "SAI, TAI and ECGI"
            elif uli_type == "1C":
                return "RAI, TAI and ECGI"
            elif uli_type == "1E":
                return "SAI, RAI, TAI and ECGI"
            else:
                return "Unknown"
