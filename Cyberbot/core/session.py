import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..Config import Config
from .client import LegendClient

__version__ = "1.10.6"

loop = None

if Config.CYBER_STRING:
    session = StringSession(str(Config.CYBER_STRING))
else:
    session = "CyberUserBot"

try:
    legend = LegendClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"CYBER_STRING - {e}")
    sys.exit()

legend.tgbot = tgbot = LegendClient(
    session="LegendTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)
