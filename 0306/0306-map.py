
#name = input("Enter your name")
def normalize(str):
    #str.upper()  # 把所有字符中的小写字母转换成大写字母
    #str.lower()  # 把所有字符中的大写字母转换成小写字母
    return str.capitalize()  # 把第一个字母转化为大写字母，其余小写
    #str.title()  # 把每个单词的第一个字母转化为大写，其余小写

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)