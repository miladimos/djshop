import datetime
import random
import string
import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from apps.core.models import BaseModel
from apps.payments.models import IrBank


class Country(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    flag = models.CharField(max_length=255)


class Province(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)


class City(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)


class ActivationCode(BaseModel):
    code = models.CharField(max_length=50, unique=True)
    expired_at = models.DateTimeField(default=datetime.timedelta(minutes=3))


class User(AbstractUser):
    # mobile = models.CharField(null=True, blank=True,
    #                           unique=True, max_length=11)
    # mobile_verified = models.BooleanField(default=False)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['mobile']

    # objects = UserManager()

    def __str__(self):
        return self.username


class UserProfile(BaseModel):
    # province, city, instagram, telegram
    class GenderChoices(models.TextChoices):
        male = 'male'
        female = 'female'
        unknown = 'unknown'
        # __empty__ = '(Unknown)'

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        upload_to='avatars/', blank=True, null=True, default='default_avatar.jpg')
    gender = models.CharField(
        max_length=8, choices=GenderChoices.choices, default=GenderChoices.unknown)
    bio = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(verbose_name=_(
        'تاریخ تولد'), null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username

    def get_avatar_image_path(self, filename):
        return f'accounts/avatars/{self.pk}/profile_image.jpg'

    def get_default_avatar_image():
        return 'accounts/avatars/default_avatar.jpg'


class UserMeta(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)

    last_login_at = models.DateTimeField(null=True, blank=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    last_logout_at = models.DateTimeField(null=True, blank=True)
    last_login_agent = models.TextField(null=True, blank=True)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    email_changed_at = models.DateTimeField(null=True, blank=True)
    mobile_changed_at = models.DateTimeField(null=True, blank=True)
    mobile_verified_at = models.DateTimeField(null=True, blank=True)
    username_changed_at = models.DateTimeField(null=True, blank=True)
    password_changed_at = models.DateTimeField(null=True, blank=True)
    is_banned = models.BooleanField(default=False)
    banned_at = models.DateTimeField(null=True, blank=True)
    unbanned_at = models.DateTimeField(null=True, blank=True)


class Address(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("کاربر"))
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, related_name='province', verbose_name=_("کاربر"))
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='city', verbose_name=_("کاربر"))
    title = models.CharField(max_length=150, verbose_name=_('عنوان'))
    address = models.TextField(verbose_name=_('آدرس'))
    # zip_code = models.CharField(max_length=50, verbose_name=_('کد پستی'))
    default = models.BooleanField(default=False)

    # map , receiver_self, receiver_name,
    # receiver_mobile, last_used_at


class UserBank(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("کاربر"))
    bank = models.ForeignKey(
        IrBank, on_delete=models.CASCADE, verbose_name=_("بانک"))
    title = models.CharField(max_length=150, verbose_name=_('عنوان'))
    shaba = models.CharField(max_length=250, verbose_name=_('شبا'))
    account_number = models.CharField(
        max_length=250, verbose_name=_('شماره حساب'))

    class Meta:
        verbose_name = _('بانک کاربر')
        verbose_name_plural = _('بانک کاربر ها')


class Wallet(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField(
        verbose_name=_('موجودی'), default=0)

    class Meta:
        verbose_name = _('کیف پول')
        verbose_name_plural = _('کیف پول ها')


class AccountDeleteRequest(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("کاربر"))
    approved_at = models.DateTimeField(null=True, blank=True)
    complete_at = models.DateTimeField(null=True, blank=True)


class OtpRequest(models.Model):
    class OtpChannel(models.TextChoices):
        ANDROID = 'a', _("android")
        IOS = 'i', _("ios")
        WEB = 'w', _("web")

    request_id = models.UUIDField(default=uuid.uuid4, editable=False)
    channel = models.CharField(
        _('channel'), max_length=20, choices=OtpChannel.choices)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=4, null=True)
    valid_form = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(seconds=120))
    receipt_id = models.CharField(max_length=255, null=True)

    def generate_otp(self):
        self.password = self._random_password()
        self.valid_until = timezone.now() + timezone.timedelta(seconds=120)

    def _random_password(self):
        rand = random.SystemRandom()
        digits = rand.choice(string.digits, k=4)
        return ''.join(digits)

    class Meta:
        verbose_name = _('Otp Request')
        verbose_name_plural = _('Otp Requests')
