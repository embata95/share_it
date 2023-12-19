# Generated by Django 4.2.2 on 2023-12-19 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("expenses", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="expensetype",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="expenses.expensetype",
            ),
        ),
        migrations.AlterField(
            model_name="expense",
            name="paid_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="expensetype",
            name="position",
            field=models.IntegerField(help_text="Column position in grouped reports."),
        ),
        migrations.AddConstraint(
            model_name="expensetype",
            constraint=models.UniqueConstraint(
                fields=("parent", "position"), name="unique_position"
            ),
        ),
        migrations.AddConstraint(
            model_name="expensetype",
            constraint=models.UniqueConstraint(
                models.F("position"),
                condition=models.Q(("parent__isnull", True)),
                name="unique_main_position",
            ),
        ),
    ]
