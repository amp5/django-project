# Generated by Django 4.1.3 on 2022-12-18 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0004_alter_post_modified_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='blogging.post'),
            preserve_default=False,
        ),
    ]
