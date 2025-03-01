# repack by blue. #

""" Userbot module for System Stats commands """

import asyncio
import platform
import sys
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version
from shutil import which

import psutil
from pytgcalls import __version__ as pytgcallss
from telethon import __version__, version

from AyiinXd import ALIVE_EMOJI, ALIVE_LOGO, ALIVE_TEKS_CUSTOM, BOT_VER, CHANNEL
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, GROUP, StartTime
from AyiinXd.ayiin import __version__ as py_ver
from AyiinXd.ayiin import (
    AyiinDB,
    HOSTED_ON,
    ayiin_version,
    bash,
    edit_or_reply,
    ayiin_cmd,
)


from .ping import get_readable_time

try:
    from carbonnow import Carbon
except ImportError:
    Carbon = None

modules = CMD_HELP
emoji = ALIVE_EMOJI
alive_text = ALIVE_TEKS_CUSTOM


@ayiin_cmd(
    pattern="sysinfo$",
)
async def _(e):
    xxnx = await edit_or_reply(e, "`Processing...`")
    x, y = await bash("neofetch|sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g' >> neo.txt")
    with open("neo.txt", "r") as neo:
        p = (neo.read()).replace("\n\n", "")
    ok = Carbon(base_url="https://carbonara.vercel.app/api/cook", code=p)
    haa = await ok.memorize("neofetch")
    await e.reply(file=haa)
    await xxnx.delete()
    remove("neo.txt")


@ayiin_cmd(pattern=r"spc")
async def psu(event):
    uname = platform.uname()
    softw = "**Iɴғᴏʀᴍᴀsɪ Sɪsᴛᴇᴍ**\n"
    softw += f"**Sɪsᴛᴇᴍ   :** `{uname.system}`\n"
    softw += f"**Rɪʟɪs    :** `{uname.release}`\n"
    softw += f"**Vᴇʀsɪ    :** `{uname.version}`\n"
    softw += f"**Mᴇsɪɴ    :** `{uname.machine}`\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"**Wᴀᴋᴛᴜ Hɪᴅᴜᴘ:** `{bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}`\n"
    # CPU Cores
    cpuu = "**Iɴғᴏʀᴍᴀsɪ CPU**\n"
    cpuu += "**Pʜʏsɪᴄᴀʟ Cᴏʀᴇs   :** `" + \
        str(psutil.cpu_count(logical=False)) + "`\n"
    cpuu += "**Tᴏᴛᴀʟ Cᴏʀᴇs      :** `" + \
        str(psutil.cpu_count(logical=True)) + "`\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"**Mᴀx Fʀᴇǫᴜᴇɴᴄʏ    :** `{cpufreq.max:.2f}Mhz`\n"
    cpuu += f"**Mɪɴ Fʀᴇǫᴜᴇɴᴄʏ    :** `{cpufreq.min:.2f}Mhz`\n"
    cpuu += f"**Cᴜʀʀᴇɴᴛ Fʀᴇǫᴜᴇɴᴄʏ:** `{cpufreq.current:.2f}Mhz`\n\n"
    # CPU usage
    cpuu += "**CPU Usᴀɢᴇ Pᴇʀ Cᴏʀᴇ**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"**Cᴏʀᴇ {i}  :** `{percentage}%`\n"
    cpuu += "**Tᴏᴛᴀʟ CPU Usᴀɢᴇ**\n"
    cpuu += f"**Sᴇᴍᴜᴀ Cᴏʀᴇ:** `{psutil.cpu_percent()}%`\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "**Mᴇᴍᴏʀʏ Dɪɢᴜɴᴀᴋᴀɴ**\n"
    memm += f"**Tᴏᴛᴀʟ     :** `{get_size(svmem.total)}`\n"
    memm += f"**Aᴠᴀɪʟᴀʙʟᴇ :** `{get_size(svmem.available)}`\n"
    memm += f"**Usᴇᴅ      :** `{get_size(svmem.used)}`\n"
    memm += f"**Pᴇʀᴄᴇɴᴛᴀɢᴇ:** `{svmem.percent}%`\n"
    # Bandwidth Usage
    bw = "**Bᴀɴᴅᴡɪᴛʜ Dɪɢᴜɴᴀᴋᴀɴ**\n"
    bw += f"**Uɴɢɢᴀʜ  :** `{get_size(psutil.net_io_counters().bytes_sent)}`\n"
    bw += f"**Dᴏᴡɴʟᴏᴀᴅ:** `{get_size(psutil.net_io_counters().bytes_recv)}`\n"
    help_string = f"{softw}\n"
    help_string += f"{cpuu}\n"
    help_string += f"{memm}\n"
    help_string += f"{bw}\n"
    help_string += "**Iɴғᴏʀᴍᴀsɪ Mᴇsɪɴ**\n"
    help_string += f"**Pʏᴛʜᴏɴ :** `{sys.version}`\n"
    help_string += f"**Tᴇʟᴇᴛʜᴏɴ :**`{__version__}`\n"
    help_string += f"**Pʏ-ʙʟᴜᴇ :** `{py_ver}`\n"
    help_string += f"**ʙʟᴜᴇ ᴠᴇʀsɪᴏɴ :** `{ayiin_version} [{HOSTED_ON}]`"
    await edit_or_reply(event, help_string)


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


