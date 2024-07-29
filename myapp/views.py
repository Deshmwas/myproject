
# from rest_framework import viewsets
# from .models import Event
# from .serializers import EventSerializer

# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer


# from django.contrib.auth import authenticate, login
# from rest_framework import status, viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Event, UserProfile
# from .serializers import EventSerializer, UserSerializer, UserProfileSerializer

# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer

# @api_view(['POST'])
# def register(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             UserProfile.objects.create(user=user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def user_login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
#     return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# from .models import Event
# from .serializers import EventSerializer, UserSerializer

# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer

# class UserProfileViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all() # type: ignore
#     serializer_class = UserSerializer

# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from .models import Event, UserProfile
# from .serializers import EventSerializer, UserSerializer, UserProfileSerializer

# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer

# class UserViewSet(viewsets.ViewSet):
#     @action(detail=False, methods=['post'])
#     def register(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             user_profile = UserProfile.objects.create(user=user)
#             return Response(UserProfileSerializer(user_profile).data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     @action(detail=False, methods=['post'])
#     def login(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Event, UserProfile
from .serializers import EventSerializer, UserSerializer, UserProfileSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class UserViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_profile = UserProfile.objects.create(user=user)
            return Response(UserProfileSerializer(user_profile).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


   