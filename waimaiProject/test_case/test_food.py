# -*- coding: utf-8 -*-
# test_food
# 2021/8/31
import allure
import pytest,os
from tools.excelControl import get_excel_data2
@allure.epic("外卖项目")
@allure.feature("食品管理模块")#模块级别
class TestFood:
    # 添加食品种类接口测试方法
    @pytest.mark.parametrize('caseTitle, inDate, expdate',get_excel_data2('../data/testCaseFile_V1.5.xls', "食品管理", "Addfoodkind"))
    @allure.story('添加食品种类')
    @allure.title('{caseTitle}')
    def test_add_category(self, caseTitle, inDate, expdate, food_init):
        '''

        :param caseTitle: 测试用例标题
        :param inDate: 请求参数
        :param expdate: 预期响应
        :param food_init: 调用fixture函数
        :return:
        '''

        # 1.调用添加食品种类接口
        resq = food_init.add_category(inDate)
        # 2.断言
        if 'pass' in caseTitle:
            assert resq['code'] == expdate['code']
        elif 'fail' in caseTitle:
            assert resq['error'] == expdate['error']

    # 列出食品信息接口测试方法
    @allure.story('列出食品')
    @pytest.mark.parametrize('caseTitle, uri, expdate', get_excel_data2('../data/testCaseFile_V1.5.xls','食品管理','listfood'))
    @allure.title('{caseTitle}')
    def test_get_category(self, caseTitle, uri, expdate,  food_init):
        # 1.调用列出食品信息接口
        resq = food_init.get_category(uri)
        # 2.断言
        if 'pass' in caseTitle:
            assert resq['code'] == expdate['code']
        elif 'fail' in caseTitle:
            assert resq['status'] == expdate['status']




if __name__ == '__main__':
    pytest.main(['test_food.py','-s','--alluredir','../report/tmp'])
    os.system('allure serve ../report/tmp')

