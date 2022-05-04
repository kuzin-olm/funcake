# Generated by Django 3.2.12 on 2022-05-04 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipelayer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipelayer',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='layers', to='recipes.recipe'),
        ),
    ]
