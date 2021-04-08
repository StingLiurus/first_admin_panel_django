# Generated by Django 3.1.5 on 2021-02-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=160, null=True)),
                ('type', models.CharField(blank=True, max_length=7, null=True)),
                ('dep_id', models.IntegerField(blank=True, null=True)),
                ('people_id', models.CharField(blank=True, max_length=20, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'issue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewsEvents',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('shorttext', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'news_events',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('phone', models.CharField(blank=True, max_length=60, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('post', models.TextField(blank=True, null=True)),
                ('name_link', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=3, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('hist', models.IntegerField(blank=True, null=True)),
                ('iss', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'people',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plav',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('time_create', models.IntegerField(blank=True, null=True)),
                ('time_progn', models.IntegerField(blank=True, null=True)),
                ('vlazh', models.TextField(blank=True, null=True)),
                ('osadki', models.TextField(blank=True, null=True)),
                ('veter', models.TextField(blank=True, null=True)),
                ('temp', models.TextField(blank=True, null=True)),
                ('temp_priz', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=12, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'PLAV',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('dept', models.TextField(blank=True, null=True)),
                ('chamber', models.SmallIntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('label', models.IntegerField(blank=True, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('idrand', models.IntegerField()),
                ('dateok', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'requests',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiteFace',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('paramname', models.TextField(blank=True, null=True)),
                ('paramvalue', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'site_face',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiteFaceEn',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('paramname', models.TextField(blank=True, null=True)),
                ('paramvalue', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'site_face_en',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=80, null=True)),
                ('name_id', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=5, null=True)),
                ('dep_id', models.IntegerField(blank=True, null=True)),
                ('info', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'structure',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Towns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=1, null=True)),
                ('regname', models.CharField(blank=True, db_column='RegName', max_length=1, null=True)),
                ('size', models.PositiveIntegerField(blank=True, null=True)),
                ('regnum', models.IntegerField()),
            ],
            options={
                'db_table': 'towns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vacanc',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('vacancy', models.TextField(blank=True, null=True)),
                ('speciality', models.TextField(blank=True, null=True)),
                ('pay', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'vacanc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wrf',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('time_create', models.IntegerField(blank=True, null=True)),
                ('time_progn', models.IntegerField(blank=True, null=True)),
                ('vlazh', models.TextField(blank=True, null=True)),
                ('osadki', models.TextField(blank=True, null=True)),
                ('veter', models.TextField(blank=True, null=True)),
                ('temp', models.TextField(blank=True, null=True)),
                ('temp_priz', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=12, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'WRF',
                'managed': False,
            },
        ),
    ]
