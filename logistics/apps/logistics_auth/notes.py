from django.contrib.auth.models import AbstractUser, UserManager
# from apps.logistics.models import User
# from django.contrib.auth.models import User
import os
"""
默认的是username， email，password
自定义是舍弃系统自己写的的user对象，继承AbstractBaseUser/PermissionsMixin，BaseUserManage
对象重写一份，写完之后参考下面形式，用以创建用户
关于User里面的object指向的都是db.models
"""
# user = User.object.create_user('dengping', '1364477536.com', '123456')
# user2 = User.object.create_superuser('xuchao', '1364477536.com', '123456')
# user3 = User.objects.get(pk=1)
# user3.set_password('2345')
# user3.save()
"""
request.session.items() ==  dict_items([
    ('_auth_user_id', 'E8aHp3q5hesSGJxEjtfdQv'),
    ('_auth_user_backend', 'django.contrib.auth.backends.ModelBackend'),
    ('_auth_user_hash', 'bce45acb9d86039185c46d8c1a58c240ac64a2b5aa28c43e4627f8c19ff697cb')
])
"""