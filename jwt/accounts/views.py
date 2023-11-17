from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mypage_view(request):
    return Response({"message": f"반갑습니다, {request.user.email}님!"})

# accounts/views.py
from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class CustomRegisterView(RegisterView):
    def get_response_data(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
