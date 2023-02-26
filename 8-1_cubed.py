print('何か数字を入力してください。3乗します。:')
x_Input=input()

try:
    if type(x_Input) is not int:
        x_Input=float(x_Input)
        print('出力結果は……',x_Input**3)
except ValueError:
    print('数字じゃないですよね?処理終了。')
