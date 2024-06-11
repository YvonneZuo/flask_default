from os import environ as env

DEBUG_MODE = int(env.get('DEBUG_MODE', 1))
PORT = int(env.get("PORT", 8080))