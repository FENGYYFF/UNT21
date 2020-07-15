import openpyxl
from common.caseData import CaseData


class ReadExcel(object):
    def __init__(self, filename, sheetname):
        """
        :param filename: 文件名
        :param sheetname: 表单名
        """
        super().__init__()
        self.filename = filename
        self.sheetname = sheetname

    def openfile(self):
        """
        :return: 返回一个列表的case对象
        """
        # 创建workbook对象
        self.workbook = openpyxl.load_workbook(self.filename)
        # 创建worksheet对象
        self.sheet = self.workbook[self.sheetname]  # type: openpyxl.workbook.workbook.Worksheet

    def getTestData(self):
        self.openfile()
        # 获取行
        rows = list(self.sheet.rows)
        # 创建一个空数据列表
        testdata = []
        # 获取表头
        title = [cell.value for cell in rows[0]]
        # 获取其余行的内容
        for row in rows[1:]:  # 循环每一行
            content = [cell.value for cell in row]
            zip_obj = zip(title, content)
            casedata = CaseData(zip_obj)
            testdata.append(casedata)
        return testdata

    def writeTestData(self,row,column,value):
        """
        :param row: 写入的行
        :param column: 写入的列
        :param value: 写入值
        """
        # 打开文件
        self.openfile()
        #对应的位置写入值
        self.sheet.cell(row,column,value=value)
        # 保存文件
        self.workbook.save(self.filename)


if __name__ == '__main__':
    c = ReadExcel('../testdata/data_xl.xlsx', 'login_sheet')
    d = c.getTestData()
    l = []
    for i in d:
        l.append(i)
    print(*l)
