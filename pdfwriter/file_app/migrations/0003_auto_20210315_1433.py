# Generated by Django 3.1.7 on 2021-03-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0002_remove_file_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='upload/'),
        ),
    ]
