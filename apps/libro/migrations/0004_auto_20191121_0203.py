# Generated by Django 2.2.7 on 2019-11-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_auto_20191121_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor_id',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor_id',
            field=models.ManyToManyField(to='libro.Autor'),
        ),
    ]
