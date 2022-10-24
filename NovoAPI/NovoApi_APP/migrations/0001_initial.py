# Generated by Django 4.1.1 on 2022-10-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('revision', models.IntegerField()),
            ],
            options={
                'db_table': 'boards',
            },
        ),
        migrations.CreateModel(
            name='bom_parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('designators', models.CharField(max_length=2000)),
                ('bom_id', models.PositiveIntegerField()),
                ('part_id', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'bom_parts',
            },
        ),
        migrations.CreateModel(
            name='bom_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'bom_types',
            },
        ),
        migrations.CreateModel(
            name='boms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('board_id', models.PositiveIntegerField()),
                ('type_id', models.PositiveIntegerField()),
                ('uuid', models.CharField(max_length=32)),
                ('variant', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'boms',
            },
        ),
        migrations.CreateModel(
            name='manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'manufacturers',
            },
        ),
        migrations.CreateModel(
            name='part_purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_code', models.CharField(max_length=50)),
                ('manufacturers_code', models.CharField(max_length=50)),
                ('manufacturers_id', models.PositiveIntegerField()),
                ('supplier_id', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'part_purchase',
            },
        ),
        migrations.CreateModel(
            name='parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('uuid', models.CharField(max_length=40)),
                ('family', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('ns_code', models.CharField(max_length=14)),
                ('ns_type', models.CharField(max_length=10)),
                ('ns_rating', models.CharField(max_length=50)),
                ('ns_status', models.CharField(max_length=100)),
                ('ns_docs', models.CharField(max_length=20)),
                ('lifecycle', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'parts',
            },
        ),
        migrations.CreateModel(
            name='supplier_pkg_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'supplier_pkg_type',
            },
        ),
        migrations.CreateModel(
            name='supplier_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_time', models.IntegerField()),
                ('stock', models.PositiveIntegerField()),
                ('code', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('updated_on', models.DateTimeField()),
                ('part_id', models.IntegerField()),
                ('pkg_type_id', models.IntegerField(blank=True, default=1, null=True)),
                ('supplier_id', models.IntegerField(blank=True, default=2, null=True)),
            ],
            options={
                'db_table': 'supplier_stock',
            },
        ),
        migrations.CreateModel(
            name='suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'suppliers',
            },
        ),
    ]
