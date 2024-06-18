from django.urls import path
from .views import contactUs

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('contactUs', contactUs),

]
