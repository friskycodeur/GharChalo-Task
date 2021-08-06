# Generated by Django 3.2.6 on 2021-08-06 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'size',
                'verbose_name_plural': 'sizes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('type', models.CharField(choices=[('round', 'Round'), ('square', 'Square')], default='round', max_length=7)),
                ('price', models.PositiveIntegerField()),
                ('topping', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('size', models.ManyToManyField(related_name='pizzas', to='pizzas.Size')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
