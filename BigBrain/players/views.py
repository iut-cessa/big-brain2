from rest_framework.generics import CreateAPIView
from .serializers import PlayerSerializer


class NewUser(CreateAPIView):
    serializer_class = PlayerSerializer
