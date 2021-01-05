
class Company_exist_err(Exception):
    def __str__(self):
        return '公司已存在，请更换公司名称或编辑已有公司'

class Staff_exist_err(Exception):
    def __str__(self):
        return '员工已存在，请更换员工工号或编辑已有员工'

class Project_exist_err(Exception):
    def __str__(self):
        return '项目已存在，请更换项目和子项目名称或编辑已有项目'

class Caption_exist_err(Exception):
    def __str__(self):
        return '科目已存在，请更换一级和二级科目名称或编辑已有项目'

class Account_exist_err(Exception):
    def __str__(self):
        return '账户已存在，请更换账户名称或编辑已有账户'

class No_import_data_err(Exception):
    def __str__(self):
        return '无有效数据可导入'