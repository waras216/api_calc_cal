from django.db import models


class ApiAlimento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    calorias = models.FloatField()
    proteinas = models.FloatField()
    carbohidratos = models.FloatField()
    grasas = models.FloatField()

    class Meta:
        managed = False
        db_table = 'api_alimento'


class ApiRegistrocomida(models.Model):
    id = models.BigAutoField(primary_key=True)
    cantidad = models.FloatField()
    alimento = models.ForeignKey(ApiAlimento, models.DO_NOTHING)
    usuario = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_registrocomida'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DailyGoals(models.Model):
    id_goal = models.AutoField(primary_key=True)
    id_user = models.IntegerField(blank=True, null=True)
    calorias_meta = models.IntegerField(blank=True, null=True)
    carbohidratos_meta = models.IntegerField(blank=True, null=True)
    proteinas_meta = models.IntegerField(blank=True, null=True)
    grasas_meta = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_goals'


class DetailsMeals(models.Model):
    id_mdetails = models.AutoField(primary_key=True)
    id_meal = models.IntegerField(blank=True, null=True)
    id_food = models.IntegerField(blank=True, null=True)
    cantidad_gramos = models.IntegerField(blank=True, null=True)
    calorias_totales = models.IntegerField(blank=True, null=True)
    proteinas_totales = models.IntegerField(blank=True, null=True)
    grasas_totales = models.IntegerField(blank=True, null=True)
    carbohidratos_totales = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details_meals'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Favorites(models.Model):
    id_favorites = models.AutoField(primary_key=True)
    id_user = models.IntegerField(blank=True, null=True)
    id_food = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorites'


class Foods(models.Model):
    id_food = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    proteinas = models.IntegerField(blank=True, null=True)
    carbohidratos = models.IntegerField(blank=True, null=True)
    calorias = models.IntegerField(blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    grasas = models.IntegerField(blank=True, null=True)
    porcion_gramos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    imagen = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foods'


class ImagenAnalisis(models.Model):
    id_analisis = models.AutoField(primary_key=True)
    id_user = models.IntegerField(blank=True, null=True)
    image_path = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    resultado_json = models.CharField(max_length=200, blank=True, null=True)
    detectado = models.IntegerField(blank=True, null=True)
    confianza = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagen_analisis'


class Meals(models.Model):
    id_meal = models.AutoField(primary_key=True)
    id_user = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    tipo_comida = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meals'


class Planes(models.Model):
    id_plan = models.AutoField(primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    coste_iva = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planes'


class ProveedoresAuth(models.Model):
    id_proveedorauth = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores_auth'


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido_p = models.CharField(max_length=100, blank=True, null=True)
    apellido_m = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    peso = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    estatura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=40, blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    objetivo = models.CharField(max_length=200, blank=True, null=True)
    avatar_url = models.CharField(max_length=500, blank=True, null=True)
    id_proveedorauth = models.ForeignKey(ProveedoresAuth, models.DO_NOTHING, db_column='id_proveedorauth', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'