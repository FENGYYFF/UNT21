import openpyxl
from common.caseData import CaseData


class ReadExcel(object):
    def __init__(self, filename, sheetname):
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
        for row in rows[1:]:  # 循环每一行
            content = [cell.value for cell in row]
            zip_obj = zip(title, content)
            casedata = CaseData(zip_obj)
            testdata.append(casedata)
        return testdata

if __name__ == '__main__':
    c = ReadExcel('../testdata/data_xl.xlsx', 'login_sheet')
    d = c.getTestData()
