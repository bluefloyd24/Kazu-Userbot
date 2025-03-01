# repack by blue. #
""" Userbot initialization. """

import logging
import os
import re
import sys
import time
from asyncio import get_event_loop
from base64 import b64decode
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from math import ceil
from pathlib import Path
from sys import version_info

from dotenv import load_dotenv
from platform import python_version
from git import Repo
from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from requests import get
from telethon import Button, __version__ as vsc
from telethon.errors import UserIsBlockedError
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, custom, events
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name

from .storage import Storage


def STORAGE(n):
    return Storage(Path("data") / n)


load_dotenv("config.env")

LOOP = get_event_loop()
StartTime = time.time()
repo = Repo()
branch = repo.active_branch.name

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
CMD_LIST = {}
SUDO_LIST = {}
ZALG_LIST = {}
LOAD_PLUG = {}
INT_PLUG = ""
ISAFK = False
AFKREASON = None
ENABLE_KILLME = True

# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("asyncio").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
logging.getLogger("telethon.network.connection.connection").setLevel(logging.ERROR)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info(
        "Anda HARUS memiliki python setidaknya versi 3.8."
        "Beberapa fitur tergantung versi python ini. Bot berhenti."
    )
    sys.exit(1)

if CONFIG_CHECK := os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None
):
    LOGS.info(
        "Harap hapus baris yang disebutkan dalam tagar pertama dari file config.env"
    )
    sys.exit(1)

while 0 < 6:
    _DEVS = get(
        "https://raw.githubusercontent.com/roemahjaseb/roemahjase/Kazu-Userbot/app.json"
    )
    if _DEVS.status_code != 200:
        if 0 != 5:
            continue
        DEVS = [
            1700405732,
            1841642016,
            1663657124,
            1905050903,
            844432220,
            883761960,
            2130526178,
            1700405732,
            1663258664,
            2062364017,
            2073495031,
            5063062493,
            902478883,
            1694909518,
            1755047203,
            1824630420,
            750233563,
            1054295664,
            1889573907,
            1898065191,
            1810243126,
            1936017380,
            1992087933,
            817945139,
            482945686,
            816526222,
            1557184285,
            1928772230,
            5089916692,
            1441342342,
            7176613752,
            6037364404,
            7053717310,
            6878107336,
            1254466650,
            6080567417,
        ]
        break
    DEVS = _DEVS.json()
    break

del _DEVS

SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
BL_CHAT = {int(x) for x in os.environ.get("BL_CHAT", "").split()}
BLACKLIST_GCAST = {
    int(x) for x in os.environ.get(
        "BLACKLIST_GCAST",
        "").split()}

# For Blacklist Group Support
BLACKLIST_CHAT = os.environ.get("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283, -1001675396283, -1001608701614,
                     -1001726206158, -1001287188817, -1001638078842,
                     -1001692751821, -1001459812644, -1001812143750, -1001599474353, -1001876092598, -1001861414061]

# Telegram App KEY and HASH
API_KEY = int(os.environ.get("API_KEY") or 0)
API_HASH = str(os.environ.get("API_HASH") or None)

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", "0"))

# Load or No Load modules
LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "").split()

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "True"))
PM_LIMIT = int(os.environ.get("PM_LIMIT", 6))

# Custom Handler command
CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."
SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"$")

# Support
GROUP = os.environ.get("GROUP", "roemahjasebsupport")
CHANNEL = os.environ.get("CHANNEL", "roemahjaseb")

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# JustWatch Country
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get("UPSTREAM_REPO_URL", "https://github.com/roemahjaseb/Kazu-Userbot.git")

# Custom Name Sticker Pack
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", "jK9nGhjQPtd2Y5RhwMwB5EMA")

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get(
    "GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", "Jakarta")

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# untuk perintah teks costum .alive
ALIVE_TEKS_CUSTOM = os.environ.get(
    "ALIVE_TEKS_CUSTOM",
    "im alive, what's your command?")

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", "Roemahjaseb-Userbot")

