# Generated by Django 4.1.2 on 2022-12-02 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Anime', '0003_rename_bnguimi_id_anime_banguimi_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='banguimi_id',
            new_name='bangumi_id',
        ),
    ]
