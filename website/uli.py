import logging
import timeit

from application_controller import ApplicationController

ULI_TYPE_FIELDS = {
    0x01: "CGI",
    0x02: "SAI",
    0x04: "RAI",
    0x08: "TAI",
    0x10: "ECGI",
}


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
        if len(uli) < 12:
            raise ValueError(f"Value {uli} is too short to be a valid ULI")
        index = 0
        uli_type = uli[index:index + 2]
        fields = self._get_fields(uli_type)

        self._uli_type = uli_type
        self._fields = fields

    def _get_fields(self, uli_type):
        fields = []
        for key in ULI_TYPE_FIELDS:
            if int(uli_type, 16) & key:
                fields.append(ULI_TYPE_FIELDS[key])
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


def main():
    application_controller = ApplicationController()

    logging.info("Application started")
    application_start_time = timeit.default_timer()

    uli = Uli("1F0000000000")
    print(uli.get_formatted_uli())
    [print(item) for item in uli.get_uli_details()]

    application_stop_time = timeit.default_timer()
    logging.debug(f"Finished in {application_stop_time - application_start_time:.1f}s")
    logging.info("Application finished")


if __name__ == "__main__":
    main()
