import asyncio

from random import choice

from telethon import events
from pyrogram import enums

from config import X1, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from SHUKLASPAM.data import PRAID

PREPLY_RAID = []


@X1.on(events.NewMessage(incoming=True, pattern=r"\%spraid(?: |$)(.*)" % hl))
async def praid(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in SHASHANK:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ✨🥀")
            elif uid == OWNER_ID:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ🥀")
            elif uid in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ✨")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(PRAID)
                    caption = f"❖ {username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝐏𝐫𝐚𝐢𝐝 ➥ {hl}praid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}praid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True))
async def _(event):
    global PREPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in PREPLY_RAID:
        await asyncio.sleep(0.1)
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(choice(PRAID)),
            reply_to=event.message.id,
        )


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sprraid(?: |$)(.*)" % hl))
async def hrraid(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in SHASHANK:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ✨🥀")
            elif user_id == OWNER_ID:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ🥀")
            elif user_id in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ✨")
            else:
                global PREPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in PREPLY_RAID:
                    PREPLY_RAID.append(check)
                await e.reply("✦ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʜɪɴᴅɪ ʀᴇᴘʟʏʀᴀɪᴅ ✅")
        except NameError:
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝐏𝐛𝐢 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝 ➥ {hl}hrraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}hrraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sdpraid(?: |$)(.*)" % hl))
async def dpraid(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global PREPLY_RAID
            if check in PREPLY_RAID:
                PREPLY_RAID.remove(check)
            await e.reply("✦ ʜɪɴᴅɪ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")
        except NameError:
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝐃𝐏𝐛𝐢 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝 ➥ {hl}dpraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}dpraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

        except Exception as e:
            print(e)
