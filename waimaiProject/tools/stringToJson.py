# -*- coding: utf-8 -*-
# stringToJson
# 2021/8/31
string = "name=草莓酸奶&description=草莓酸奶,正常糖,走冰&restaurant_id=8442"
list1 = string.split('&')
dict1 = {}
for one in list1:
    listEle = one.split('=')
    key = listEle[0]
    value = listEle[1]
    dict1[key] = value
print(dict1)