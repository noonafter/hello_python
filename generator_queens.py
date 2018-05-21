def borad(queen_num=8):
    pos_range = range(queen_num)
    for queeen0 in pos_range:
        for queeen1 in pos_range:
            for queeen2 in pos_range:
                for queeen3 in pos_range:
                    for queeen4 in pos_range:
                        for queeen5 in pos_range:
                            for queeen6 in pos_range:
                                for queeen7 in pos_range:
                                    yield [queeen0,queeen1,queeen2,queeen3,queeen4,queeen5,queeen6,queeen7]

def conflict_detec(queen_tuple):
    queen_len = len(queen_tuple)
    if set(queen_tuple) != set(range(queen_len)):
        return True
    else:
        for ind_cur in range(1,queen_len):
            for ind_pre in range(0,ind_cur):
                if abs(ind_cur-ind_pre)==abs(queen_tuple[ind_cur]-queen_tuple[ind_pre]) and ind_cur != ind_pre:
                    return True
    return False


count = 0
for i in borad():
    if conflict_detec(i):continue
    else:
        count+=1
        print(i)
print("The number of solutions for this problem is %d" % count)


#心得： 序列索引引用应该用[],而不是圆括号 TypeError: 'list' object is not callable
#如果没有生成器，这个问题需要创建8**8个长度为8的列表，内存会炸

#example in the book
def conflict(state,nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(nextX-state[i]) in (0,abs(nextY-i)):
            return True
    return False

def queens(num=8,state=()):
    #生成器加递归 解决八皇后问题
    #num确定棋盘大小，state确定棋盘上已有皇后位置
    for pos in range(num):
        if not conflict(state,pos):
            if len(state)==num-1:
                yield (pos,)
            else:
                for result in queens(num,state=state+(pos,)):
                    # 对生成器进行迭代，用自己的话来说就是对迭代器进行解包
                    yield (pos,)+result
                    #棋盘大小确定，已有皇后位置确定的情况下，问题的解为（下一列可行的pos）+queens(num,state+(pos,))"当然这里也得用for对迭代器进行解包"

for i in queens():
    print(i)

#心得：生成器+递归，效果很强大。
#递归特点：1.有基本情况，能够终止循环；2.递归过程中，递归函数参数要像基本情况靠近
#什么时候适合用生成器：需要用到for进行迭代时