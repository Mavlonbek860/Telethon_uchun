from telethon import TelegramClient

api_id = 29953563
api_hash = '52c460e5dcc4801f1dae5aab3ee3a740'
bot_token = '7674394960:AAEO4-YQI80TIlKOcluoAJFyj_g8dM5gbnQ'

client = TelegramClient('mavlon', api_id, api_hash)

async def main():
	me = await client.get_me()
	print(me.stringify())
	username = me.username
	print(username)
	print(me.phone)
	async for dialog in client.iter_dialogs():
		print(dialog.name, 'has ID', dialog.id)
	#await client.send_message('+998993958460', 'hello friend!')
	async for message in client.iter_messages('🎇🇺🇿Norinlik🇺🇿🎇 🎇🇺🇿somsapazlar🇺🇿🎇'):
		print(message.id, message.text)

with client:
	client.loop.run_until_complete(main())