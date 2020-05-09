# ui_auto_test
ui自动化测试的简单封装
##一、增加yaml文件

```$xslt
- by: id
  locator: kw
- action: send
  value: "{key}"
- by: id
  locator: su
- action: click
```
- by 定位方式
- locator 定位元素
- action  动作
- value  内容



##二、加class
 在api相应目录下找到或增加类或方法，有参数加参数
```$xslt
      def search(self,content: str):
        self._params['key'] = content
        self._steps(r"..\data\search.yaml") 
  ```
##三、测试用例

```$xslt
     
  def setup(self):
        self.search = SearchPage()

    def test_search(self):
        self.search.search('ui测试')
        assert 'UI测试' in self.search.page_source()

    def teardown(self):
        self.search.quit()
    
```

##四、生成测试报告
集成了allure报告

![测试报告](https://raw.githubusercontent.com/little-success/api_xiaoxin/blob/master/src/main/resources/img/01.png)



![Relative date](https://img.shields.io/date/1587719993)
![language](https://img.shields.io/badge/language-java-green.svg)
