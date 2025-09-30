from website import create_application

app = create_application()

if __name__ == "__main__":
    # argument_parser = argparse.ArgumentParser()
    # argument_parser.add_argument("--debug", action="store_true")
    # application = create_application()
    # application.run(debug=argument_parser.parse_args().debug)
    app.run(debug=False)
