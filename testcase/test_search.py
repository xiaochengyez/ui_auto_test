# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2020/5/9  11:54 
# 文件  test_search
from page.search_page import SearchPage


class TestSearch:
    def setup(self):
        self.search = SearchPage()

    def test_search(self):
        self.search.search('ui测试')
        assert 'UI测试' in self.search.page_source()

    def teardown(self):
        self.search.quit()