@ayiin_cmd(pattern="sysd$")
async def sysdetails(sysd):
    if not sysd.text[0].isalpha() and sysd.text[0] not in ("/", "#", "@", "!"):
        try:
            fetch = await asyncrunapp(
                "neofetch",
                "--stdout",
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) + \
                str(stderr.decode().strip())

            await edit_or_reply(sysd, "`" + result + "`")
        except FileNotFoundError:
            await edit_or_reply(sysd, "**Install neofetch Terlebih dahulu!!**")


@ayiin_cmd(pattern="botver$")
async def bot_ver(event):
    if event.text[0].isalpha() or event.text[0] in ("/", "#", "@", "!"):
        return
    if which("git") is not None:
        ver = await asyncrunapp(
            "git",
            "describe",
            "--all",
            "--long",
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        rev = await asyncrunapp(
            "git",
            "rev-list",
            "--all",
            "--count",
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await rev.communicate()
        revout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        await edit_or_reply(
            event,
            "✧ **Userbot Versi :** " f"`{verout}`" "\n✧ **Revisi :** " f"`{revout}`",
        )
    else:
        await edit_or_reply(
            event, "anda tidak memiliki git, Anda Menjalankan Bot - 'v1.beta.4'!"
        )


@ayiin_cmd(pattern="(?:alive|yinson)\\s?(.)?")
async def amireallyalive(alive):
    adB = AyiinDB()
    user = await alive.client.get_me()
    uptime = await get_readable_time((time.time() - StartTime))
    await alive.edit("👨‍❤️‍👨")
    await asyncio.sleep(3)
    output = (
        f"**here is [𝗥𝗢𝗘𝗠𝗔𝗛𝗝𝗔𝗦𝗘𝗕-userbot](t.me/roemahjaseb)**\n\n"
        f"**{alive_text}**\n\n"
        f"━━━━━━━━━━━━━━\n"
        f"** - Bᴀsᴇ Oɴ :** ••{adB.name}••\n"
        f"** - Oᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id}) \n"
        f"** - Mᴏᴅᴜʟᴇs :** `{len(modules)} Modules` \n"
        f"** - Bᴏᴛ Vᴇʀsɪᴏɴ :** `{BOT_VER}` \n"
        f"** - Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{python_version()}` \n"
        f"** - PʏTɢCᴀʟʟs Vᴇʀsɪᴏɴ :** `{pytgcallss}` \n"
        f"** - Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{version.__version__}` \n"
        f"** - Pʏ-ʙʟᴜᴇ ᴠᴇʀsɪᴏɴ :** `{py_ver}`\n"
        f"** - roemahjaseb ᴠᴇʀsɪᴏɴ :** `{ayiin_version}` [{HOSTED_ON}]\n"
        f"** - Bᴏᴛ Uᴘᴛɪᴍᴇ :** `{uptime}`\n"
        "━━━━━━━━━━━━━━━\n\n"
    )
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await alive.client.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(800)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n ***Logo yang diberikan tidak valid."
                "\nPastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await edit_or_reply(alive, output)


CMD_HELP.update(
    {
        "system": f"**Plugin : **`system`.\
        \n\n  »  **Perintah :** `{cmd}sysinfo`\
        \n  »  **Kegunaan : **Informasi sistem menggunakan neofetch mengirim sebagai gambar.\
        \n\n  »  **Perintah :** `{cmd}sysd`\
        \n  »  **Kegunaan : **Informasi sistem menggunakan neofetch.\
        \n\n\n  »  **Perintah :** `{cmd}botver`\
        \n  »  **Kegunaan : **Menampilkan versi userbot.\
        \n\n  »  **Perintah :** `{cmd}spc`\
        \n  »  **Kegunaan : **Menampilkan spesifikasi sistem secara lengkap.\
    "
    }
)


CMD_HELP.update(
    {
        "alive": f"**Plugin : **`alive`\
        \n\n  »  **Perintah :** `{cmd}alive` atau `{cmd}kazu`\
        \n  »  **Kegunaan : **Untuk melihat apakah bot Anda berfungsi atau tidak.\
    "
    }
    )
