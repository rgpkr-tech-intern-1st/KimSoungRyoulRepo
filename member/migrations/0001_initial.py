# Generated by Django 2.1.1 on 2018-10-11 05:17

import django.contrib.auth.models
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MileageHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, help_text='해당 데이터가 작성된 날짜')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='해당 데이터가 수정된 날짜')),
                ('mileage_amount', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserOwnedAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, help_text='해당 데이터가 작성된 날짜')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='해당 데이터가 수정된 날짜')),
                ('old_address', models.CharField(help_text='구 주소 체계', max_length=200)),
                ('new_address', models.CharField(help_text='신 주소 체계', max_length=200, null=True)),
                ('detail_address', models.CharField(help_text='이하 상세 주소 기입', max_length=200, null=True)),
                ('address_category',
                 models.CharField(default='최근 주소', max_length=50, verbose_name='주소의 카테고리 집, 회사 또는 최근사용한주소 ')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
            ],
            options={
                'ordering': ['username'],
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
            managers=[
                ('acc_objects', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('reg_date', models.DateTimeField(auto_now_add=True, help_text='해당 데이터가 작성된 날짜')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='해당 데이터가 수정된 날짜')),
                ('account',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False,
                                      to='member.Account')),
                ('name', models.CharField(help_text='회원의 이름', max_length=100)),
                ('phone_num', models.CharField(help_text='회원의 전화번호 - 포함 ', max_length=50)),
                ('owner_mileage_amount', models.PositiveIntegerField(default=0, help_text='적립된 마일리지 없으면 0이 디폴트 ')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='mileagehistory',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Account'),
        ),
        migrations.AddField(
            model_name='mileagehistory',
            name='related_payment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payments.Payment'),
        ),
        migrations.AddField(
            model_name='userownedaddress',
            name='owned_user_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.UserInfo'),
        ),
    ]