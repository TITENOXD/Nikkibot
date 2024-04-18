import asyncio

from pyrogram import Client as c

API_ID = input("\nᴇɴᴛᴇʀ ʏᴏᴜʀ ᴀᴘɪ_ɪᴅ ʙᴀʙᴇ:\n > ")
API_HASH = input("\nᴇɴᴛᴇʀ ʏᴏᴜʀ ᴀᴘɪ_ʜᴀsʜ ʙᴀʙᴇ:\n > ")

print("\n\n ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴍᴏʙɪʟᴇ ɴᴜᴍʙᴇʀ ʙᴀʙᴇ.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    xx = f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴄᴏᴘʏ ɪᴛ..\n\n`{ss}`\n\nɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ ʟɪʟʏ x ᴍᴜsɪᴄ"
    ok = await i.send_message("me", xx)
    print("\nʜᴇʀᴇ ɪs ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ, ᴄᴏᴘʏ ɪᴛ, ᴅᴏɴ'ᴛ sʜᴀʀᴇ..\n")
    print(f"\n{ss}\n") 
    print("\nɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ ʟɪʟʏ x ᴍᴜsɪᴄ\n")


asyncio.run(main())
