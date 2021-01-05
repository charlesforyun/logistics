from django import forms
from apps.forms import FormMixin
from apps.logistics_auth.models import User


class LoginForm(forms.Form, FormMixin):
    """
    max_length,min_length,默认required=true,error_messages
    自定义验证 def clean_fields return fields
               def clean ; have no return
    """
    telephone = forms.CharField(
        max_length=11,
        error_messages={
            'max_length': '号码过长，请重新输入！'
        }
    )
    password = forms.CharField(
        max_length=10,
        min_length=6,
        error_messages={
            'max_length': '密码过长，请重新输入',
            'min_length': '密码过短，请重新输入！'
        }
    )
    remember = forms.IntegerField(
        required=False
    )


class RegisterForm(forms.ModelForm, FormMixin):
    password_repeat = forms.CharField(
        max_length=20,
        error_messages={
            'max_length': '密码太长'
        }
    )

    class Meta:
        model = User
        fields = ['telephone', 'username', 'password', 'email']
        # error_messages = {
        #     'telephone': {
        #         'max_length': '太长了',
        #     }
        # }

    def clean(self):
        """
        验证两次密码是否一致
        :return: super().clean
        """
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password_repeat')
        if password1 != password2:
            raise forms.ValidationError('两次密码输入不一致')
        else:
            return cleaned_data

