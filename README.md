# Roblox Friend Checker
Checks to see if 2 people have each other friended... for normal reasons, trust.

## Config
*user1* and *user2* are the 2 Roblox user ids that we are checking to see if they are friends or not

If you want to add multiple, add them into the list respectively and add either true or false into the *value* list

If you want to loop it, simply set *loop* to true, and set *loop_time_mins* to however many minutes between checks

If you want to add a discord webhook, simply add the link into *discord_webhook_link*, and if you want to mention any user, add their user id into *discord_webhook_mention_ids*

## Running
Run *main.vbs*

If you want it to run at startup, simply create a shortcut of *main.vbs* and put it in the folder *Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup*

**To close it you have to go into task manager and close python, still a bit janky rn but imma fix it trust**
