
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "82d3b3e552cec2660f402542ddebc41f"
