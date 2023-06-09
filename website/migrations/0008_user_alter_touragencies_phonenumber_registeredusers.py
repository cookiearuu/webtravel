# Generated by Django 4.0.1 on 2023-05-26 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_rename_categoryid_category_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='touragencies',
            name='phonenumber',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.CreateModel(
            name='registeredusers',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('card_number', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=4)),
                ('expiration_date', models.DateField()),
                ('email', models.ForeignKey(default='cookiearu@gmail.com', on_delete=django.db.models.deletion.CASCADE, to='website.user')),
                ('tour', models.ForeignKey(default=22, on_delete=django.db.models.deletion.CASCADE, to='website.tours')),
            ],
        ),
    ]
