# Generated by Django 4.2.6 on 2023-10-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_user_plan_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='addprofit',
            name='referral_profit',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
