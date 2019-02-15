from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _

from .manager import UserManager
from .models import User


# Create your forms here.


class ManagerUserCreationForm(forms.ModelForm):
    # 사용자 생성 폼
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Email address'),
                'required': 'True',
            }
        )
    )
    name = forms.CharField(
        label=_('first name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('이름'),
                'required': 'True',
            }
        )
    )
    phone_number = forms.CharField(
        label=_('휴대폰 번호'),
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('휴대폰 번호'),
                'required': 'True',
            }
        )
    )
    date_of_birth = forms.DateField(
        label=_('생년월일'),
        required=True,
        widget=AdminDateWidget()
    )

    class Meta:
        model = User
        fields = ('email', 'name', 'phone_number', 'date_of_birth')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(ManagerUserCreationForm, self).save(commit=False)
        user.email = UserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(UserManager().make_random_password())
        if commit:
            user.save()
        return user


class UserPasswordResetForm(forms.Form):
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control font-goudy',
                'placeholder': _('Password'),
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control font-goudy',
                'placeholder': _('Password confirmation'),
                'required': 'True',
            }
        )
    )

    def clean_password2(self):
        # 두 비밀번호 입력 일치 확인
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password)
            except forms.ValidationError as error:
                self.add_error('password2', error)
