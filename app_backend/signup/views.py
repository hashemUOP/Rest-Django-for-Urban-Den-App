from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def register_user(request):
    data = request.data
    print("Received data:", data)
    return Response({"message": "User registered!"})
