# Generated by Django 4.1.6 on 2023-02-24 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_userinformation_geschlecht_userinformation_notiz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='email_after_1',
            field=models.BooleanField(default=False),
        ),
    ]