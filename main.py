from time import time, sleep
from os import system
from terminut import BetaConsole # https://pypi.org/project/terminut/ (by @imvast)
import requests
from pypresence import Presence # https://pypi.org/project/pypresence/ (by @qwertyquerty)





# discord rpc
RPC = Presence("1207858419411849226")
RPC.connect()
RPC.update(details="Checking discord tokens...", state="discord.gg/nsc", start=time())







# discord api
class CustomDiscordAPI:
    def __init__(self, version: str = "v9"):
        self.version = version

    def getUser(self, token):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }
        response = requests.get(f"https://discord.com/api/{self.version}/users/@me", headers=headers)

        return response








# main function
if __name__ == "__main__":
    c = BetaConsole(speed=2)
    timestamp = c.getTimestamp()
    discordApi = CustomDiscordAPI()

    system("cls || clear")
    print(f"""
             __               ___  __   __       
        \_/ /  \ |__| |  |     |  /  \ /  \ |    
        / \ \__/ |  | |/\|     |  \__/ \__/ |___ 
    Token Checker | Developed by @xohw | discord.gg/nsc
    """)

    with open("./tokens.txt", "r") as file:
        totalTokens = len(file.readlines())
        RPC.update(details=f"Checking {totalTokens} discord tokens...", state="discord.gg/nsc", start=time())
        c.alphaPrint("", f"[{timestamp}] Checking {totalTokens} discord tokens...")

        for token in file:
            token = token.strip()
            userData = discordApi.getUser(token)

            if userData.status_code == 200:
                user = userData.json()
                userId = user["id"]
                userEmail = user["email"]
                userName = user["username"]
                userLocale = user["locale"]

                c.alphaPrint("", f"[{timestamp}] [VALID] ID: {userId} | Email: {userEmail} | Username: {userName} | Locale: {userLocale}")
            else:
                c.alphaPrint("", f"[{timestamp}] [INVALID] {token}")

    while True:
        sleep(0.1)