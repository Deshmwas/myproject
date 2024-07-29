
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import EventViewSet
# from .views import EventViewSet, register, user_login

# router = DefaultRouter()
# router.register(r'events', EventViewSet)


# urlpatterns = [
#     path('', include(router.urls)),
#      path('register/', register, name='register'),
#     path('login/', user_login, name='login'),
    
# ]




# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import EventViewSet, register, user_login

# router = DefaultRouter()
# router.register(r'events', EventViewSet)
# router.register(r'users', UserViewSet, basename='users') # type: ignore

# urlpatterns = [
#     path('', include(router.urls)),
    
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, UserViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]



