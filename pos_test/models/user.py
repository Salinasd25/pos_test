# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.validators import UnicodeUsernameValidator
# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     UserManager,
#     PermissionsMixin,
#     Permission,
#     Group,
# )


# class UserManager(UserManager):

#     def _create_user(self, email, password, **extra_fields):
#         """
#         Crear y guardar un usuario con el correo electrónico y
#         la contraseña proporcionados.
#         """
#         if not email:
#             raise ValueError(_('The given email must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         extra_fields.setdefault('is_active', True)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(
#             self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True.'))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True.'))
#         if extra_fields.get('is_active') is not True:
#             raise ValueError(_('Superuser must have is_active=True.'))

#         return self._create_user(email, password, **extra_fields)

#     def normalize_email(self, email):
#         email = super().normalize_email(email)
#         return email.lower()


# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(
#         max_length=150,
#         unique=True,
#         help_text=_(
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
#         ),
#         validators=[UnicodeUsernameValidator()],
#         error_messages={
#             "unique": _("A user with that username already exists."),
#         },
#     )
#     name = models.CharField(
#         verbose_name='name',
#         max_length=255,
#         help_text='Nombre',
#     )
#     last_name = models.CharField(
#         verbose_name='last name',
#         max_length=255,
#         help_text='Apellido',
#         null=True,
#         blank=True
#     )
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         null=True,
#         help_text='Correo electronico',
#     )
#     is_active = models.BooleanField(
#         default=True
#     )
#     is_staff = models.BooleanField(
#         'staff',
#         default=False
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         editable=False,
#         help_text='Fecha de creación del objeto'
#     )
#     updated_at = models.DateTimeField(
#         auto_now=True,
#         help_text='Fecha de actualización del objeto'
#     )
#     deleted_at = models.DateTimeField(
#         auto_now=False,
#         auto_now_add=False,
#         null=True,
#         help_text='Fecha de actualización del objeto'
#         'Anule la selección de esto en lugar de eliminar las cuentas.'
#     )
#     created_by = models.ForeignKey(
#         'self',
#         on_delete=models.CASCADE,
#         related_name='+',
#         null=True,
#         help_text='Usuario que creo el objeto'
#     )
#     updated_by = models.ForeignKey(
#         'self',
#         on_delete=models.CASCADE,
#         related_name='+',
#         null=True,
#         help_text='Usuario que modifico el objeto'
#     )
#     deleted_by = models.ForeignKey(
#         'self',
#         on_delete=models.CASCADE,
#         related_name='+',
#         null=True,
#         help_text='Usuario que elimino el objeto'
#     )
#     objects = UserManager()


#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
#         db_table = 'users'
#         ordering = ('-id',)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['name', 'last_name']

#     def __str__(self):
#         return f'{self.name} {self.last_name}'

#     @property
#     def full_name(self):
#         return self.name+" "+self.last_name

#     @property
#     def permissions(self):
#         data = []
#         permissions = Permission.objects.filter(user=self.pk).all()
#         for value in permissions:
#             data.append(
#                 {
#                     "id": value.id,
#                     "name": value.name,
#                     "codename": value.codename,
#                 }
#             )
#         return data

#     @property
#     def not_permissions(self):
#         data_all = []
#         permissions = Permission.objects
#         for data in permissions.all():
#             group = Group.objects.filter(
#                 user__id=self.pk,
#                 permissions__id=data.pk
#             ).first()
#             user_permission = permissions.filter(pk=data.pk, user=self.pk)
#             if not group and not user_permission:
#                 data_all.append(
#                     {
#                         "name": data.name,
#                         "codename": data.codename,
#                     }
#                 )
#         return data_all


#     @property
#     def short_name(self):
#         name = self.name.split()[0]
#         last_name = self.last_name.split()[0] if self.last_name else ""
#         return name+" "+last_name