from internet_speed_bot import InternetSpeedTwitterBot

PROMISED_DOWNLOAD_SPEED = 200
PROMISED_UPLOAD_SPEED = 50

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if PROMISED_DOWNLOAD_SPEED > bot.down or PROMISED_UPLOAD_SPEED > bot.up:
    bot.tweet_at_provider(PROMISED_DOWNLOAD_SPEED, PROMISED_UPLOAD_SPEED)
