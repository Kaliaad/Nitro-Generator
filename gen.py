import random
import requests
from dhooks import Webhook

upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
lower_letter = "abcdefghijklmnopqrstuvwyz"
digits = "123456789"
numbtogen = input('How Many Nitro Codes Do You Want To Generate:')
upper, lower, nums = True, True, True,
all = ""

if upper:
    all += upper_letter
if lower:
    all += lower_letter
if nums:
    all += digits

length = 16
amount = numbtogen

# Kullanıcıdan webhook URL'sini alalım
webhook_url = input("Please enter the webhook URL: ")
hook = Webhook(webhook_url)

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    file.write("Generated Nitro Codes:\n\n")

    for x in range(int(numbtogen)):
        nitro = ''.join(random.sample(all, length))
        print('discord.gift/' + nitro)
        
        url = "https://discord.gift/" + nitro
        response = requests.get(url)
        
        if "discord.gift/" in response.text:
            print(f'Valid nitro: {url}')
            hook.send(url)
            file.write(url + '\n')
        else:
            print(f'Invalid nitro: {url}')

print("Generated nitro codes have been sent and saved to Nitro Codes.txt.")
print("Credits by lulz_sec (ask me if you wanna share in your server please.) and made for discord.gg/bankzgen ehm also my server: https://discord.gg/j3pxHKFkKS")