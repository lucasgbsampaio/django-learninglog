from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls','users'),namespace='users')),
    path('', include(('learning_logs.urls','learning_logs'),namespace='learning_logs')),

]
