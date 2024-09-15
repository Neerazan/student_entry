# Generated by Django 5.1.1 on 2024-09-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.CharField(choices=[('CS', 'Computer Science'), ('MATH', 'Mathematics'), ('BIO', 'Biology'), ('CHEM', 'Chemistry'), ('PHY', 'Physics')], default='CS', max_length=4),
        ),
    ]
