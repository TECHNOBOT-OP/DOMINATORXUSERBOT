from . import *

@dominator_cmd(pattern="hello$")
async def viello(event):
    reply_to_id = await reply_id(event)
    event = await event.edit("(❛ Hi ❜!")
    HELL_PIC = "https://te.legra.ph/file/b86eff074051b0b2d4513.jpg"
    K_PIC = "https://te.legra.ph/file/a679e3d061ac6b349cd60.jpg"
    L_PIC = "https://te.legra.ph/file/96c2b61d6361f112ceac5.jpg"
    M_PIC = "https://te.legra.ph/file/4d0c641e085f7ed15dfec.jpg"
    if HELL_PIC:
        HELLO = f"╔┓┏╦━╦┓╔┓╔━━╗\n"
        HELLO += f"║┗┛║┗╣┃║┃║X X ║\n"
        HELLO += f"║┏┓║┏╣┗╣┗╣╰╯║\n"
        HELLO += f"╚┛┗╩━╩━╩━╩━━╝\n"
        on = await event.client.send_file(
            event.chat_id, file=HELL_PIC, caption=HELLO, reply_to=reply_to_id
        )
        await asyncio.sleep(3)
        ok = await event.client.edit_message(event.chat_id, on, file=K_PIC)
        await asyncio.sleep(3)
        ok1 = await event.client.edit_message(event.chat_id, on, file=L_PIC)
        await asyncio.sleep(3)
        ok2 = await event.client.edit_message(event.chat_id, ok1, file=M_PIC)
        await asyncio.sleep(5)
        ok3 = await event.client.edit_message(event.chat_id, ok2, file=L_PIC)
        await asyncio.sleep(5)
        ok4 = await event.client.edit_message(event.chat_id, ok3, file=K_PIC)
        await asyncio.sleep(5)
        ok5 = await event.client.edit_message(event.chat_id, ok4, file=HELL_PIC)
        await asyncio.sleep(3)
        ok6 = await event.client.edit_message(event.chat_id, ok5, file=L_PIC)
        await asyncio.sleep(3)
        ok7 = await event.client.edit_message(event.chat_id, ok6, file=M_PIC)
        await asyncio.sleep(5)
        ok8 = await event.client.edit_message(event.chat_id, ok7, file=L_PIC)
        await asyncio.sleep(5)
        ok9 = await event.client.edit_message(event.chat_id, ok8, file=K_PIC)
        await asyncio.sleep(5)
        ok10 = await event.client.edit_message(event.chat_id, ok9, file=HELL_PIC)
        await asyncio.sleep(5)
        ok11 = await event.client.edit_message(event.chat_id, ok10, file=HELL_PIC)
        await asyncio.sleep(3)
        ok12 = await event.client.edit_message(event.chat_id, ok11, file=L_PIC)
        await asyncio.sleep(3)
        ok13 = await event.client.edit_message(event.chat_id, ok12, file=M_PIC)
        await asyncio.sleep(5)
        ok14 = await event.client.edit_message(event.chat_id, ok13, file=L_PIC)
        await asyncio.sleep(5)
        ok15 = await event.client.edit_message(event.chat_id, ok14, file=K_PIC)
        await asyncio.sleep(5)
        ok16 = await event.client.edit_message(event.chat_id, ok15, file=HELL_PIC)
        await asyncio.sleep(5)
        ok17 = await event.client.edit_message(event.chat_id, ok16, file=HELL_PIC)
        await asyncio.sleep(3)
        ok18 = await event.client.edit_message(event.chat_id, ok17, file=L_PIC)
        await asyncio.sleep(3)
        ok19 = await event.client.edit_message(event.chat_id, ok18, file=M_PIC)
        await asyncio.sleep(5)
        ok20 = await event.client.edit_message(event.chat_id, ok19, file=L_PIC)
        await asyncio.sleep(5)
        ok21 = await event.client.edit_message(event.chat_id, ok20, file=K_PIC)
        await asyncio.sleep(5)
        ok22 = await event.client.edit_message(event.chat_id, ok21, file=HELL_PIC)
        await asyncio.sleep(5)
        ok23 = await event.client.edit_message(event.chat_id, ok22, file=HELL_PIC)
        await asyncio.sleep(3)
        ok24 = await event.client.edit_message(event.chat_id, ok23, file=L_PIC)
        await asyncio.sleep(3)
        ok25 = await event.client.edit_message(event.chat_id, ok24, file=M_PIC)
        await asyncio.sleep(5)
        ok26 = await event.client.edit_message(event.chat_id, ok25, file=L_PIC)
        await asyncio.sleep(5)
        ok27 = await event.client.edit_message(event.chat_id, ok26, file=K_PIC)
        await asyncio.sleep(5)
        ok28 = await event.client.edit_message(event.chat_id, ok27, file=HELL_PIC)
        await event.delete()