from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from services import create_stripe_price, create_stripe_session, create_stripe_product
from users.models import CustomUser
from users.serializers import UserSerializer

from .models import Payment
from .serializers import PaymentSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (
        AllowAny,
    )  # API регистрации доступен для всех, остальные API только для зарегистрированных

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
    filterset_fields = ["paid_course", "paid_lesson", "payment_method"]
    ordering_fields = ["payment_date"]

class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)

        price = create_stripe_price(payment.amount)
        print(self.request)
        if payment.paid_course:
            product = create_stripe_product(product=payment.paid_course.name)

        session_id, url = create_stripe_session(price)
        payment.session_id = session_id
        if payment.paid_course:
            payment.paid_course = product

        payment.link = url
        payment.save()