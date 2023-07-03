# Generated by Django 4.2.2 on 2023-06-28 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0003_post_blog_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_blog',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cmsapp.user'),
            preserve_default=False,
        ),
    ]
