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
        match uli_type:
            case "01":
                return "CGI"
            case "02":
                return "SAI"
            case "04":
                return "RAI"
            case "05":
                return "CGI and RAI"
            case "06":
                return "SAI and RAI"
            case "08":
                return "TAI"
            case "10":
                return "ECGI"
            case "18":
                return "TAI and ECGI"
            case "19":
                return "CGI, TAI and ECGI"
            case "1A":
                return "SAI, TAI and ECGI"
            case "1C":
                return "RAI, TAI and ECGI"
            case "1E":
                return "SAI, RAI, TAI and ECGI"
