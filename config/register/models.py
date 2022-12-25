from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name='Admin', number=None, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not number:
            raise ValueError("User must have an number")

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            number=number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, number, password=None):
        user = self.create_user(
                email=email,
                number=number,
                password=password,
        )
        user.is_admin=True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    number = models.CharField(max_length=10, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = MyUserManager()
    
    @property
    def is_staff(self):
        return self.is_admin
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['number',]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
