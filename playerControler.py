"""
    2018/03/10
    目覚まし機能の改善のためのplayerControllerの作り直し

    - オブジェクト指向の記述
    - 分単位での時刻設定の実現

"""

import subprocess
import datetime
import sys
import RPi.GPIO as GPIO
import loader

# 制御用スイッチの番号
SWITCH = 27

def initialize():
    # 準備を始める前に，スイッチが入っているかチェック
    # gpio初期化
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SWITCH, GPIO.IN)	# 入力にセット

    if GPIO.input(SWITCH) == GPIO.HIGH:
        sys.exit()  # スイッチが入っていないならその場で終わり

def fetch_time():
    # 曜日ごとに鳴らす時刻 : 月曜-日曜の時刻を "hh:mm" で表す
    SETTIME = [
        "7:15", #Mon
        "7:15", #Tue
        "7:15", #Wed
        "7:15", #Thu
        "7:15", #Fri
        "7:15", #Sat
        "7:15"  #Sun
    ]

    # 時刻情報の確認
    today_datetime = datetime.datetime.now()
    weekday = today_datetime.weekday()   # 曜日：月曜日を0として整数で扱う
    hour = today_datetime.hour   # 時：0-23で表す
    minute = today_datetime.minute # 分：0-59で表す
    currentTime = [hour, minute]    # 現在時刻について[時, 分]の組

    # 鳴らすべき時間か判定
    # [時, 分]の組を得る
    todaysSetTime = list(map(int, SETTIME[weekday].split(":")))
    if currentTime != todaysSetTime:
        # 時刻の要素が少しでも一致していない時
        sys.exit()


# 目覚ましBGMのオブジェクト ----------------------------------------
class Player:

    def __init__(self):
        mLoader = loader.Loader()
        # ループ
        self.play_loop()

    def play(self, fileName):
        subprocess.call("mpg321 -g 100 " + fileName, shell=True)

    def play_loop(self):
        # BGMはスイッチが入っている限り鳴り続ける
        while GPIO.input(SWITCH) == GPIO.LOW:
            self.play(mLoader.load())


if __name__ == '__main__':
    initialize()
    fetch_time()
    pl = Player()
