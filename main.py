import json
import logging

from config import Config

from auth import create_app

LOG = logging.getLogger()

with open('config/local.json') as file:
    config_object = Config(json.load(file))

app = create_app(config_object)
