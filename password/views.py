from rest_framework.views import APIView
from .serializer import PasswordSerializer
import random
from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View

# Create your views here.


class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": "ok"}, status=200)


class PasswordGenerator(APIView):
    serializer_class = PasswordSerializer

    def post(self, request):
        serializer_class = self.serializer_class(data=request.data)
        if serializer_class.is_valid():
            length = serializer_class.validated_data.get("password_length")
            uppercase = serializer_class.validated_data.get("uppercase")
            numbers = serializer_class.validated_data.get("numbers")
            symbols = serializer_class.validated_data.get("symbols")

            chars = list("abcdefghijklmnopqrstuvwxyz")

            if uppercase:
                chars.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            if numbers:
                chars.extend("0123456789")
            if symbols:
                chars.extend(" +#$%^&*()@!")

            password_choice = "".join(random.choice(chars) for i in range(length))

            return Response({"The password generated is": password_choice})
        return Response(serializer_class.errors, status=400)

    def get(self, request):
        return Response({"Generate your password😊"}, status=200)
