from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _

# Create your managers here.


class UserManager(BaseUserManager):
    def create_user(self, email, name, phone_number, date_of_birth, password=None):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, date_of_birth, password):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
