# Generated by Django 4.2.6 on 2023-10-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_addprofit_date_chat_date_payment_date_withdraw_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='date',
            new_name='replay_date',
        ),
        migrations.AddField(
            model_name='chat',
            name='message_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]