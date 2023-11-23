import json
from constants import *


def read_cache():
    with open(LABEL_CACHE, "r") as json_file:
        return json.load(json_file)
