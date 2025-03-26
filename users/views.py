from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payment
from .serializers import PaymentSerializer
from users.models import CustomUser
from users.serializers import UserSerializer
from rest_framework.permissions import AllowAny

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny, )


    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.all()

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['paid_course', 'paid_lesson', 'payment_method']
    ordering_fields = ['payment_date']