from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# 안에 내용을 추가하지 않고 명시적으로 만들어서 사용하겠다.
# 유저는 customising된 유저를 사용(default 유저를 사용하더라도 장고에서는 *강력히* 커스텀 유저를 사용하라고 권장)
class User(AbstractUser):
    pass

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    # Todo 사용할때마다 terminal에 찍히게 해서 내가 확인하려고 작성
    def __str__(self):
        return self.title