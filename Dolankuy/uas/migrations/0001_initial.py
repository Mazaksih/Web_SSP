# Generated by Django 4.2.2 on 2023-06-15 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('ket', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodebrg', models.CharField(max_length=8)),
                ('nama', models.CharField(max_length=50)),
                ('stok', models.IntegerField()),
                ('harga', models.BigIntegerField()),
                ('link_gbr', models.CharField(blank=True, max_length=150)),
                ('waktu_posting', models.DateTimeField(auto_now_add=True)),
                ('jenis_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='uas.jenis')),
            ],
        ),
    ]
