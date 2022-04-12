# Generated by Django 4.0.3 on 2022-04-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('pub_com', models.CharField(max_length=200)),
                ('descri', models.TextField(max_length=400)),
                ('quant', models.IntegerField()),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
