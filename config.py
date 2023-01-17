import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5988729095:AAGvaDalDuWU9vhSIcZHwywZYjRRiUJPcAw")
      API_ID = int(os.environ.get("APP_ID", "5503927"))
      API_HASH = os.environ.get("API_HASH", "6f3a051b5da7f5b499cde019d273fca1")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "\n**Powered By :- @MoviesLandFamily \n**[♻JOIN US](https://t.me/MoviesLandFamily) | [♻INVITE](https://api.whatsapp.com/send?text=കാണാൻ%20ആഗ്രഹമുള്ള%20ഏതു%20സിനിമയും%20ഏതു%20നേരത്തും%20ചോദിക്കാം%20-%20https://t.me/movieslandfamily/)️**")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "royrajan")
