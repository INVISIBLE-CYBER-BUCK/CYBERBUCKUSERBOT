from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 12160082
    API_HASH = "d4628d23654c7afb8ae808f869d85cd9"
    # the name to display in your alive message
    ALIVE_NAME = "CYBER BUCK"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://wyscvopwknuhdp:20fcf2a74264bd61c4db5c5a2449fb7c3599e207feb550ced2bff39a46202a55@ec2-52-3-200-138.compute-1.amazonaws.com:5432/dnjk7ou4uv1q4"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    CYBER_STRING = "1BVtsOLgBu6RlfM_ecaY9GdmGtTIQTTq50_Jl5rrc4mZcIado1tEBw09gSjq6B7BJWqx1Yfmki8xPI-GreS7dya5q-_JTt1vwp6jYt9ucoUEHLAsW13bW4bOAZQZAHE28bW5rqDfv8IvwKtkHdOIVJhEqPRiY9VVDYwsmdIHs0HUuEaNDsp1yElyN6U6AouDA6zg3hxcJZZWfpJZ3xDd1Wik3cp2epX29oK4VA9iFp3D18BgAYDYttCMWGw0DWg4VALB6o3X4zcO6ihxTeDFCsPJxBzdIn2drQiYNcGq2BKOUImjaOrXVeDwld9RAQ85vIcknOgYRt5MprkQHIDR7P-0iDW46f3E="
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = "5828120691:AAG_-23YM0JrUbIThBTEnFSGdbBudfP4Dwc"
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTRA_REPO = "https://github.com/ITS-LEGENDBOT/PLUGINS"
    UPSTREAM_REPO = "pro"
    # Your City's TimeZone
    TZ = "India"
