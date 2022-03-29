from .. import worker
from telethon import events, Button

@worker.on(events.NewMessage(incoming=True, pattern="/alone"))
async def repo(event):
    await event.reply("Info About Alone",
                    buttons=[
                        [Button.url("GITHUB", url="https://github.com/improking")],
                        [Button.url("ALONE", url="https://t.me/you_r_hacked_001")]
                    ])