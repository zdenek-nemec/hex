import argparse

from website import create_application


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--debug", action="store_true")
    application = create_application()
    application.run(debug=argument_parser.parse_args().debug)


if __name__ == "__main__":
    main()
