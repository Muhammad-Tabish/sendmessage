import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '+923414279535',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())