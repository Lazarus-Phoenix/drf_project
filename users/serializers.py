from rest_framework.serializers import ModelSerializer

from users.models import CustomUser, Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = "__all__"
        # fields = ["id", "email", "phone", "city", "avatar", "payments", "password"]
