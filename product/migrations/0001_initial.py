# Generated by Django 2.1.1 on 2018-10-11 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, help_text='해당 데이터가 작성된 날짜')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='해당 데이터가 수정된 날짜')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='FoodOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, help_text='해당 데이터가 작성된 날짜')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='해당 데이터가 수정된 날짜')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('related_food',
                 models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Food')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderedFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, help_text='해당 데이터가 작성된 날짜')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='해당 데이터가 수정된 날짜')),
                ('owned_order',
                 models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('required_food',
                 models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Food')),
                ('required_options', models.ManyToManyField(to='product.FoodOption')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('reg_date', models.DateTimeField(auto_now_add=True, help_text='해당 데이터가 작성된 날짜')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='해당 데이터가 수정된 날짜')),
                ('owner_name', models.CharField(default='no_name', help_text='사장님 이름', max_length=50)),
                ('descriptions', models.CharField(default='no contents', help_text='식당 간략하게 소개 ', max_length=200)),
                ('id', models.BigAutoField(default='', primary_key=True, serialize=False, verbose_name='식당의 고유 id')),
                ('name', models.CharField(max_length=100, verbose_name='식당 이름 ')),
                ('restaurant_owner', models.CharField(default='no_name', max_length=100, verbose_name='식당 사장님 이름 ')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='food',
            name='food_owned_restaurant',
            field=models.ForeignKey(default='', help_text='음식(메뉴)을 작성한 식당 고유번호',
                                    on_delete=django.db.models.deletion.CASCADE, to='product.Restaurant'),
        ),
    ]
