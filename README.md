mytools
==========
My python tools  
どんどん追加予定．ネタ募集中です．  
こんなのあったらいいなとかアイデアあったら気軽に[twitter](https://twitter.com/lal_ryuki)に連絡ください．  

##### インストール  
```
$ pip install git+https://github.com/ryukifujita/mytools
```

##### アンインストール  
```
$ pip uninstall mytools
```

使い方
==========

## @fntime：関数の処理時間を表示するデコレータ
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
![出力](https://raw.githubusercontent.com/RyukiFujita/mytools/images/fntime_result.png)
