import requests
import telebot,time
from telebot import types
from gatet import Tele
import os

xc = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://www.handyapi.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.handyapi.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

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
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "ERROR"
				if 'risk' in last:
					last='declined'
				elif 'Duplicate' in last:
					last='Approved'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f" {cc} ", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➤ [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➤ [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 ☠️ ➤ [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
				mes.add(cm1,cm3, cm4, cm5, stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝐖𝐀𝐈𝐓 𝐅𝐎𝐑 𝐑𝐄𝐒𝐔𝐋𝐓
𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐁𝐘 : @FC_ZC ✅''', reply_markup=mes)
				bin = cc[:6]
				response = requests.get(f'https://data.handyapi.com/bin/{bin}', headers=xc)
				info = str(response.json()['Scheme'])
				info2 = str(response.json()['Type'])
				info3 = str(response.json()['CardTier'])
				country = str(response.json()['Country']['Name'])
				bank = str(response.json()['Issuer'])
				msg = f'''
Approved ✅

𝗖𝗮𝗿𝗱: {cc}
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Stripe ⚡.
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Approved.

Bin: {bin}
𝐢𝐧𝐟𝐨: {info} - {info2} - {info3}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}

Developer : @FC_ZC ✅'''
				print(last)
				if "nextPageURL" in last:
					live += 1
					bot.reply_to(message, msg)
				elif 'Your card could not be authorized using the postal code provided. Please update the postal code, or contact your card issuer for further details.' in last:
					msg = f'''
Approved ✅

𝗖𝗮𝗿𝗱: {cc}
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Stripe ⚡.
Response -> Your card has insufficient funds.

Bin: {bin}
𝐢𝐧𝐟𝐨: {info} - {info2} - {info3}
𝐁𝐚𝐧𝐤: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country}

Developer : @FC_ZC ✅'''
					bot.reply_to(message, msg)
				elif 'Your card was declined' in last:
					dd += 1
					time.sleep(1)
				elif 'Your card number is incorrect' in last:
					dd += 1
					time.sleep(1)
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