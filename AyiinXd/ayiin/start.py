from telethon import Button
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
)

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://vault.pictures/p/2bbbdcf75e0243349d7d72a735933657",
                caption="𝗥𝗢𝗘𝗠𝗔𝗛𝗝𝗔𝗦𝗘𝗕-Userbot.\n     **status : Active\n     ketik `.ping` untuk cek bot!**",
                buttons=[(Button.url("Channel", "https://t.me/roemahjaseb")),
                         (Button.url("Support", "https://t.me/roemahjasebsupport"))]
            )
    except Exception as e:
        LOGS.error(e)
        return None
