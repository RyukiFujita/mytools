# mytools
My python tools

## 関数の処理時間を表示
計測したい関数に@fntimeを付ける
``` tests/fntime_test.py
from mytools import fntime

@fntime
def hoge() :
    for i in range(10000000) :
        dummy = True

@fntime
def fuga() :
    for i in range(100000000) :
        dummy = True

@fntime
def hoga() :
    for i in range(1000000000) :
        dummy = True

hoge()
fuga()
hoga()
```
出力
![出力]("https://raw.githubusercontent.com/RyukiFujita/blob/images/fntime_result.png")
