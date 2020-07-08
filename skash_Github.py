#スカッシュゲーム(壁打ちテニス)
#branchテスト

#モジュールのインポート
from tkinter import *
import random

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
    point = 10
    speed = 35
    win.title("スカッシュゲームスタート！")

#画面描画
def draw_screen():
    #画面クリア
    cv.delete('all')
    #キャンバス（画面）の作成
    cv.create_rectangle(0,0,640,480,fill="white",width=0)

def draw_ball():
    #ボール描く
    cv.create_oval(ball_ichi_x - ball_size,ball_ichi_y - ball_size,
        ball_ichi_x + ball_size,ball_ichi_y + ball_size,fill = "red")

def draw_racket():
    #ラケットを描く
    cv.create_rectangle(racket_ichi_x,470,racket_ichi_x +75,480,fill="yellow")

#ボールの移動
def move_ball():
    global is_gameover,point,ball_ichi_x,ball_ichi_y,ball_idou_x,ball_idou_y
    if is_gameover: return

 #左右の壁に当たったかの判定
    if ball_ichi_x + ball_idou_x < 0 or ball_ichi_x + ball_idou_x > 640:
        ball_idou_x *= -1

#天井か床に当たったかの判定
    if ball_ichi_y + ball_idou_y < 0:
        ball_idou_y *= -1
        
 #ラケットに当たったか判定
    if ball_ichi_y + ball_idou_y > 470 and (
        racket_ichi_x <= (ball_ichi_x + ball_idou_x) <=
        (racket_ichi_x + racket_size)
        ):
        ball_idou_y *= -1
        if random.randint(0, 1) == 0:
            ball_idou_x *= -1

        mes = random.randint(0,4)
        if mes == 0:
            message = "うまい"
        if mes == 1:
            message = "グッド"
        if mes == 2:
            message = "ナイス"
        if mes == 3:
            message = "よし"
        if mes == 4:
            message = "素敵"
        point += 10
        win.title(message + "得点="+ str(point))

 #ミスしたときの判定
    if ball_ichi_y + ball_idou_y >= 480:
        mes = random.randint(0,2)
        if mes == 0:
            message = "下手くそ"
        if mes == 1:
            message = "ミス"
        if mes == 2:
            message = "は？"
        win.title(message +"得点=" + str(point))
        is_gameover = True

    if 0 <= ball_ichi_x + ball_idou_x <= 640:
        ball_ichi_x = ball_ichi_x + ball_idou_x
    if 0 <= ball_ichi_y + ball_idou_y <= 480:
        ball_ichi_y = ball_ichi_y + ball_idou_y

#マウスの動きの処理
def motion(event):
    global racket_ichi_x
    racket_ichi_x = event.x

def click(event):
    if event.num == 1:
        init_game()

#マウスの動きとクリックの確認
win.bind('<Motion>',motion)
win.bind('<Button>',click)

#ゲームの繰り返し処理の指令
def game_loop():
    draw_screen()
    draw_ball()
    draw_racket()
    move_ball()
    win.after(speed,game_loop)
    
#ゲームのメイン処理
init_game()
game_loop()
win.mainloop()
