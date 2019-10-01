# Generated by Django 2.2.3 on 2019-09-24 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_client_hotel_reservation_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('categorie', models.CharField(max_length=100)),
                ('disponibilite', models.BooleanField(default=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Hotel')),
            ],
        ),
    ]