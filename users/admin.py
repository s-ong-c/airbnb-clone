from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )


"""
1. django는 powerful ORM 기능을 갖고 있다.

2. @admin.register(models.User)는 decorator라 부르고 반드시 class 위에 적어야 한다.
@admin.register(models.User) === admin.site.register(models.User, CustomUserAdmin) 과 같다
3. inheritance 상속의 개념을 잘 숙지하자.
강사님이 쉽게 설명해준 내용 ex>
class dog():
    leg = 4
    eyes = 2

class bulldog(dog):


(*easy)

4. # config 폴더 안에 setting.py 파일 최하단에 아래 코드를 추가해야 장고가 기본적으로 제공하는 모델을 확장할 수 있다.
AUTH_USER_MODEL = "users.User"
"""
