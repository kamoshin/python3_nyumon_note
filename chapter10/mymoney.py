import exchange        #exchangeモジュールを読み込む
yen = 25000            
rate = 114.22          #円/ドル
charge = 1.0           #為替手数料
doller = exchange.yen2doller(yen, rate, charge)
print(f"{doller :,.2f}ドル")