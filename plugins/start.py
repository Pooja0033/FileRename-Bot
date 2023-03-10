from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from Script import script
from helper.database import db
from config import START_PIC, FLOOD, ADMIN 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):    
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    button=InlineKeyboardMarkup( [[
                InlineKeyboardButton("π π²πΎπ½ππ°π²π π", callback_data='dev')                
                ],[
                InlineKeyboardButton('π₯Ή πππΏπΏπΎππ π₯Ή', url='https://t.me/Prv_35'),
                InlineKeyboardButton('π«° α΄α΄Ι΄α΄α΄α΄ π«°', callback_data='donate')
                ],[
                InlineKeyboardButton('π«£ α΄Κα΄α΄α΄ π«£', callback_data='about'),
                InlineKeyboardButton('π« Κα΄Κα΄ π«', callback_data='help')
                ]]
                )
    if START_PIC:
        await message.reply_photo(
            photo=random.choice(START_PIC), 
            caption=(script.START_TXT.format(user.mention)), 
            reply_markup=button
        )       
    else:
        await message.reply_text(
            text=(script.START_TXT.format(user.mention)), 
            reply_markup=button, 
            disable_web_page_preview=True
        )

    
@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    user = query.from_user
    if data == "start":
        await query.message.edit_text(
            text=(script.START_TXT.format(user.mention)),
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("π π²πΎπ½ππ°π²π π", callback_data='dev')                
                ],[
                InlineKeyboardButton('π₯Ή πππΏπΏπΎππ π₯Ή', url='https://t.me/Prv_35'),
                InlineKeyboardButton('π«° α΄α΄Ι΄α΄α΄α΄ π«°', callback_data='donate')
                ],[
                InlineKeyboardButton('π«° α΄Κα΄α΄α΄ π«°', callback_data='about'),
                InlineKeyboardButton('π« Κα΄Κα΄ π«', callback_data='help')
                ]]
                )
            )     
    
    elif data == "help":
        await query.message.edit_text(
            text=script.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("ποΈπ²π»πΎππ΄ποΈ", callback_data = "close"),
               InlineKeyboardButton("Β«Β«π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "donate":
        await query.message.edit_text(
            text=script.DONATE_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("ποΈπ²π»πΎππ΄ποΈ", callback_data = "close"),
               InlineKeyboardButton("Β«Β«π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[    
               InlineKeyboardButton("β‘οΈ α΄α΄α΄ΙͺΙ΄ β‘οΈ", url="https://t.me/Owner_PM_Bot") ],[      
               InlineKeyboardButton("ποΈπ²π»πΎππ΄ποΈ", callback_data = "close"),
               InlineKeyboardButton("Β«Β«π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=script.DEV_TXT,
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("ποΈπ²π»πΎππ΄ποΈ", callback_data = "close"),
               InlineKeyboardButton("Β«Β«π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()



@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"Error:\n`{e}`")


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**WΚα΄α΄ α΄α΄ Κα΄α΄ α΄‘α΄Ι΄α΄ α΄α΄ α΄α΄ α΄α΄ α΄‘Ιͺα΄Κ α΄ΚΙͺs ?ΙͺΚα΄.?**\n\n**FΙͺΚα΄ Nα΄α΄α΄** :- `{filename}`\n\n**FΙͺΚα΄ SΙͺα΄’α΄** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("β Κα΄Ι΄α΄α΄α΄ β", callback_data="rename") ],
                   [ InlineKeyboardButton("β α΄α΄Ι΄α΄α΄Κ β", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**WΚα΄α΄ α΄α΄ Κα΄α΄ α΄‘α΄Ι΄α΄ α΄α΄ α΄α΄ α΄α΄ α΄‘Ιͺα΄Κ α΄ΚΙͺs ?ΙͺΚα΄.?__**\n\n**FΙͺΚα΄ Nα΄α΄α΄* :- `{filename}`\n\n**FΙͺΚα΄ SΙͺα΄’α΄** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("β Κα΄Ι΄α΄α΄α΄ β", callback_data="rename") ],
                   [ InlineKeyboardButton("β α΄α΄Ι΄α΄α΄Κ β", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass
