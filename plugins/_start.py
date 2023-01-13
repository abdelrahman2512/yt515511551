# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [YouTube-Bot](https://github.com/sanila2007/YouTube_bot_telegram)

# Read GNU General Public License v3.0: https://github.com/sanila2007/YouTube_bot_telegram/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I am doing these things for free and open source
# Star, fork, enjoy!


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔍Search YouTube", switch_inline_query_current_chat="")
        ]
    ]
)


@Client.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    reply_markup = START_BUTTONS
    await message.reply(
        f"السلام عليكم يا  {message.from_user.first_name}!\n\n هذا بوت لتحميل قوائم تشغيل يوتيوب و فيديوهات يوتيوب \n\n فقط أرسل رابط قائمة تشغيل أو رابط فيديو يوتيوب \n\n 🚨 // البوت لا يدعم تحميل قوائم التشغيل بصيغة صوتية للأسف \n\n 🚨 ممنوع استخدام البوت لتحميل الأغاني أو المسلسلات أو الأناشيد الإسلامية أو أي شيء حرام \n\n لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 \n\n و لدعم استمرار المشروع هنا \n\n  http://paypal.me/kelectronic89  "
        f"يمكنك أن تضغط الأمر \n\n /help \n\n لمزيد من المساعدة ", reply_markup=reply_markup)
