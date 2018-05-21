# auto-music-player
a music-player loaded by cron in raspberry pi.

- 自室のサーバ化されたRaspberry Pi 2B上で，cronにより毎分呼び出される．設定された時刻と現在時刻が一致しなければプログラム終了という形で制御．
- 主に朝の目覚ましに使用（これがないともはや起きられない）
- loader.pyは，音楽データを読み込む処理を記述しているので，ここにはアップロードしない．  
    
    > 引数なしで，なにかしらのmp3ファイルへのパスを返すだけの単純なプログラムである