from rest_framework import generics , permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, WorkSerializer, ArtistSerializer
from django.contrib.auth.models import User
from .models import Work, Artist

class RegisterAPI(generics.CreateAPIView):
    permisssion_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class WorkApiView(APIView):
    permission = [permissions.IsAuthenticated]

    def get(self, request):
        artist = self.request.GET.get("artist")
        work_type = self.request.GET.get("work_type")

        if artist:
            queryset = Artist.objects.filter(name = artist)
            serializer = ArtistSerializer(queryset, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

        if work_type:
            queryset = Work.objects.filter(work_type = work_type)
            serializer = WorkSerializer(queryset, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

        else:
            work = Work.objects.all()
            serializer = WorkSerializer(work, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)





    # Create your views here.
