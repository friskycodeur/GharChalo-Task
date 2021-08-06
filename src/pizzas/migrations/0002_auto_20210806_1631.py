# Generated by Django 3.2.6 on 2021-08-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='created',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='price',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='user',
        ),
        migrations.RemoveField(
            model_name='size',
            name='slug',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='topping',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='type',
            field=models.CharField(choices=[('1', 'Round'), ('2', 'Square')], default='round', max_length=7),
        ),
        migrations.AddField(
            model_name='pizza',
            name='topping',
            field=models.ManyToManyField(related_name='pizzas', to='pizzas.Topping'),
        ),
    ]
