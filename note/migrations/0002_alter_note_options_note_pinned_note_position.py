# Generated by Django 5.0.6 on 2024-07-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-pinned', 'position', 'created_at']},
        ),
        migrations.AddField(
            model_name='note',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='note',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
