# -*- coding: utf-8 -*-
# food
# 2021/8/31

from configs.config import HOST
import requests
from libs.login import Login
from shop import Shop
class Food:
    def __init__(self,inToken):
        self.header = {"Authorization":inToken}  #请求头参数

    # 1.添加食品种类接口
    def add_category(self, inDate):
        url = f'{HOST}/shopping/addcategory'
        resq =requests.post(url, data=inDate, headers=self.header)
        return resq.json()

    # 2.列出食品信息
    def get_category(self, uri):
        url = f'{HOST}{uri}'
        resq = requests.get(url, headers=self.header)
        return resq.json()


if __name__ == '__main__':
    # 1.登录获取token
    token = Login().login({"username":"th0310","password":"11446"},getToken=True)

    # 2.添加食品种类
    foodObj = Food(token)
    inDate = {"restaurant_id":"3269"}  # {'name': '草莓酸奶', 'description': '草莓酸奶,正常糖,走冰', 'restaurant_id': '8442'}
    resq = foodObj.add_category(inDate) # 返回值是字典格式
    print(resq)

    # 3.列出食品信息
    # 需要先获取商铺ID
    # shopObject = Shop(token)
    # res = shopObject.shop_list({"page":1,"limit":1})
    # shopId = res["data"]["records"][0]["id"]
    # resq = foodObj.get_category('dfd')
    # print(resq['error'])



