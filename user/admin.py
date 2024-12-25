from django.contrib import admin
from user import models as M_USER

admin.site.register([
    M_USER.User,
    M_USER.Profilepic,
    M_USER.Coverphoto,
])