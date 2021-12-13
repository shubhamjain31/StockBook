from django.contrib.auth.base_user import BaseUserManager

# -------------------------------------------------------- For email -------------------------------------------------

# class UserManager(BaseUserManager):
#   use_in_migrations = True

#   def create_user(self, email, password=None, **extra_fields):
#     if not email:
#       raise ValueError('Email is required')

#     email = self.normalize_email(email)
#     user = self.model(email = email, **extra_fields)
#     user.set_password(password)
#     user.save(using = self._db)
#     return user

#   def create_superuser(self, email, password=None, **extra_fields):
#     extra_fields.setdefault("is_staff", True)
#     extra_fields.setdefault("is_superuser", True)
#     extra_fields.setdefault("is_active", True)

#     if extra_fields.get('is_staff') is not True:
#       raise ValueError('Super user must have is_staff true')

#     return self.create_user(email, password, **extra_fields)


# -------------------------------------------------------- For username -------------------------------------------------
class UserManager(BaseUserManager):
  use_in_migrations = True

  def create_user(self, username, password=None, **extra_fields):
    if not username:
      raise ValueError('Username is required')
      
    username  = self.model.normalize_username(username)
    user      = self.model(username = username, **extra_fields)

    user.set_password(password)
    user.save(using = self._db)
    return user

  def create_superuser(self, username, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)
    extra_fields.setdefault("is_active", True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Super user must have is_staff true')

    return self.create_user(username, password, **extra_fields)