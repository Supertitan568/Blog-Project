# Generated by Django 5.0.6 on 2024-06-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_text_comment_body_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='asdf', max_length=1000),
            preserve_default=False,
        ),
    ]
