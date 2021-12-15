# EmojiGram
Just a simple user bot for making custom animated and static emoji, based on commands.

# Installation
## Environment (**Recommended**)

`python -m venv .env`

On Windows (using cmd.exe):

`./.env/Scripts/activate.bat`

On Windows (using powershell.exe):

`./.env/Scripts/activate.ps1`

On Windows (using bash.exe):

`source .env/Scripts/activate`

On Linux (using /bin/bash):

`source .env/bin/activate`

Then when you are in the virtual environment install the packages using:

`pip install -r requirements.txt`

## confing.ini

Create a new file called `config.ini` and [create a new API Key](https://my.telegram.org/apps)

Then put your `api_id` and your `api_hash` like this:

```ini
[pyrogram]
api_id = {api_id}
api_hash = {api_hash}
```

## Start (**IN THE ENVIRONMENT!!!!**)

`python main.py`

# config.json (**structure**)

```JSON
{
  "prefix": "!",
  "emoji": {
    "static": "¯\\_(ツ)_/¯",
    "animated": {
      "fps": 0.1,
      "frames": [
        "H",
        "He",
        "Hel",
        "Hell",
        "Hello",
        "Hello W",
        "Hello Wo",
        "Hello Wor",
        "Hello Worl",
        "Hello World",
        "Hello World!"
      ]
    }
  }
}
```

`prefix`: is the command prefix (ex: `!` would be `!static`, `!animated`)

`emoji`: is a dictionary, where the keys will be the command (`ex: !animated`)

If you want to make a static emoji just put as the value of the command the string to send.

Otherwise, if you want to make an animated emoji just put as the value of the command another dictionary formed with:

`fps`: The time (in seconds) between a frame and another.

`frames`: A list of strings that will be like the frames of the animation

# **WARNING**

Remember to **don't** use too many frames for your animation or an fps value **too low**, otherwise **you will be blocked** by telegram.

**Never** put a blank string or a string ending with a space. Also **never** put two equal frames one next to another.

# Contribution

You are free to contribute to this project :)
