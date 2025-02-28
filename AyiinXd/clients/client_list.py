# RoemahJaseb Gacor. #
from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    return user_ids


JASEB_OWNER = list(map(int, b64decode("MjAxNDk5ODAzOA==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        AYIIN_USER = uid.user.first_name  # Tetap pakai AYIIN_USER
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        AYIIN_USER = client.first_name  # Tetap pakai AYIIN_USER
    jaseb_mention = f"[{AYIIN_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, AYIIN_USER, ayiin_mention
