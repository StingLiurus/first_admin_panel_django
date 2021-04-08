from django.db import models
from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField

#class AuthGroup(models.Model):
#    name = models.CharField(unique=True, max_length=150)

#    class Meta:
#        managed = False
#        db_table = 'auth_group'


#class AuthGroupPermissions(models.Model):
#    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#    class Meta:
#        managed = False
#        db_table = 'auth_group_permissions'
#        unique_together = (('group', 'permission'),)


#class AuthPermission(models.Model):
#    name = models.CharField(max_length=255)
#    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#    codename = models.CharField(max_length=100)

#    class Meta:
#        managed = False
#        db_table = 'auth_permission'
#        unique_together = (('content_type', 'codename'),)


#class AuthUser(models.Model):
#    password = models.CharField(max_length=128)
#    last_login = models.DateTimeField(blank=True, null=True)
#    is_superuser = models.IntegerField()
#    username = models.CharField(unique=True, max_length=150)
#    first_name = models.CharField(max_length=150)
#    last_name = models.CharField(max_length=150)
#    email = models.CharField(max_length=254)
#    is_staff = models.IntegerField()
#    is_active = models.IntegerField()
#    date_joined = models.DateTimeField()

#    class Meta:
#        managed = False
#        db_table = 'auth_user'


#class AuthUserGroups(models.Model):
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#    class Meta:
#        managed = False
#        db_table = 'auth_user_groups'
#        unique_together = (('user', 'group'),)


#class AuthUserUserPermissions(models.Model):
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#    class Meta:
#        managed = False
#        db_table = 'auth_user_user_permissions'
#        unique_together = (('user', 'permission'),)


#class DjangoAdminLog(models.Model):
#    action_time = models.DateTimeField()
#    object_id = models.TextField(blank=True, null=True)
#    object_repr = models.CharField(max_length=200)
#    action_flag = models.PositiveSmallIntegerField()
#    change_message = models.TextField()
#    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#    class Meta:
#        managed = False
#        db_table = 'django_admin_log'


#class DjangoContentType(models.Model):
#    app_label = models.CharField(max_length=100)
#    model = models.CharField(max_length=100)

#    class Meta:
#        managed = False
#        db_table = 'django_content_type'
#        unique_together = (('app_label', 'model'),)


#class DjangoMigrations(models.Model):
#    app = models.CharField(max_length=255)
#    name = models.CharField(max_length=255)
#    applied = models.DateTimeField()

#    class Meta:
#        managed = False
#        db_table = 'django_migrations'


#class DjangoSession(models.Model):
#    session_key = models.CharField(primary_key=True, max_length=40)
#    session_data = models.TextField()
#    expire_date = models.DateTimeField()

#    class Meta:
#        managed = False
#        db_table = 'django_session'


class Issue(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    title = models.TextField(blank=True, null=True)
    link = models.FileField(upload_to='documents/')
    type = models.CharField(max_length=7, blank=True, null=True)
    dep_id = models.IntegerField(blank=True, null=True)
    people_id = models.CharField(max_length=20, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue'

    def __str__(self):
        return self.title

class NewsEvents(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    date = models.DateField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    shorttext = models.TextField(blank=True, null=True)
    text = RichTextUploadingField()
    type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_events'

    def __str__(self):
        return self.title

class People(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    phone = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    post = models.TextField(blank=True, null=True)
    name_link = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=3, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    hist = models.IntegerField(blank=True, null=True)
    iss = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'people'

    def __str__(self):
        return self.name

class Requests(models.Model):
    id = models.SmallAutoField(primary_key=True)
    dept = models.TextField(blank=True, null=True)
    chamber = models.SmallIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    date = models.DateField()
    text = models.TextField()
    label = models.IntegerField(blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    idrand = models.IntegerField()
    dateok = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requests'

    def __str__(self):
        return self.text

class SiteFace(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    paramname = models.TextField(blank=True, null=True)
    paramvalue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_face'

    def __str__(self):
        return self.paramname

class SiteFaceEn(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    paramname = models.TextField(blank=True, null=True)
    paramvalue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_face_en'

    def __str__(self):
        return self.paramname

class Structure(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    title = models.CharField(max_length=80, blank=True, null=True)
    name_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    dep_id = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'structure'

    def __str__(self):
        return self.title

#class Towns(models.Model):
#    lat = models.FloatField(blank=True, null=True)
#    lon = models.FloatField(blank=True, null=True)
#    name = models.CharField(db_column='Name', max_length=1, blank=True, null=True)
#    regname = models.CharField(db_column='RegName', max_length=1, blank=True, null=True)
#    size = models.PositiveIntegerField(blank=True, null=True)
#    regnum = models.IntegerField()

#    class Meta:
#        managed = False
#        db_table = 'towns'


class Vacanc(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    vacancy = models.TextField(blank=True, null=True)
    speciality = models.TextField(blank=True, null=True)
    pay = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacanc'

    def __str__(self):
        return self.vacancy