# Custom Emoji Alive
ALIVE_EMOJI = os.environ.get("ALIVE_EMOJI", "✨")

# Custom Emoji Alive
INLINE_EMOJI = os.environ.get("INLINE_EMOJI", "✨")

# Custom icon HELP
ICON_HELP = os.environ.get("ICON_HELP", "✨")

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Zipfile module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# bit.ly module
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)

# Bot version
BOT_VER = os.environ.get("BOT_VER", "3.6.9")

# Default .alive logo
ALIVE_LOGO = (os.environ.get("ALIVE_LOGO")
              or "https://vault.pictures/p/1e4ef6b4327a40c5b4657153a406a012")

INLINE_PIC = (os.environ.get("INLINE_PIC")
              or "https://vault.pictures/p/2bbbdcf75e0243349d7d72a735933657")

# Picture For VCPLUGIN
PLAY_PIC = (os.environ.get("PLAY_PIC")
            or ".png")

QUEUE_PIC = (os.environ.get("QUEUE_PIC")
             or "https://vault.pictures/p/2bbbdcf75e0243349d7d72a735933657")

DEFAULT = list(map(int, b64decode("NjAzNzM2NDQwNA==").split()))

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
lastfm = None
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    try:
        lastfm = LastFMNetwork(
            api_key=LASTFM_API,
            api_secret=LASTFM_SECRET,
            username=LASTFM_USERNAME,
            password_hash=LASTFM_PASS,
        )
    except BaseException:
        pass

TEMP_DOWNLOAD_DIRECTORY = os.environ.get(
    "TMP_DOWNLOAD_DIRECTORY", "./downloads/")

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# NSFW Detect DEEP AI
DEEP_AI = os.environ.get("DEEP_AI", None)

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)

# Jangan di hapus Nanti ERROR
while 0 < 6:
    _BLACKLIST = get(
        "https://raw.githubusercontent.com/roemahjaseb/roemahjase/Kazu-Userbot/app.json"
    )
    if _BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        blacklistayiin = []
        break
    blacklistayiin = _BLACKLIST.json()
    break

del _BLACKLIST

ch = str(b64decode("QGJsdWVmbG95ZGQ="))[2:15]
gc = str(b64decode("QGJsdWV0c3N0"))[2:17]

while 0 < 6:
    _WHITELIST = get(
        "https://raw.githubusercontent.com/roemahjaseb/roemahjase/Kazu-Userbot/app.json"
    )
    if _WHITELIST.status_code != 200:
        if 0 != 5:
            continue
        WHITELIST = []
        break
    WHITELIST = _WHITELIST.json()
    break

del _WHITELIST

# 'bot' variable
if STRING_SESSION:
    session = StringSession(str(STRING_SESSION))
else:
    session = "𝗥𝗼𝗲𝗺𝗮𝗵𝗷𝗮𝘀𝗲𝗯-Userbot"
try:
    bot = TelegramClient(
        session=session,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()



if BOT_TOKEN is not None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=BOT_TOKEN)
else:
    tgbot = None


async def update_restart_msg(chat_id, msg_id):
    message = (
        f"**𝗥𝗼𝗲𝗺𝗮𝗵𝗷𝗮𝘀𝗲𝗯-Userbot v`{BOT_VER}` is back up and running!**\n\n"
        f"**Telethon:** `{vsc}`\n"
        f"**Python:** `{python_version()}`\n"
    )
    await bot.edit_message(chat_id, msg_id, message)
    return True


try:
    from AyiinXd.modules.sql_helper.globals import delgvar, gvarstatus

    chat_id, msg_id = gvarstatus("restartstatus").split("\n")
    with bot:
        try:
            LOOP.run_until_complete(
                update_restart_msg(
                    int(chat_id), int(msg_id)))
        except BaseException:
            pass
    delgvar("restartstatus")
