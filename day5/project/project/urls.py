"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from home.views import go_home
# from employees.views import go_emp
# from contact_us.views import go_contact
# from about_us.views import go_about
import home
import contact_us
import about_us
import employees

urlpatterns = [
    path('admin/', admin.site.urls),

    path('contact_us/',include('contact_us.urls')),
    path('about_us/',include('about_us.urls')),
    path('employees/',include('employees.urls')),
    path('home/',include('home.urls')),

]






# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('home/', go_home,name='home'),
#     # path('employees/', go_emp,name='emp'),
#     # path('contact_us/', go_contact,name='contact'),
#     # path('about/', go_about,name='about'),
#     #path('home/',include('home.urls')),
#     path('contact_us/',include('contact_us.urls')),
#     # path('employees/', include('employees.urls')),
#     # path('about_us/', include('about_us.urls')),

# ]

