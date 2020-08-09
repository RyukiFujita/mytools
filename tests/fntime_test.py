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
