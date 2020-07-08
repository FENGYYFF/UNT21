users = [{'user': 'python18', 'password': '123456'}]


def register(username, password1, password2):
    """# 注册功能"""
    password1 = str(password1)
    password2 = str(password2)
    for user in users:  # 遍历所有的账号， 判断账号是否存在
        if username == user['user']:
            # 获取键值，判断为已存在
            return {'code': 0, 'msg': '用户已存在'}
        else:
            if password1 != password2:  # 判断输入的两次密码是否一致
                return {'code': 0, 'msg': '输入的两次密码不一致'}
            else:
                # 账号不存在，密码不重复，判断账号密码长度是否在6-18位之间
                if 6 <= len(username) <= 18 and 6 <= len(password1) <= 18:
                    users.append({'user': username, 'password': password1})
                    return {'code': 1, 'msg': '注册成功'}
                else:
                    return {'code': 0, 'msg': '账号和密码的长度需要在6-18位之间'}

# res  = register('p8', 1256, 1256)
# print(res)
