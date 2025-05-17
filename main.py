import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_django1.settings")

django.setup()


from user_app.models import User, Group

#new_group = Group(name="Вчителі")
#new_group.save()


#user = User.objects.create(username="admin",
#                           email='admin@gmail.com',
#                           role='admin')

print(User.objects.all())