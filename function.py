# 函数
import var

amount = len(var.need) # 物品种类数
# 计算总需求


def 计算总需求():
    rv=[]
    for j in range(amount) :
        rv.append(0)
        for i in var.units:
            rv[j] += __计算每个单位的需求(i)[j]
    var.need_t = rv
    # return rv

def __计算每个单位的需求(u):
    rv=[]
    for j in range(amount) :
        rv.append(var.pf[u.type][j]*u.worker)
    return rv

def __计算总金钱():
    rv = 0
    for i in var.units:
        rv += i.money

def 计算价格(p):
    return 1.5



