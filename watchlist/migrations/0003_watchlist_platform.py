# Generated by Django 4.0.6 on 2022-07-15 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0002_streamplatform_watchlist_delete_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='watchlist.streamplatform'),
            preserve_default=False,
        ),
    ]
