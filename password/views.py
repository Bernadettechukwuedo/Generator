from rest_framework.views import APIView
from .serializer import PasswordSerializer
import random
from rest_framework.response import Response

# Create your views here.


class PasswordGenerator(APIView):
    serializer_class = PasswordSerializer

    def post(self, request):
        serializer_class = PasswordSerializer(data=request.data)
        if serializer_class.is_valid():
            length = serializer_class.validated_data.get("password_length")
            uppercase = serializer_class.validated_data.get("uppercase")
            number = serializer_class.validated_data.get("number")
            symbols = serializer_class.validated_data.get("symbols")

            chars = list("abcdefghijklmnopqrstuvwxyz")

            if uppercase:
                chars.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            if number:
                chars.extend("0123456789")
            if symbols:
                chars.extend(" +#$%^&*()@!")

            password_choice = ""

            for i in range(length):
                password_choice += random.choice(chars)

            return Response(password_choice)
