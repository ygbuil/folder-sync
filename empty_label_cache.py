import json


def empty_label_cache(filename):
    with open(filename, "w") as file:
        json.dump({"origin": "", "destination": ""}, file, indent=2)


if __name__ == "__main__":
    empty_label_cache("label_cache.json")
