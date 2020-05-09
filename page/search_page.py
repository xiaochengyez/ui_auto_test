# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2020/5/9  11:50 
# 文件  search_page
from common.base_page import BasePage


class SearchPage(BasePage):
    def search(self,content: str):
        self._params['key'] = content
        self._steps(r"..\data\search.yaml")