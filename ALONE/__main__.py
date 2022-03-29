# By < ₳ⱠØ₦Ɇ>
# // SPAMMERBOT MADE BY ₳ⱠØ₦Ɇ //

import glob
from pathlib import Path
from ALONE.utils import load_plugins
import logging
from . import worker


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "ALONE/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("₳ⱠØ₦Ɇ SUCCESSFULLY DEPLOYED!")
print("Enjoy! SPAMMER BOT MADE BY ₳ⱠØ₦Ɇ™ (ALONE)")

if __name__ == "__main__":
    worker.run_until_disconnected()
