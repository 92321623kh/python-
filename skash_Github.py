#スカッシュゲーム(壁打ちテニス)

#モジュールのインポート
from tkinter import *
from tkinter import ttk
import random

#ゲームスタート画面表示
root = Tk()
root.geometry('640x480')
#フレーム生成
frame3 = ttk.Frame(root)
width=250,
height=200,
frame3.pack()
            
style = ttk.Style()
style.theme_use('classic')
            
#ラベル表示
label4 = ttk.Label(
frame3,
text='GAME START',
background='white',#背景色
foreground='red',#文字の色
relief='solid',#枠線のスタイル
font = ("FixedSys","60","bold","underline",),#フォント設定
borderwidth=10,#枠線の幅
anchor = N,
padding=(170, 240))#文字を中心とした塗りつぶしの位置
label4.grid(row=0, column=0)
#ボタン生成
button2 = ttk.Button(root,
                    text='START',
                    width='10',
                    command=lambda:[close_window(),skashgame()])#ウィンドウ閉じる＆ゲーム再開

button2.place(x=180,y=320)#ボタン位置

#ウィンドウ閉じる
def close_window():
    root.destroy()
    
def skashgame():
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
        global racket_ichi_x,racket_size,racket_left,racket_center,racket_right,point,speed
        global block_ichi_x,block_size,point,stock
        global racket_ichi_x,racket_size,point,speed
        global block_ichi_x,block_size,block_idou_x,point,stock

    
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
    #ポイント加算オブジェクト
        cv.create_rectangle( 350, 0,350 +76,8,fill="red")
    #ポイント減算オブジェクト
        cv.create_rectangle( 640,10, 630,10+120,fill="purple")
    
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
            point -= 20
            win.title(message +"得点="+ str(point))
        
            stock = stock - 1
        
        #ストック数減少
        #ポイント0以下でゲーム終了
            if stock == 0 or point <= 0:
                label2 = ttk.Label(
                frame1,
                text= 'GAMEOVER',
                background='#ffffff',
                width=20,
                anchor=E,
                padding=(5, 10))
                label2.grid(row=0, column=2)
                is_gameover = True
            
            #ゲームオーバー画面表示
                root = Tk()
                root.geometry('640x480')
            #フレーム生成
                frame2 = ttk.Frame(root)
                width=250,
                height=200,
                frame2.pack()
            
                style = ttk.Style()
                style.theme_use('classic')
            
            #ラベル表示
                label3 = ttk.Label(
                frame2,
                text='GAME OVER',
                background='GRAY',#背景色
                foreground='blue',#文字の色
                relief='solid',#枠線のスタイル
                font = ("FixedSys","60","bold","underline",),#フォント設定
                borderwidth=10,#枠線の幅
                anchor = N,
                padding=(170, 240))#文字を中心とした塗りつぶしの位置
                label3.grid(row=0, column=0)
            #ボタン生成
                button1 = ttk.Button(root,
                                     text='Continue?',
                                     width='10',
                                     command=lambda:[close_window(),init_game()])#ウィンドウ閉じる＆ゲーム再開
                button1.place(x=180,y=320)#ボタン位置
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
        #ウィンドウ閉じる
            def close_window():
                root.destroy()

        #やり直しボール移動(ランダム)
            x = random.randint(0,640)
            y = random.randint(0,240)
            ball_ichi_x = (ball_idou_x * -1) + x
            ball_ichi_y = (ball_idou_y * -1) + y

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
        if  ball_ichi_y + ball_idou_y <= 8 and (
            350 <= (ball_ichi_x + ball_idou_x) <=
            (350 + 76)
            ):
            ball_idou_y *= -1
        #スピード元通り
            ball_idou_x = 15
            ball_idou_y  = -15
            if random.randint(0, 1) == 0:
                ball_idou_x *= -1
        #ポイントプラス
            point += 20
            win.title("GREAT! 得点="+ str(point))
        
#ポイント減算オブジェクトに当たったかの判定
        if  10 <= ball_ichi_y + ball_idou_y <= (10+120) and (
            630 <= (ball_ichi_x + ball_idou_x) 
            ):
            ball_idou_y *= -1
        #スピードアップ
            ball_idou_x = 30
            ball_idou_y  = -30
            if random.randint(0, 1) == 0:
                ball_idou_x *= -1
        #ポイントマイナス
            point -= 20
            win.title("BAD! 得点="+ str(point))
            cv.create_rectangle( 640,150, 630,200,fill="purple")

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
