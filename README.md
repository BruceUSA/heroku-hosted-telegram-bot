Personal modified fork from https://github.com/Kylmakalle/heroku-telegram-bot
# Hosting telegram bot on [Heroku](https://heroku.com) for free.

Easy way to host your python telegram bot on Heroku deploying via [Heroku Toolbelt](https://toolbelt.heroku.com/) (CLI)

You must install [Heroku Toolbelt](https://toolbelt.heroku.com/). If you use modern Ubuntu you can snap it

`sudo snap install --classic heroku`

### Clone repository
`git clone https://github.com/miimote/heroku-hosted-telegram-bot.git`
### Edit files
1. Edit [bot.py](https://github.com/miimote/heroku-hosted-telegram-bot/blob/master/bot.py) file with your code

    **ATTENTION!** 
         Do not collapse/delete/comment `token = os.environ[TELEGRAM_TOKEN]`  
         Do not change any string or add your real Telegram token. Next, token will be setted up below!  
         **Please do not include your token in your files**  
         **Please do not include your token in your files**  
         **Please do not include your token in your files**  
         [More About Config Vars](https://devcenter.heroku.com/articles/config-vars)

2. Edit [requirements.txt](https://github.com/miimote/heroku-hosted-telegram-bot/blob/master/requirements.txt) with your code's dependencies
    In this case I use [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
3. Go to command line
    Bellow, change:  
        - _appname_ by your app name  
        - _123456789:AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLL_ by your Telegram token  
```
#previous git steps if not done
git config --global user.email "your-quoted-e-mail"
git config --global user.name "your-quoted-user-name"

cd heroku-telegram-bot
heroku login
heroku create --region eu appname # create app in eu region, common regions: eu, us
git add .
git commit -am "some git commit comment"
git push heroku master # deploy app to heroku
heroku config:set TELEGRAM_TOKEN=123456789:AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLL # set config vars, insert your own
heroku ps:scale bot=1 # start bot dyno
## Other stuff
heroku logs --tail # If for some reason it’s not working, check the logs
heroku ps:stop bot #stop bot dyno
```

### More about
- https://devcenter.heroku.com/articles/dynos
- https://devcenter.heroku.com/articles/config-vars
- https://devcenter.heroku.com/articles/heroku-redis
- https://devcenter.heroku.com/articles/error-codes

Thanks to [Roman Zaynetdinov](https://github.com/zaynetro) for awesome and easy CLI guide.
