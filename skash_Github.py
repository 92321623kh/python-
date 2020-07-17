#スカッシュゲーム(壁打ちテニス)

#モジュールのインポート
from tkinter import *
from tkinter import ttk
import random

#ウィンドウ作成
win = Tk()
cv = Canvas(win,width = 640,height = 480)
cv.pack()


#ストックウィンドウ
root = Tk()
#ストックウィンドウ位置指定
root.geometry('280x150+10+40')
root.title('ストック')
frame1 = ttk.Frame(root)
frame1.grid()
style = ttk.Style()
style.theme_use('classic')


#ラベル１表示
label1 = ttk.Label(
    frame1,
    text='残り',
    background='#0000aa',
    foreground='#ffffff',
    padding=(5, 10))
label1.grid(row=0, column=0)

#ラベル２表示
label2 = ttk.Label(
    frame1,
    text='3',
    background='#ffffff',
    width=20,
    anchor=E,
    padding=(5, 10))
label2.grid(row=0, column=2)

#ゲームの初期化
def init_game():
    global is_gameover,ball_ichi_x,ball_ichi_y
    global ball_idou_x,ball_idou_y,ball_size

<<<<<<< HEAD
    global racket_ichi_x,racket_size,racket_left,racket_center,racket_right,point,speed
    global block_ichi_x,block_size,point,stock

    global racket_ichi_x,racket_size,point,speed
    global block_ichi_x,block_size,block_idou_x,point,stock,point2
=======
    global racket_ichi_x,racket_size,point,speed
    global block_ichi_x,block_size,block_idou_x,point,stock

    global racket_ichi_x,racket_size,racket_left,racket_center,racket_right,point,speed
    global block_ichi_x,block_size,point,stock
>>>>>>> 86c0ee0ddab779ddb1adf23e899621847a7df513

    
    is_gameover = False
    ball_ichi_x = 0
    ball_ichi_y = 250
    ball_idou_x = 15
    ball_idou_y = -15
    ball_size = 10
    racket_ichi_x = 0
    racket_size = 100
    block_ichi_x = 100
    block_size = 100
    stock_ichi_x = 100
    stock_ichi_y = 100
    block_idou_x = 30
    plus_block_x = 350
    point = 10
    point2 = 20
    stock = 3
    speed = 70
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
    cv.create_rectangle(racket_ichi_x,470,racket_ichi_x +40,480,fill="yellow")
    cv.create_rectangle(racket_ichi_x+40,470,(racket_ichi_x +40)+40,480,fill="yellow")
    cv.create_rectangle(racket_ichi_x+80,470,(racket_ichi_x +80)+40,480,fill="yellow")
    
    
def draw_block():
    #障害物を描く
    cv.create_rectangle(block_ichi_x,106,block_ichi_x +76,138,fill="blue")

    #ポイント加算障害物
    cv.create_rectangle( 350, 0,350 +76,8,fill="red")
    
    
#ボールの移動
##グローバル関数定義


#ボールの移動
 ##グローバル関数定義

def move_ball():
    global is_gameover,point,ball_ichi_x,ball_ichi_y,ball_idou_x,ball_idou_y,stock
    if is_gameover: return

#左右の壁に当たったかの判定
    if ball_ichi_x + ball_idou_x < 0 or ball_ichi_x + ball_idou_x > 640:
        ball_idou_x *= -1

#天井か床に当たったかの判定
    if ball_ichi_y + ball_idou_y < 0:
        ball_idou_y *= -1
        
#ラケットに当たったか判定
    #ラケット左側当たり判定
    if ball_ichi_y + ball_idou_y > 470 and (
        racket_ichi_x <= (ball_ichi_x + ball_idou_x) <=
       (racket_ichi_x + 40)
        ):
        ball_idou_y *= -1
        
        if ball_idou_x > 0:
            ball_idou_x *= -1
        if ball_idou_x < 0:
            ball_idou_x *= 1

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

    #ラケット中央当たり判定
    if ball_ichi_y + ball_idou_y > 470 and (
        racket_ichi_x+40 <= (ball_ichi_x + ball_idou_x) <=
       ((racket_ichi_x + 40)+40)
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
        
    #ラケット右側当たり判定
    if ball_ichi_y + ball_idou_y > 470 and (
        racket_ichi_x+80 <= (ball_ichi_x + ball_idou_x) <=
       ((racket_ichi_x + 80)+40)
        ):
        ball_idou_y *= -1
        
        if ball_idou_x > 0:
            ball_idou_x *= 1
        if ball_idou_x < 0:
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
        point -= 30
        win.title(message +"得点="+ str(point))

     
        stock = stock - 1
        
        #ストック数減少
        if stock == 0:
            label2 = ttk.Label(
            frame1,
            text= 'GAMEOVER',
            background='#ffffff',
            width=20,
            anchor=E,
            padding=(5, 10))
            label2.grid(row=0, column=2)
            is_gameover = True
        #ストックが０以外の時
        else:
            label2 = ttk.Label(
            frame1,
            text=str(stock),
            background='#ffffff',
            width=20,
            anchor=E,
            padding=(5, 10))
            label2.grid(row=0, column=2)
<<<<<<< HEAD
=======
            
>>>>>>> 86c0ee0ddab779ddb1adf23e899621847a7df513

        #やり直しボール移動(ランダム)
        x = random.randint(0,640)
        y = random.randint(0,240)
        ball_ichi_x = (ball_idou_x * -1) + x
        ball_ichi_y = (ball_idou_y * -1) + y

<<<<<<< HEAD
=======
        #やり直しボール移動    
        ball_ichi_x = ball_idou_x * -1
        ball_ichi_y = (ball_idou_y * -1) + 60
>>>>>>> 86c0ee0ddab779ddb1adf23e899621847a7df513

    #ボールが枠内の時の移動        
    if 0 <= ball_ichi_x + ball_idou_x <= 640:
        ball_ichi_x = ball_ichi_x + ball_idou_x
    if 0 <= ball_ichi_y + ball_idou_y <= 480:
        ball_ichi_y = ball_ichi_y + ball_idou_y

#障害物に当たったかの判定
    if 106 < ball_ichi_y + ball_idou_y < 138 and (
        block_ichi_x <= (ball_ichi_x + ball_idou_x) <=
        (block_ichi_x + 76)
        ):
        ball_idou_y *= -1
        if random.randint(0, 1) == 0:
            ball_idou_x *= -1
        
#ポイント加算オブジェクトに当たったかの判定
    if  ball_ichi_y + ball_idou_y < 8 and (
        350 <= (ball_ichi_x + ball_idou_x) <=
        (350 + 76)
        ):
        ball_idou_y *= -1
        if random.randint(0, 1) == 0:
            ball_idou_x *= -1
        win.title("GREAT! 得点="+ str(point+20))
            
#マウスの動きの処理
def motion(event):
    global racket_ichi_x
    racket_ichi_x = event.x


def click(event):
    if event.num == 1:
        #ストック数回復
        label2 = ttk.Label(
        frame1,
        text='3',
        background='#ffffff',
        width=20,
        anchor=E,
        padding=(5, 10))
        label2.grid(row=0, column=2)
        init_game()

#マウスの動きとクリックの確認
win.bind('<Motion>',motion)
win.bind('<Button>',click)

#ゲームの繰り返し処理の指令
def game_loop():
    draw_screen()
    draw_ball()
    draw_racket()
    draw_block()
    move_ball()
    #move_block()
    win.after(speed,game_loop)
    
#ゲームのメイン処理
init_game()
game_loop()
win.mainloop()
