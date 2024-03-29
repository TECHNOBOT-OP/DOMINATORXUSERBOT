import os
from keep_alive import keep_alive

keep_alive()
import sys
import time

from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger

from DominatorBot.clients.session import H2, H3, H4, H5, Dominator, DominatorBot
from DominatorBot.config import Config


StartTime = time.time()
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))


if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)


LOGS = getLogger(__name__)

bot = Dominator
tbot = DominatorBot


if not Config.API_HASH:
    LOGS.warning("Please fill var API_HASH to continue.")
    quit(1)


if not Config.APP_ID:
    LOGS.warning("Please fill var APP_ID to continue.")
    quit(1)


if not Config.BOT_TOKEN:
    LOGS.warning("Please fill var BOT_TOKEN to continue.")
    quit(1)
    
    
# if not Config.BOT_USERNAME:
#     LOGS.warning("Please fill var BOT USERNAME to continue.")
#     quit(1)
    

if not Config.DB_URI:    
    LOGS.warning("Please fill var DATABASE_URL to continue.")
    quit(1)


if not Config.DOMINATORBOT_SESSION:
    LOGS.warning("Please fill var DOMINATORBOT_SESSION to continue.")
    quit(1)


try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None


# global variables
CMD_LIST = {}
CMD_HELP = {}
CMD_HELP_BOT = {}
CMD_INFO = {}
INT_PLUG = ""
LOAD_PLUG = {}
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
ISAFK = False
AFKREASON = None
SUDO_LIST = {}


# DominatorBot
