# Copyright (C) 2019 The Raphielscape Company LLC.
# Licensed under the Raphielscape Public License, Version 1.c
# Copyright (C) 2021 TeamUltroid for autobot
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

""" Userbot start point """

import sys
import asyncio
from importlib import import_module
from platform import python_version

from pytgcalls import __version__ as pytgcalls
from telethon import version
from telethon.tl.alltlobjects import LAYER

from AyiinXd.ayiin.events import ajg
from AyiinXd import BOT_TOKEN, BOTLOG_CHATID, LOGS, bot
from AyiinXd.clients import ayiin_userbot_on, multiayiin
from AyiinXd.core.git import git
from AyiinXd.modules import ALL_MODULES
from AyiinXd.ayiin import AyiinDB, HOSTED_ON, autobot, autopilot, ayiin_version

async def start_bot():
    try:
        # Import semua module userbot
        for module_name in ALL_MODULES:
            import_module(f"AyiinXd.modules.{module_name}")

        # Cek database dan jalankan multi-client
        adB = AyiinDB()
        client = multiayiin()
        
        # Cek versi & git update
        git()
        LOGS.info(f"Python Version: {python_version()}")
        LOGS.info(f"Telethon Version: {version.__version__} [Layer: {LAYER}]")
        LOGS.info(f"PyTgCalls Version: {pytgcalls}")
        LOGS.info(f"Userbot Version: {ayiin_version} [{HOSTED_ON}]")
        LOGS.info(f"Userbot Name: {adB.name}")
        LOGS.info("✨ Userbot berhasil diaktifkan! ✨")

        # Jalankan userbot
        await ayiin_userbot_on()
        await ajg()
        
        # Jalankan fitur autobot/autopilot jika diperlukan
        if not BOTLOG_CHATID:
            await autopilot()
        if not BOT_TOKEN:
            await autobot()

        # Menjaga bot tetap berjalan
        await bot.run_until_disconnected()

    except Exception as e:
        LOGS.error(f"Terjadi kesalahan: {e}", exc_info=True)
        sys.exit(1)

# Menjalankan bot dengan asyncio
if __name__ == "__main__":
    asyncio.run(start_bot())
