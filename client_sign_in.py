from telethon import TelegramClient

api_id = 29953563
api_hash = '52c460e5dcc4801f1dae5aab3ee3a740'

with TelegramClient('mavlon', api_id, api_hash) as client:
	while True:
		client.loop.run_until_complete(client.send_message('me', 'hello myself!'))