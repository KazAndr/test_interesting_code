import datetime
import os
main_time = datetime.datetime(2017, 12, 31, hour=23, minute=58, second=57, microsecond=9999, tzinfo=None)
five_time = datetime.datetime(2017, 12, 31, hour=23, minute=56, second=26, microsecond=9999, tzinfo=None)

while five_time > datetime.datetime.now():
        now_time = datetime.datetime.now()
        print('%d:%d:%d' % (now_time.hour, now_time.minute, now_time.second))
os.system("mplayer 5\ минут\ .mp4")
os.system("mplayer Бой\ курантов\ и\ гимн\ России.mp4")
