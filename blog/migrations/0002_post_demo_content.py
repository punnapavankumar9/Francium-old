# Generated by Django 3.1.4 on 2020-12-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='demo_content',
            field=models.TextField(default='jkgflkjsbdf sdfhsdkljfsdjf'),
            preserve_default=False,
        ),
    ]
