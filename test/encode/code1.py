import sys, locale

s = "小甲"
print(s)
print(type(s))
print(sys.getdefaultencoding())
print(locale.getdefaultlocale())

# with open("utf1","w",encoding = "utf-8") as f:
#     f.write(s)
# with open("gbk1","w",encoding = "gbk") as f:
#     f.write(s)
# with open("jis1","w",encoding = "shift-jis") as f:
#     f.write(s)

#coding=utf8

# Unicode编码演示
print('Unicode:')
print(repr(u'Unicode编码'))

# 二进制编码演示
print(u'二进制编码:')
print(repr('Unicode编码'))

