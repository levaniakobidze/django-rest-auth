# Generated by Django 5.0.1 on 2024-02-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='levan@gmail.com', max_length=254),
        ),
    ]