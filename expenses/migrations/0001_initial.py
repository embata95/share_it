# Generated by Django 4.2.2 on 2023-07-24 23:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Expense",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "related_date",
                    models.DateField(
                        help_text="Date that the expense is accounted to."
                    ),
                ),
                ("value", models.DecimalField(decimal_places=2, max_digits=6)),
                ("comment", models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ExpenseType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=15, unique=True)),
                (
                    "position",
                    models.IntegerField(
                        help_text="Column position in grouped reports.", unique=True
                    ),
                ),
            ],
        ),
    ]