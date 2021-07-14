# Generated by Django 3.2.4 on 2021-07-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_myuser_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='auth_token',
            field=models.CharField(default='0000', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
