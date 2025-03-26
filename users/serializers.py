from rest_framework.serializers import ModelSerializer
from users.models import Payment, CustomUser


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'payment_date', 'paid_course', 'paid_lesson', 'amount', 'payment_method']

class UserSerializer(ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'phone', 'tg_nick', 'city', 'avatar', 'payments']