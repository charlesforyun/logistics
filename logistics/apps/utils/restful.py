from django.http import JsonResponse
# return JsonResponse({"code": 200, "message": {}, "data": {}})


class HttpCode:
    ok = 200
    params_error = 400  # 黑名单
    un_auth = 401  # 请求头错误，验证失败
    method_error = 405
    server_error = 500


def result(code=HttpCode.ok, message=None, data=None, kwargs=None):
    # 重构JsonResponse
    json_data = {"code": code, "message": message, "data": data}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_data.update(kwargs)
    return JsonResponse(json_data)


def ok(data=None):
    return result(data=data)


def params_error(message=None, data=None):
    return result(code=HttpCode.params_error, message=message, data=data, kwargs=None)


def un_auth(message=None, data=None):
    return result(code=HttpCode.un_auth, message=message, data=data, kwargs=None)


def method_error(message=None, data=None):
    return result(code=HttpCode.method_error, message=message, data=data, kwargs=None)


def server_error(message=None, data=None):
    return result(code=HttpCode.server_error, message=message, data=data, kwargs=None)