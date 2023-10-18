# Generated by Django 4.1 on 2023-09-29 11:43

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AccountDeleteRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='1143f46e-39c5-4a48-a859-39763e2e5e50', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('complete_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActivationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='1143f46e-39c5-4a48-a859-39763e2e5e50', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('expired_at', models.DateTimeField(default=datetime.timedelta(seconds=180))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='1143f46e-39c5-4a48-a859-39763e2e5e50', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('default', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='1143f46e-39c5-4a48-a859-39763e2e5e50', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='1143f46e-39c5-4a48-a859-39763e2e5e50', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('flag', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtpRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('channel', models.CharField(choices=[('a', 'android'), ('i', 'ios'), ('w', 'web')], max_length=20, verbose_name='channel')),
                ('mobile', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=4, null=True)),
                ('valid_form', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_until', models.DateTimeField(default=datetime.datetime(2023, 9, 29, 11, 45, 17, 90834, tzinfo=datetime.timezone.utc))),
                ('receipt_id', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Otp Request',
                'verbose_name_plural': 'Otp Requests',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='1143f46e-39c5-4a48-a859-39763e2e5e50', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='1143f46e-39c5-4a48-a859-39763e2e5e50', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('shaba', models.CharField(max_length=250, verbose_name='شبا')),
                ('account_number', models.CharField(max_length=250, verbose_name='شماره حساب')),
            ],
            options={
                'verbose_name': 'بانک کاربر',
                'verbose_name_plural': 'بانک کاربر ها',
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='1143f46e-39c5-4a48-a859-39763e2e5e50', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('amount', models.PositiveBigIntegerField(default=0, verbose_name='موجودی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'کیف پول',
                'verbose_name_plural': 'کیف پول ها',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='1143f46e-39c5-4a48-a859-39763e2e5e50', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('avatar', models.ImageField(blank=True, default='default_avatar.jpg', null=True, upload_to='avatars/')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('unknown', 'Unknown')], default='unknown', max_length=8)),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='1143f46e-39c5-4a48-a859-39763e2e5e50', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('last_login_at', models.DateTimeField(blank=True, null=True)),
                ('last_login_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('last_logout_at', models.DateTimeField(blank=True, null=True)),
                ('last_login_agent', models.TextField(blank=True, null=True)),
                ('email_verified_at', models.DateTimeField(blank=True, null=True)),
                ('email_changed_at', models.DateTimeField(blank=True, null=True)),
                ('mobile_changed_at', models.DateTimeField(blank=True, null=True)),
                ('mobile_verified_at', models.DateTimeField(blank=True, null=True)),
                ('username_changed_at', models.DateTimeField(blank=True, null=True)),
                ('password_changed_at', models.DateTimeField(blank=True, null=True)),
                ('is_banned', models.BooleanField(default=False)),
                ('banned_at', models.DateTimeField(blank=True, null=True)),
                ('unbanned_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
