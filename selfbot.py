print('''

███████╗██╗   ██╗██████╗  ██████╗         ██╗    ██╗███████╗██████╗ 
██╔════╝██║   ██║██╔══██╗██╔═══██╗        ██║    ██║██╔════╝██╔══██╗
███████╗██║   ██║██║  ██║██║   ██║        ██║ █╗ ██║█████╗  ██████╔╝
╚════██║██║   ██║██║  ██║██║   ██║        ██║███╗██║██╔══╝  ██╔══██╗
███████║╚██████╔╝██████╔╝╚██████╔╝███████╗╚███╔███╔╝███████╗██████╔╝
╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚══╝╚══╝ ╚══════╝╚═════╝ 
                                                                    

	''')
from pyrogram import Client , filters
import redis
import psutil
import re
import random
import requests
import time
import datetime
x = False
id = 11421598
hash = "d2726e1c38949a6052d9037f86c1d3bb" 
app = Client("selfpy"  , api_id= id, api_hash=hash)
admin = 1634717698
@app.on_message(filters.private , filters.group)
async def self(client , message):
    user = message.from_user.id
    text = message.text
    chat_id = message.chat.id
    global x
    if x == True:
        if (message.chat.type == 'supergroup') or (message.chat.type == 'private'):
            await app.send_chat_action(chat_id , "typing")
    if user == admin:
        if re.match(r"^help$|^راهنما$" , text):
            await message.reply("""
            راهنمای سلف TAB SUDO V.1
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
 ping
🧤 اطلاع از آنلاینی سلف
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
TypingAction  on | off 
🖋 خاموش و روشن کردن حالت درحال نوشتن
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
Name (text)
👤تغییر نام 
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
bio (text)
👤تغییر بیوگرافی
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆



⚙️ بخش کاربردی
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
 status
♨️ مقدار رم درحال مصرف
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
 block
❌ بلاک کردن کاربر
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
 unblock
✅ آنبلاک کردن کاربر
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆



😼بخش فان
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
font (text)

🖌زیبا سازی اسم
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
jok
جوک به صورت رندوم
☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆

            """)
        if re.match(r"^ping$" , text):
            textt = ["بسه داش ", "ستون بسه", "هستم " , "ژوون بابا"]
            r = random.choice(textt)
            await message.reply(r)
        if re.match(r"^jok$" , text):
            x = requests.get("https://api.codebazan.ir/jok/")
            await message.reply(x.text)
        if re.match(r"status", text):
            await message.reply(f"مقدار رم مصرف شده :{psutil.virtual_memory().percent}")
        if re.match(r"^font (\w+)$",text):
            spl = text.split("font ")[1]
            font = requests.get(f"http://api.codebazan.ir/font/?text={spl}")
            await message.reply(font.text)
        if re.match("^TypingAction (on|off)$" , text):
            spl = text.split("TypingAction ")[1]
            print(spl)
            if spl == "on":
                x = True
                await message.reply("ᴛʏᴘɪɴɢ ᴍᴏᴅᴇ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴛᴜʀɴᴇᴅ ᴏɴ")
            if spl == "off":
                x = False
                await message.reply("ᴛʏᴘɪɴɢ ᴍᴏᴅᴇ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴛᴜʀɴᴇᴅ ᴏꜰꜰ")
        if re.match(r"^(Name|name) (\w+)$" , text):
            spl = text.split(" ")[1]
            print(spl)
            await app.update_profile(first_name=spl)
            await message.reply(f"""⚙️حاجی اسمت با موفقیت عوض شد⚙️
اسم جدیدت :   {spl}""")
        if re.match(r"^Bio|bio (\w+)$" , text):
            spl = text.split(" ")[1]
            if len(spl) > 70 :
                await message.reply("😒😡کلا 70 کارکتر میتونی بنویسی تو بیوتتتت چ خبرتههه داییی⭕️❌")
            else :
                await app.update_profile(bio=spl)
                await message.reply(f"""
                ⚙️حاجی بیوت با موفقیت عوض شد⚙️
بیو جدیدت :   {spl}
                
                
                """)
        if re.match(r"^block (\w+)$" , text):
            spl = text.split(" ")[1]
            await app.block_user(spl)
            await message.reply("❌❌کاربر مورد نظر بلاک شد ستون⚙️")
        if re.match(r"^unblock (\w+)$" ,text):
            spl = text.split(" ")[1]
            await app.unblock_user(spl)
            await message.reply("❌❌کاربر مورد نظر انبلاک شد ستون😒🤦🏿‍♂️")
app.run()
