from pyrogram import Client, filters
from asyncio import sleep
import json

app = Client("my_account")
CONFIG = None

def loadConfig():
    global CONFIG
    oldConfig = CONFIG

    CONFIG = json.load(open('config.json', encoding='utf-8'))
    if (["prefix", "emoji"] != list(CONFIG.keys())):
        CONFIG = oldConfig
        raise RuntimeError("Invalid config no prefix or emoji config found")
    
    if ("emoji:reload-config" in list(CONFIG["emoji"].keys())):
        CONFIG = oldConfig
        raise RuntimeError("Invalid config don't use 'emoji:reload-config' as alias!")

    if ("emoji:help" in list(CONFIG["emoji"].keys())):
        CONFIG = oldConfig
        raise RuntimeError("Invalid config don't use 'emoji:help' as alias!")


async def editMessage(message, text):
    if (len(text) > 4096):
        text = "Invalid message"
    await app.edit_message_text(message.chat.id, message.message_id, text, None)


@app.on_message(filters.me & ~filters.edited)
async def hello(client, message):
    textMsg = message.text

    if (textMsg.startswith(CONFIG["prefix"])):
        textMsg = textMsg.replace(CONFIG["prefix"], "", 1)
        msgs = textMsg.split(" ")
        command = msgs[0]
        text = ' '+' '.join(msgs[1:])

        if CONFIG:
            if command in CONFIG["emoji"]:
                emoji = CONFIG["emoji"][command]
                if  type(emoji) == str:
                    await editMessage(message, emoji+text)
                elif type(emoji) == dict:
                    if not 'fps' in emoji or emoji["fps"] < 0 or not 'frames' in emoji or type(emoji['frames']) != list:
                        await editMessage(message, "invalid emoji config for alias: "+command)
                    else:
                        for frame in emoji["frames"]:
                            await editMessage(message, frame+text)
                            await sleep(emoji["fps"])
            elif command == "emoji:help":
                text = '\n'.join(list(CONFIG["emoji"].keys()))
                await editMessage(message, text)
            elif command == "emoji:reload-config":
                text = "Success: Config reloaded successfully!"
                try:
                    loadConfig()
                except RuntimeError as e:
                    text = "Error: "+str(e)
                except (FileNotFoundError, FileExistsError):
                    text = "Error: config.json doesn't exist"
                except json.decoder.JSONDecodeError as e:
                    text = "Error: JSON Error, "+str(e)
                finally:
                    await editMessage(message, text)
        else:
            text = "Error: Couldn't load the config"
            await editMessage(message, text)

def main(): 
    loadConfig()

if __name__ == "__main__":
    try:
        main()
        app.run()
    except KeyboardInterrupt:
        print("Good Bye")
    except RuntimeError as e:
        print("Error:", str(e))
    except json.decoder.JSONDecodeError as e:
        print("Error: JSON Error,", str(e))
    except (FileNotFoundError, FileExistsError):
        print("Error: config.json doesn't exist")
