import tomllib


def main():
    read_toml()


def read_toml():
    with open("./example.toml", "rb") as f:
        toml_data = tomllib.load(f)
        print(toml_data["title"])
        dob = toml_data["owner"]["dob"]
        print(dob)
        print(type(dob))


def add_notes_to_exception():
    try:
        raise TypeError("Some type error")
    except TypeError as type_error:
        type_error.add_note("Add some information")
        # reraise the error
        raise


if __name__ == "__main__":
    add_notes_to_exception()
    # main()
