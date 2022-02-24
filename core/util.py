import yaml
from munch import Munch


def get_config(fl):
    with open(fl, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return Munch.fromDict(data)
