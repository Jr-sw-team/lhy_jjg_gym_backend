# from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.db import models
# from django.utils import timezone
# from django.utils.translation import ugettext_lazy as _
#
#
# class UserManager(BaseUserManager):
#     def create_user(self):
#         pass
#     def create_superuser(self):
#         pass
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     '''
#     email       (로그인 시 필요)
#     password    (로그인 시 필요)
#     tell        (필수 입력 사항)
#     address     (필수 입력 사항)
#     profile_pic (선택 사항, 없으면 기본 이미지로 설정)
#     is_trainer  (True or False)
#     career      (선택 입력 사항)
#     '''
#     email = models.EmailField(
#         verbose_name=_('Email address'),
#         max_length=255,
#         unique=True,
#     )
#     username = models.CharField(
#         verbose_name=_('Username'),
#         max_length=30,
#         unique=True
#     )
#     date_joined = models.DateTimeField(
#         verbose_name=_('Date joined'),
#         default=timezone.now
#     )
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['password', ]
#
#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
#         ordering = ('-date_joined',)
#
#     def __str__(self):
#         return self.username
#
#     def get_full_name(self):
#         return self.username
#
#     def get_short_name(self):
#         return self.username
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All superusers are staff
#         return self.is_superuser
#
#     get_full_name.short_description = _('Full name')