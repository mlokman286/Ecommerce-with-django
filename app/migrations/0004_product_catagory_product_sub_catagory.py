# Generated by Django 4.2.7 on 2023-11-20 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.catagory'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_catagory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.sub_catagory'),
        ),
    ]
