class Simple:           #Simpleクラス定義
    pass

Simple.x = 100          #クラス変数xを代入
print(Simple.x * 2)

def hello(msg = "ハロー"):      #helloメソッドの定義
    print(msg)

def drum(beat = "とことこ"):
    print(beat)

def sax(phrase = "プープー"):
    print(phrase)

Simple.greeting = hello         #greetingメソッドを追加する
Simple.greeting("おはよう")     #実行

obj = Simple()
obj.a = 123
print(obj.a)

obj1 = Simple()         #Simpleクラスからインスタンスを生成
obj2 = Simple()         #Simpleクラスからインスタンスを生成
obj1.play = drum        #obj1にインスタンスメソッドplay()を追加する
obj2.play = sax         #obj2にインスタンスメソッドplay()を追加する

obj1.play("ドンドコ")       #実行
obj2.play("ぷーぷー")       #実行

#追加したメンバーを削除する
obj.a = None
obj1.play = None
del Simple.x
