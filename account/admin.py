from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.translation import gettext_lazy as _

from account.forms import ManagerUserCreationForm
from .models import User, RegisterLink


# Register your models here.


class UserAdmin(BaseUserAdmin):
    add_form = ManagerUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'email', 'phone_number', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    list_display_links = ('name',)
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    actions = ['admin_send_invitation']
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name', 'phone_number', 'date_of_birth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone_number', 'date_of_birth'),
        }),
    )
    search_fields = ('email', 'name', 'phone_number')
    ordering = ('-date_joined',)

    def admin_send_invitation(self, request, queryset):
        queryset = queryset
        users = queryset
        for user in users:
            link = RegisterLink.objects.create(user=user)
            user.email_user("서강대학교 멋쟁이 사자처럼 사이트에 가입 안내.", "안녕하세요, %s님!\n멋쟁이 사자처럼에 오신걸 진심으로 환영합니다!\n\n1시간 안에 아래 링크를 통해 서강대학교 멋쟁이 사자처럼 사이트에 가입해주세요:\n%s\n\n감사합니다." % (user.name, request.build_absolute_uri(reverse('register', kwargs={'uuid': link.uuid.hex}))), settings.DEFAULT_FROM_EMAIL)
        self.message_user(request, "%s명에게 초대 메일이 성공적으로 발송되었습니다." % users.count())

    admin_send_invitation.short_description = "선택된 사용자(들)에게 초대 메일 발송"


class RegisterLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'register_until', 'register_available')
    list_display_links = ('user',)


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(RegisterLink, RegisterLinkAdmin)
