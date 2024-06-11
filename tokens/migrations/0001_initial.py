# Generated by Django 5.0.6 on 2024-06-11 04:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=20, unique=True)),
                ('price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('volume_24h', models.DecimalField(decimal_places=10, default=0, max_digits=30)),
                ('volume_change_24h', models.DecimalField(decimal_places=10, default=0, max_digits=20)),
                ('percent_change_1h', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('percent_change_24h', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('percent_change_7d', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('market_cap', models.DecimalField(decimal_places=10, default=0, max_digits=30)),
                ('market_cap_dominance', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('fully_diluted_market_cap', models.DecimalField(decimal_places=10, default=0, max_digits=30)),
                ('last_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=10, default=0, max_digits=20)),
                ('acquired_at', models.DateTimeField(auto_now_add=True)),
                ('last_online', models.DateTimeField(auto_now=True)),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tokens.token')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'token')},
            },
        ),
    ]
