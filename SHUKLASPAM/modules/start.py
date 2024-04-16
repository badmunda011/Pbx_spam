
from telethon import __version__, events, Button

from config import X1


START_BUTTON = [
    [
        Button.url("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", "https://t.me/avishaxbot?startgroup=true")
    ],
    [
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/ll_THE_BAD_BOT_ll"),
        Button.url("ʀᴇᴘᴏ", "https://github.com/Badhacker98/BAD_SPAM_X/fork")
    ],
    [
        Button.inline("ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs", data="help_back")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n❍ 𝗛𝗘𝗬 ‣ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n❍ 𝗜 𝗔𝗠 ‣ [{bot_name}](tg://user?id={bot_id})\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n● ɪ ᴀᴍ ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟ sᴘᴀᴍ ʙᴏᴛ ●\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n⊚ ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴀɪᴅ\n⊚ ᴜɴʟɪᴍɪᴛᴇᴅ sᴘᴀᴍ \n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n⦿ 24x7 ʀᴜɴ|[sᴛʀᴀɴɢᴇʀ](https://t.me/FIGHTERS1234)\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•**"
        await event.client.send_file(
            event.chat_id,
            "https://telegra.ph/file/05522e13c97752efe5e75.png",
            caption=TEXT,
            buttons=START_BUTTON
        )