except AttributeError:
    pass


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 6
    number_of_cols = 2
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            f"{INLINE_EMOJI} {x} {INLINE_EMOJI}", data=f"ub_modul_{x}"
        )
        for x in helpable_modules
    ]
    pairs = list(
        zip(
            modules[::number_of_cols],
            modules[1::number_of_cols],
        )
    )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⪻", data=f"{prefix}_prev({modulo_page})"
                ),
                custom.Button.inline(
                    "⪼ ʙᴀᴄᴋ ⪻", data=f"{prefix}_close({modulo_page})"
                ),
                custom.Button.inline(
                    "⪼", data=f"{prefix}_next({modulo_page})"
                ),
            )
        ]
    return pairs


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


with bot:
    try:
        import os
        import random

        from AyiinXd.modules.sql_helper.bot_blacklists import check_is_black_list
        from AyiinXd.modules.sql_helper.bot_pms_sql import add_user_to_db, get_user_id
        from AyiinXd.modules.sql_helper.globals import addgvar, delgvar, gvarstatus
        from AyiinXd.ayiin import AyiinDB, HOSTED_ON, reply_id
        from Stringyins import get_languages, get_string, language

        adB = AyiinDB()
        dugmeler = CMD_HELP
        user = bot.get_me()
        uid = user.id
        owner = user.first_name
        asst = tgbot.get_me()
        botusername = asst.username
        logo = ALIVE_LOGO
        logoyins = random.choice(
                [
                    "https://vault.pictures/p/2bbbdcf75e0243349d7d72a735933657",
                    "https://vault.pictures/p/2bbbdcf75e0243349d7d72a735933657",
                ]
        )
        cmd = CMD_HANDLER
        tgbotusername = BOT_USERNAME
        BTN_URL_REGEX = re.compile(
            r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)"
        )

        main_help_button = [
            [
                Button.inline(get_string("help_3"), data="konten_yins"),
                Button.inline(get_string("help_4"), data="inline_yins"),
            ],
            [
                Button.inline(get_string("help_2"), data="reopen"),
            ],
            [
                Button.inline(get_string("help_6"), data="yins_langs"),
                Button.url(get_string("help_7"), url=f"t.me/{botusername}?start="),
            ],
            [Button.inline(get_string("help_8"), data="close")],
        ]

        @tgbot.on(events.NewMessage(incoming=True,
                  func=lambda e: e.is_private))
        async def bot_pms(event):
            chat = await event.get_chat()
            if check_is_black_list(chat.id):
                return
            if chat.id != uid:
                msg = await event.forward_to(uid)
                try:
                    add_user_to_db(
                        msg.id, get_display_name(chat), chat.id, event.id, 0, 0
                    )
                except Exception as e:
                    LOGS.error(str(e))
                    if BOTLOG:
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            f"**ERROR:** Saat menyimpan detail pesan di database\n`{str(e)}`",
                        )
            else:
                if event.text.startswith("/"):
                    return
                reply_to = await reply_id(event)
                if reply_to is None:
                    return
                users = get_user_id(reply_to)
                if users is None:
                    return
                for usr in users:
                    user_id = int(usr.chat_id)
                    reply_msg = usr.reply_id
                    user_name = usr.first_name
                    break
                if user_id is not None:
                    try:
                        if event.media:
                            msg = await event.client.send_file(
                                user_id,
                                event.media,
                                caption=event.text,
                                reply_to=reply_msg,
                            )
                        else:
                            msg = await event.client.send_message(
                                user_id,
                                event.text,
                                reply_to=reply_msg,
                                link_preview=False,
                            )
                    except UserIsBlockedError:
                        return await event.reply(
                            "❌ **Bot ini diblokir oleh pengguna.**"
                        )
                    except Exception as e:
                        return await event.reply(f"**ERROR:** `{e}`")
                    try:
                        add_user_to_db(
                            reply_to,
                            user_name,
                            user_id,
                            reply_msg,
                            event.id,
                            msg.id)
                    except Exception as e:
                        LOGS.error(str(e))
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                f"**ERROR:** Saat menyimpan detail pesan di database\n`{e}`",
                            )
                            
        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(rb"reopen")))
        async def on_plug_in_callback_query_handler(event):
            try:
        # Ambil ID pesan dari event.query jika event.message tidak ada
                message_id = event.query.message_id
                chat_id = event.chat_id

        # Ambil pesan asli menggunakan client.get_messages
                message = await event.client.get_messages(chat_id, ids=message_id)

        # Debugging log untuk memeriksa apakah pesan berhasil ditemukan
                print(f"Pesan ditemukan: {message.text}")

        # Buat tombol dan teks untuk menu
                buttons = paginate_help(0, dugmeler, "helpme")
                text = (
                    f"**𝗥𝗼𝗲𝗺𝗮𝗵𝗷𝗮𝘀𝗲𝗯-Userbot Menu**\n\n"
                    f"**Based on:** {adB.name}\n"
                    f"**Deploy on:** •[{HOSTED_ON}]•\n"
                    f"**Owner:** {owner}\n"
                    f"**Jumlah:** {len(dugmeler)} **Modules**"
        )

        # Edit pesan dengan tombol
                await message.edit(
                    text,
                    file=logoyins,
                    buttons=buttons,
                    link_preview=False,
                )
            except Exception as e:
        # Tampilkan error jika pesan tidak ditemukan atau ada kesalahan lain
                print(f"Error saat mengambil atau mengedit pesan: {e}")
                await event.answer(
                    "Pesan asli tidak ditemukan atau telah dihapus.",
                    alert=True,
                )
        
        @tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith(
                    "@AyiinXdSupport"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = await event.builder.photo(
                    file=logoyins,
                    link_preview=False,
                    text=f"**𝗥𝗼𝗲𝗺𝗮𝗵𝗷𝗮𝘀𝗲𝗯-Userbot**\n\n Bases on :** {adB.name}\n Deploy on :** •[{HOSTED_ON}]•\n Owner :** {user.first_name}\n Jumlah :** {len(dugmeler)} **Modules**",
                    buttons=main_help_button,
                )
            elif query.startswith("repo"):
                result = builder.article(
                    title="Repository",
                    description="Repository 𝙺𝙰𝚉𝚄-𝚄𝚂𝙴𝚁𝙱𝙾𝚃",
                    url="https://t.me/kazusupportgrp",
                    thumb=InputWebDocument(
                        INLINE_PIC,
                        0,
                        "image/jpeg",
                        []),
                    text="**𝗥𝗼𝗲𝗺𝗮𝗵𝗷𝗮𝘀𝗲𝗯-Userbot\n✧  **ʀᴇᴘᴏ :** [𝙺𝙰𝚉𝚄 𝚄𝚂𝙴𝚁𝙱𝙾𝚃](https://t.me/disinikazu)\n✧ **sᴜᴘᴘᴏʀᴛ :** @kazusupportgrp\n✧ **ʀᴇᴘᴏsɪᴛᴏʀʏ :** [KazuUBot](https://github.com/ionmusic/Kazu-Userbot)\n➖➖➖➖➖➖➖➖➖➖",
                    buttons=[
                        [
                            custom.Button.url(
                                "ɢʀᴏᴜᴘ",
                                "https://t.me/kazusupportgrp"),
                            custom.Button.url(
                                "ʀᴇᴘᴏ",
                                "https://github.com/ionmusic/Kazu-Userbot"),
                        ],
                    ],
                    link_preview=False,
                )
            elif query.startswith("string"):
                result = builder.article(
                    title="String",
                    description="String 𝙺𝙰𝚉𝚄 𝚄𝚂𝙴𝚁𝙱𝙾𝚃",
                    url="https://t.me/kazusupportgrp",
                    thumb=InputWebDocument(
                        logoyins,
                        0,
                        "image/jpeg",
                        []),
                    text=get_string("lang_4"),
                    buttons=[
                        [
                            custom.Button.url(
                                "Bᴏᴛ Sᴛʀɪɴɢ",
                                url="https://t.me/kazu_stringbot?start="),
                            custom.Button.url(
                                "Sᴛʀɪɴɢ Rᴇᴘʟɪᴛ",
                                url="https://repl.it/@AyiinXd/AyiinString?lite=1&outputonly=1"),
                        ],
                        [
                            custom.Button.url("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/kazusupportgrp"),
                        ],
                    ],
                    link_preview=False,
                )
            elif query.startswith("lang"):
                languages = get_languages()
                text = "List Of Available Languages.",
                tutud = [
                    Button.inline(
                        f"{languages[yins]['asli']} [{yins.lower()}]",
                        data=f"set_{yins}",
                    )
                    for yins in languages
                ]
                buttons = list(zip(tutud[::2], tutud[1::2]))
                if len(tutud) % 2 == 1:
                    buttons.append((tutud[-1],))
                buttons.append([custom.Button.inline("ʙᴀᴄᴋ", data="yins_close")])
                result = builder.article(
                    title="roemahjaseb",
                    description="𝗥𝗢𝗘𝗠𝗔𝗛𝗝𝗔𝗦𝗘𝗕-Userbot",
                    url="https://t.me/kazusupportgrp",
                    thumb=InputWebDocument(
                        logoyins,
                        0,
                        "image/jpeg",
                        []),
                    text=get_string("lang_1"),
                    buttons=buttons,
                    link_preview=False,
                )
            elif query.startswith("Inline buttons"):
                markdown_note = query[14:]
                prev = 0
                note_data = ""
                buttons = []
                for match in BTN_URL_REGEX.finditer(markdown_note):
                    n_escapes = 0
                    to_check = match.start(1) - 1
                    while to_check > 0 and markdown_note[to_check] == "\\":
                        n_escapes += 1
                        to_check -= 1
                    if n_escapes % 2 == 0:
                        buttons.append(
                            (match.group(2), match.group(3), bool(
                                match.group(4))))
                        note_data += markdown_note[prev: match.start(1)]
                        prev = match.end(1)
                    elif n_escapes % 2 == 1:
                        note_data += markdown_note[prev:to_check]
                        prev = match.start(1) - 1
                    else:
                        break
                else:
                    note_data += markdown_note[prev:]
                message_text = note_data.strip()
                tl_ib_buttons = ibuild_keyboard(buttons)
                result = builder.article(
                    title="Inline creator",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="whats?",
                    description="𝗥𝗼𝗲𝗺𝗮𝗵𝗷𝗮𝘀𝗲𝗯-Userbot",
                    url="https://t.me/hatisemu",
                    thumb=InputWebDocument(
                        INLINE_PIC,
                        0,
                        "image/jpeg",
                        []),
                    text=f"残酷 ──I. 𝗥𝗼𝗲𝗺𝗮𝗵𝗷𝗮𝘀𝗲𝗯.",
                    buttons=[
                        [
                            custom.Button.url(
                                "Old Testie",
                                "https://t.me/roemahjaseb"),
                            custom.Button.url(
                                "Deploy Ubot",
                                "https://github.com/roemahjaseb/Kazu-Userbot/tree/Kazu-Userbot"),
                        ],
                    ],
                    link_preview=False,
                )
            await event.answer(
                [result], switch_pm="👥 USERBOT PORTAL", switch_pm_param="start"
            )

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = (
                    f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                )
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:  # @Kyy-Userbot
                # https://t.me/TelethonChat/115200
                await event.edit(
                    file=logoyins,
                    link_preview=True,
                    buttons=main_help_button)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"gcback")
            )
        )
        async def gback_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:  # @iamuput-Userbot
                # https://t.me/TelethonChat/115200
                text = (
                    f"**𝗕𝗟𝗨𝗘𝗙𝗟𝗢𝗬𝗗-Userbot Menu**\n\n✧ **ᴏᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id})\n✧ **ᴊᴜᴍʟᴀʜ :** {len(dugmeler)} **Modules**")
                await event.edit(
                    text,
                    file=logoyins,
                    link_preview=True,
                    buttons=main_help_button)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"set_(.*)")
            )
        )
        async def langs(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                lang = event.data_match.group(1).decode("UTF-8")
                language[0] = lang
                if not gvarstatus("lang"):
                    delgvar(language[0])
                    languages = get_languages()
                if languages:
                    try:
                        addgvar("language", lang)
                        await event.edit(
                            get_string("lang_2").format(
                                languages[lang]['asli'], lang),
                            file=logoyins,
                            link_preview=True,
                            buttons=[Button.inline("ʙᴀᴄᴋ", data="yins_close")]
                        )
                    except Exception:
                        pass

            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.CallbackQuery(data=b"inline_yins"))
        async def about(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                await event.edit(f"""
•Menu• - Voice chat group untuk [{user.first_name}](tg://user?id={user.id})
""",
                                 buttons=[
                                     [
                                         Button.inline("⍟ ᴠᴄ ᴘʟᴜɢɪɴ ⍟",
                                                       data="vcplugin"),
                                         Button.inline("⍟ ᴠᴄ ᴛᴏᴏʟs ⍟",
                                                       data="vctools")],
                                     [custom.Button.inline(
                                         "ʙᴀᴄᴋ", data="gcback")],
                                 ]
                                 )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"vcplugin")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                text = (
                    f"""
✘ **Perintah yang tersedia di vcplugin** ✘

  »  **Perintah : **`{cmd}play` <Judul Lagu/Link YT>
  »  **Kegunaan :** __Untuk Memutar Lagu di voice chat group dengan akun kamu.__

  »  **Perintah : **`{cmd}vplay` <Judul Video/Link YT>
  »  **Kegunaan :** __Untuk Memutar Video di voice chat group dengan akun kamu.__

  »  **Perintah : **`{cmd}end`
  »  **Kegunaan :** __Untuk Memberhentikan video/lagu yang sedang putar di voice chat group.__

  »  **Perintah : **`{cmd}skip`
  »  **Kegunaan :** __Untuk Melewati video/lagu yang sedang di putar.__

  »  **Perintah : **`{cmd}pause`
  »  **Kegunaan :** __Untuk memberhentikan video/lagu yang sedang diputar.__

  »  **Perintah : **`{cmd}resume`
  »  **Kegunaan :** __Untuk melanjutkan pemutaran video/lagu yang sedang diputar.__

  »  **Perintah : **`{cmd}volume` 1-200
  »  **Kegunaan :** __Untuk mengubah volume (Membutuhkan Hak admin).__

  »  **Perintah : **`{cmd}playlist`
  »  **Kegunaan :** __Untuk menampilkan daftar putar Lagu/Video.__
""")
                await event.edit(
                    text,
                    file=logoyins,
                    link_preview=True,
                    buttons=[Button.inline("ʙᴀᴄᴋ", data="inline_yins")])
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"vctools")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                text = (
                    f"""
✘ **Perintah yang tersedia di vctools** ✘

  »  **Perintah : **`{cmd}startvc`
  »  **Kegunaan :** __Untuk Memulai voice chat group.__

  »  **Perintah : **`{cmd}stopvc`
  »  **Kegunaan :** __Untuk Memberhentikan voice chat group.__

  »  **Perintah :** `{cmd}joinvc` atau `{cmd}joinvc` <chatid/username gc>
  »  **Kegunaan :** __Untuk Bergabung ke voice chat group.__

  »  **Perintah : **`{cmd}leavevc` atau `{cmd}leavevc` <chatid/username gc>
  »  **Kegunaan :** __Untuk Turun dari voice chat group.__

  »  **Perintah : **`{cmd}vctitle` <title vcg>
  »  **Kegunaan :** __Untuk Mengubah title/judul voice chat group.__

  »  **Perintah : **`{cmd}vcinvite`
  »  **Kegunaan :** __Mengundang Member group ke voice chat group.__
""")
                await event.edit(
                    text,
                    file=logoyins,
                    link_preview=True,
                    buttons=[Button.inline("ʙᴀᴄᴋ", data="inline_yins")])
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.CallbackQuery(data=b"konten_yins"))
        async def about(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                await event.edit(f"""
•Menu• - Konten Channel untuk [{user.first_name}](tg://user?id={user.id})
""",
                                 buttons=[
                                     [
                                         Button.inline("⍟ ʙᴛᴘᴍ ⍟",
                                                       data="btpmayiin"),
                                         Button.inline("⍟ ʏɪɴs ʙᴏᴋᴇᴘ ⍟",
                                                       data="yinsbokep")],
                                     [custom.Button.inline(
                                         "ʙᴀᴄᴋ", data="gcback")],
                                 ]
                                 )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"btpmayiin")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                text = (
                    f"""
✘ **Perintah Yang Tersedia Di btpm** ✘

  »  **Perintah : **`{cmd}btpm` <username ch>
  »  **Kegunaan :** __Untuk Mendapatkan List Btpm Kosong.__

  »  **Perintah : **`{cmd}savebt` <nama_list>
  »  **Kegunaan :** __Untuk Menyimpan List Btpm, Gunakan Nama Yang Berbeda.__

  »  **Perintah : **$<nama_list>
  »  **Kegunaan :** __Untuk Mendapatkan List Btpm Yang Tersimpan.__

  »  **Perintah : **`{cmd}delbt` <nama_list>
  »  **Kegunaan :** __Menghapus List Btpm Yang Tersimpan.__

  »  **Perintah : **`{cmd}listbt` <nama_list>
  »  **Kegunaan :** __Untuk Menlihat Semua List Btpm Yang Tersimpan.__
""")
                await event.edit(
                    text,
                    file=logoyins,
                    link_preview=True,
                    buttons=[Button.inline("ʙᴀᴄᴋ", data="konten_yins")])
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"yinsbokep")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                text = (
                    f"""
✘ **Perintah yang tersedia di yins bokep** ✘

  »  **Perintah : **`{cmd}bokp`
  »  **Kegunaan :** __Untuk Mengirim bokp secara random.__
""")
                await event.edit(
                    text,
                    file=logoyins,
                    link_preview=True,
                    buttons=[Button.inline("ʙᴀᴄᴋ", data="konten_yins")])
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"yins_langs")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                text = (
                    f"""
✘ **Perintah yang tersedia di tools** ✘

  »  **Perintah :** `{cmd}lang`
  »  **Kegunaan : **Untuk Mengubah Bahasa.

  »  **Perintah :** `{cmd}string`
  »  **Kegunaan : **Untuk Membuat String Session.
""")
                await event.edit(
                    text,
                    file=logoyins,
                    link_preview=True,
                    buttons=[Button.inline("ʙᴀᴄᴋ", data="gcback")])
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.CallbackQuery(data=b"close"))
        async def close(event):
            buttons = [
                (custom.Button.inline("ᴍᴀɪɴ ᴍᴇɴᴜ", data="gcback"),),
            ]
            await event.edit("**ᴍᴇɴᴜ ᴅɪᴛᴜᴛᴜᴘ**", file=logoyins, buttons=buttons)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"yins_close")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                await event.edit(get_string("lang_3"), file=logoyins)

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ub_modul_(.*)")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 950:
                    help_string = (
                        str(CMD_HELP[modul_name])
                        .replace("`", "")
                        .replace("**", "")[:950]
                        + "..."
                        + f"\n\nBaca Teks Berikutnya Ketik {cmd}help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = (str(CMD_HELP[modul_name]).replace(
                        "`", "").replace("**", ""))

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else f"{modul_name} Tidak ada dokumen yang telah ditulis untuk modul."
                )
                await event.edit(
                    reply_pop_up_alert, buttons=[
                        Button.inline("ʙᴀᴄᴋ", data="reopen")]
                )

            else:
                reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {owner}"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            f"Jika mengalami error saat pemasangan silahkan klik save dipojok kanan bawah logs lalu hubungi @hatisemu atau ke @roemahjasebsupport. 𝗥𝗼𝗲𝗺𝗮𝗵𝗷𝗮𝘀𝗲𝗯-Userbot {BOT_VER}")
