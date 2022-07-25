from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다.
        """
        user = self.create_user(
            email=email,
            password=password,
            username=username,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''
    email       (로그인 시 필요)
    username    (웹 사이트에서 닉네임으로 사용됨)
    password    (로그인 시 필요)
    phone_number(필수 입력 사항)
    address     (테이블 하나 추가하는 것으로)
    profile_pic (선택 사항, 없으면 기본 이미지로 설정)
    is_trainer  (True or False)
    career      (선택 입력 사항)
    '''
    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=30,
        unique=True
    )
    phone_number = models.CharField(
        verbose_name=_('Phone number'),
        max_length=11,
        unique=True
    )
    profile_pic = models.ImageField(
        verbose_name=_('Profile picture'),
        blank=True,
        null=True,
    )
    is_trainer = models.BooleanField(default=False)
    career = models.TextField()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-pk',)

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser

    get_full_name.short_description = _('Full name')
