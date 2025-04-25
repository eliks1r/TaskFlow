from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Промежуточная модель для Many-to-Many связи
class CustomUserGroup(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'group']  # Уникальность для каждой пары (пользователь, группа)

    def __str__(self):
        return f"{self.user} - {self.group}"

# Кастомная модель пользователя
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    # Связь Many-to-Many с группами через промежуточную модель
    groups = models.ManyToManyField(Group, through=CustomUserGroup, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_set", blank=True)

    def __str__(self):
        return self.email
