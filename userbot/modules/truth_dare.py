# Ported by Fariz (Flicks-Userbot)
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.truth(?: |$)(.*)")
async def _(event):
    await event.edit("Mengirim pesan truth...")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1335899453)
            )
            await conv.send_message("/truth")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("Harap unblock `@truthordares_bot` dan coba lagi")
            return
        await event.edit(f"**Pesan truth**\n\n{response.message.message}")


@register(outgoing=True, pattern=r"^\.dare(?: |$)(.*)")
async def _(event):
    await event.edit("Mengirim pesan dare...")
    async with bot.conversation("@truthordares_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1335899453)
            )
            await conv.send_message("/dare")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("Harap unblock `@truthordares_bot` dan coba lagi")
            return
        await event.edit(f"**Pesan dare**\n\n{response.message.message}")


CMD_HELP.update(
    {
        "truth_dare": "** Plugin :** truth_dare\
        \n\n  •  Perintah : `.truth`\
        \n  •  Function : Untuk mengirim pesan truth secara random\
        \n\n  •  Perintah : `.dare`\
        \n  •  Function : Untuk mengirim pesan dare secara random\
    "
    }
)
