# example in book for list nested expansion
def flatten(nested):
    try:
        # considering str class can't be recurred
        try:nested+""
        except TypeError:pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

# inspired by the example in Internet
def unwrap(nested):
    if isinstance(nested,list)==0:
        return [nested] #!!!very import return a list
    else:
        return sum(map(unwrap, nested),[])

# def unwrap(nested): return sum(map(unwrap, nested),[]) if isinstance(nested,list) else [nested]

# from functools import reduce
# from operator import add
# def unwrap(nested):
#     try:nested+[]
#     except TypeError:return [nested] #!!!very import return a list
#     else:return reduce(add,map(unwrap,nested),[])


a = [[1,2,3,[4,5]],[6,7],[8],"nine"]
print(list(flatten(a)))
print(unwrap(a))

#心得： + 可以用来检测变量的类型，很多地方可以代替isinstance()  例如： nested+""
#sum()函数黑科技可以用来展开nested列表，只能是列表字符串等不行，例如sum("abc","")不行
#生成器：使用yield关键字的函数