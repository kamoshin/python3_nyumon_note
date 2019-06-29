v = 2
def calc():
    #v = v * 10         #vの代入式を書いた時点でvはローカル変数として解釈される
                        #右項のvが未定義のためエラーになる   
    v_local = v * 10    #vをローカル変数にしない
    ans = 3 * v_local   #vには2が入っている
    print(ans)

calc()
print(v)