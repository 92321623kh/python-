#スカッシュゲーム(壁打ちテニス)

#モジュールのインポート
from tkinter import *

#ウィンドウ作成
win = Tk()
cv = Canvas(win,width = 640,height = 480)
cv.pack()

#ゲームの初期化
def init_game():
    global is_gameover,ball_ichi_x,ball_ichi_y
    global ball_idou_x,ball_idou_y,ball_size
    global racket_ichi_x,racket_size,point,speed
    
    is_gameover = False
    ball_ichi_x = 0
    ball_ichi_y = 250
    ball_idou_x = 15
    ball_idou_y = -15
    ball_size = 10
    racket_ichi_x = 0
    racket_size = 100
    point = 0
    speed = 50
    win.title("スカッシュゲームスタート！")
    
#ゲームのメイン処理
init_game()
win.mainloop()
