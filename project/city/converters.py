from django.urls import converters, register_converter


class CategoryConverter:
    """ 关键字参数转化为列表"""
    regex = r'\w+|(\w+\+\w+)+'

    def to_python(self, value):
        # python+django+flask --> ['pythton', 'django', 'flask']
        result = value.split("+")
        # print(result)
        return result

    def to_url(self, value):
        # ['pythton', 'django', 'flask']--> python+django+flask
        if isinstance(value, list):
            result = "+".join(value)
            return result
        else:
            raise RuntimeError("转换url的时候，分类参数必须为列表！ ")


register_converter(CategoryConverter, 'cate')
