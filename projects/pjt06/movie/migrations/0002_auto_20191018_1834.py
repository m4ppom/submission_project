# Generated by Django 2.2.6 on 2019-10-18 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='movie.Movie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_score',
            field=models.CharField(max_length=200),
        ),
    ]