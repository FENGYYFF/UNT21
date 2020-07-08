import openpyxl

class ReadExcel(object):
    def __init__(self,filename,sheetname):
        super().__init__()
        self.filename = filename
        self.sheetname = sheetname

    def getTestData(self):
        # 创建workbook对象
        workbook = openpyxl.load_workbook(self.filename)
        # 创建worksheet对象
        sheet = workbook[self.sheetname]  # type: openpyxl.workbook.workbook.Worksheet
        # 获取行
        rows = list(sheet.rows)
        # 创建一个空数据列表
        testdata = []
        # 获取表头
        title = [cell.value for cell in rows[0]]
        # 获取其余行的内容
        for row in rows[1:]:#循环每一行
            content = [cell.value for cell in row]
            # 获取到每一行的content数据与title进行打包
            zip_case = dict(zip(title,content)) # 转型成dict
            # 把zipcase添加到testdata
            testdata.append(zip_case)

        return testdata
