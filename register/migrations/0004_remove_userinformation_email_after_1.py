# Generated by Django 4.1.6 on 2023-02-24 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_userinformation_email_after_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='email_after_1',
        ),
    ]
