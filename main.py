import requests
import json
from discord_webhook import DiscordWebhook
from datetime import datetime
import time

req = requests.Session()

def getuser(user1, user2):
    user1 = (req.get(
        f'https://users.roblox.com/v1/users/{user1}').json())["name"]
    user2 = (req.get(
        f'https://users.roblox.com/v1/users/{user2}').json())["name"]
    return user1, user2

def main():
    while True:
        with open("config.json") as f:
            data = json.load(f)

        z = ""
        for i in range(len(data["user1"])):
            friends = req.get(
                f'https://friends.roblox.com/v1/users/{data["user1"][i]}/friends').json()

            value = False
            for element in friends["data"]:
                if element["id"] == data["user2"][i]:
                    value = True
                    break

            if value != data["value"][i]:
                user1, user2 = getuser(data["user1"][i], data["user2"][i])
                x = True
                if value == False:
                    if len(data["discord_webhook_link"]) > 0:
                        mentions = ""
                        for y in data["discord_webhook_mention_ids"]:
                            mentions += f"<@{y}> "
                        DiscordWebhook(url=data["discord_webhook_link"], content=f"{mentions}\nUsers [{user1}](<https://www.roblox.com/users/{
                            data["user1"][i]}/profile>) and [{user2}](<https://www.roblox.com/users/{data["user2"][i]}/profile>) aren't friends").execute()
                    print(f"Users {user1} and {user2} aren't friends")
                    z += f" - Users {user1} and {user2} aren't friends"
                elif value == True:
                    if len(data["discord_webhook_link"]) > 0:
                        mentions = ""
                        for y in data["discord_webhook_mention_ids"]:
                            mentions += f"<@{y}> "
                        DiscordWebhook(url=data["discord_webhook_link"], content=f"{mentions}\nUsers [{user1}](<https://www.roblox.com/users/{
                            data["user1"][i]}/profile>) and [{user2}](<https://www.roblox.com/users/{data["user2"][i]}/profile>) are friends").execute()
                    print(f"Users {user1} and {user2} are friends")
                    z += f" - Users {user1} and {user2} aren't friends"
                data["value"][i] = value

        try:
            if x:
                with open("config.json", "w") as f:
                    json.dump(data, f, indent=4)
                try:
                    with open("gol.json") as f:
                        log = json.load(f)
                    log.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S") + z)
                    with open("gol.json", "w") as f:
                        json.dump(log, f, indent=4)
                except:
                    log = []
                    log.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S") + z)
                    with open("gol.json", "w") as f:
                        json.dump(log, f, indent=4)
        except:
            pass

        try:
            with open("log.json") as f:
                log = json.load(f)
            log.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S") + z)
            with open("log.json", "w") as f:
                json.dump(log, f, indent=4)
        except:
            log = []
            log.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S") + z)
            with open("log.json", "w") as f:
                json.dump(log, f, indent=4)

        if data["loop"]:
            time.sleep(data["loop_time_mins"] * 60 + data["loop_time_seconds"])
        else:
            break

if __name__ == "__main__":
    main()
