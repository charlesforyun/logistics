from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, \
    BaseUserManager, UserManager
from shortuuidfield import ShortUUIDField  # pip install django-shortuuidfield
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    """
    重写用户管理验证字段,原始（username,password）
    -->telephone、username、password
    example：15720618047 邓平 123456，其中telephone和password用于登陆验证
    """
    def _create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError('请输入手机号码！')
        if not username:
            raise ValueError('请输入用户名！')
        if not password:
            raise ValueError('请输入密码！')

        user = self.model(telephone=telephone, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone, username, password, **kwargs)

    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone, username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """
    password,is_supper，父类中有了。
    重写AbstractUser模型，settings中需要设置AUTH_USER_MODEL='appname.User'
    使用shortuuid作为主键
    unique(唯一)、primary_key、default、db_column(专栏，指定db中名字)、null（db中是否为空）、blank（表单验证是否为空）
    help_text()、error_message()
    不难发现，所有的关键参数默认为False
    """
    uuid = ShortUUIDField(primary_key=True)  # 全球唯一标识符小标识符
    telephone = models.CharField(max_length=11, unique=True)  # 不用int类型0开头的电话会丢失，必须指定最大长度
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)  # False是无法验证用户获取User对象
    is_staff = models.BooleanField(default=True)
    data_joined = models.DateTimeField(auto_now_add=True)
    # 设置第一次实例保存当前时间，后续可以通过save更改，auto_now则不可以手动更改非当前时间

    objects = UserManager()  # 这个objects指向的父类就是model.objects

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'telephone'  # 该字段和password用于验证
    REQUIRED_FIELDS = ['username']
    # 使用telephone、username、password、email注册

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
