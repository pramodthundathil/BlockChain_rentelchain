# Generated by Django 3.2.14 on 2023-04-13 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landdeals', '0002_contarct_personaldetailslandloard_personaldetailsleaser_rentelapprovel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract_block2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlockIndex', models.CharField(max_length=20)),
                ('BlockTimeStrap', models.DateTimeField(auto_now_add=True)),
                ('BlockData', models.CharField(max_length=255)),
                ('previous_hash', models.CharField(max_length=255)),
                ('Blockhash', models.CharField(max_length=255)),
                ('BlockLink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landdeals.contarct')),
            ],
        ),
        migrations.CreateModel(
            name='Contract_Block1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlockIndex', models.CharField(max_length=20)),
                ('BlockTimeStrap', models.DateTimeField(auto_now_add=True)),
                ('BlockData', models.CharField(max_length=255)),
                ('previous_hash_leaser', models.CharField(max_length=255)),
                ('previous_hash_landlaord', models.CharField(max_length=255)),
                ('Blockhash', models.CharField(max_length=255)),
                ('BlockLink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landdeals.contarct')),
            ],
        ),
    ]
