# By < ₳ⱠØ₦Ɇ >
# // SPAMMERBOT MADE BY ₳ⱠØ₦Ɇ //

import sys
import logging
import importlib
from telethon import TelegramClient, events
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"ALONE/plugins/{plugin_name}.py")
    name = "ALONE.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["ALONE.plugins." + plugin_name] = load
    print("₳ⱠØ₦Ɇ SPAMMER BOT has IMPoRTED " + plugin_name)
