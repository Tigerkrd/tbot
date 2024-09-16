import requests
import telebot,time
from telebot import types
from gatet import Tele
import os
token = '6996159050:AAEkMJ8XmbY5T5t2ShnmEXAG5ymjKhHV4UA'
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber ='7535577541'
subscriber ='6532862739'
subscriber ='7397683395'
subscriber ='7194638029'
@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message," 𝚂𝙴𝙽𝙳 𝙲𝙾𝙼𝙱𝙾 𝙵𝙸𝙻𝙴 📁 ")
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗')
						os.remove('stop.stop')
						return
				try:
					api = requests.get(f'https://lookup.binlist.net/{cc[:6]}').json()
				except:
					ch = 'False'
				try:
					chh = api['scheme']
					ch = chh.upper()
				except:
					ch = 'False'
				try:
					typ = api['type']
					type = typ.upper()
				except:
					ch = 'False'
				try:
					raa = api['brand']
					ra = raa.upper()
				except:
					ch = 'False'
				try:
					am = api['bank']['name']
					ame = am.upper()
				except:
					ch = 'False'
				try:
					co = api['country']['name']
					cou = co
				except:
					ch = 'False'
				try:
					emoji = api['country']['emoji']
				except:
					emoji = 'False'
				
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "ERROR"
				if 'risk' in last:
					last='declined'
				elif 'Duplicate' in last:
					last='Approved'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				#status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➤ {last} •", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➤ [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➤ [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 ☠️ ➤ [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
				mes.add(cm1,cm3, cm4, cm5, stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''W𝖆𝖎𝖙 𝖋𝖔𝖗 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 
𝖇𝖞 ➤ @FC_ZC''', reply_markup=mes)
				msg = f'''
Approved ✅
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱: {cc}
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Stripe Charge 5$⚡
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Approved.
- - - - - - - - - - - - - - - - - - - - - - -
Bin : {cc[:6]}
Bin Info : {ch} - {type} - {ra}
Bank : {ame}
Counrty : {cou} {emoji}
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @FC_ZC ✅'''
				print(last)
				if "nextPageURL" in last:
					live += 1
					bot.reply_to(message, msg)
				elif 'Your card could not be authorized using the postal code provided. Please update the postal code, or contact your card issuer for further details.' in last:
					msg = f'''
Approved ✅
- - - - - - - - - - - - - - - - - - - - - - -
𝗖𝗮𝗿𝗱: {cc}
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Stripe Charge 5$⚡
Response -> Your card has insufficient funds.
- - - - - - - - - - - - - - - - - - - - - - -
Bin : {cc[:6]}
Bin Info : {ch} - {type} - {ra}
Bank : {ame}
Counrty : {cou} {emoji}
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @FC_ZC ✅'''
					bot.reply_to(message, msg)
				else:
					dd += 1
				time.sleep(1)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
print("BOT WORKING NOW ✅")
bot.polling()