from rest_framework import serializers
from .models import Person, Product, ProductFeature


# -------------------------------------------------------------------------
# class PersonSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=20)
#     family = serializers.CharField(max_length=30)
#     email = serializers.EmailField(max_length=30)
#     age = serializers.IntegerField()
#     username = serializers.CharField(max_length=30)
#     password = serializers.CharField(max_length=60)
# -------------------------------------------------------------------------
class PersonSerializer(serializers.ModelSerializer):
    # اینجوری اینم میخواد بره و درج بشه و این اشتباهه
    # پس بهتر توی متد create که پایین نوشتیم بریم این رو پاک کنیم از دیتایی که آنپک شده
    # اگر write_olny رو true کنیم کاربر باید پر کنه ولی نمایش داده نمیشه
    re_password = serializers.CharField(max_length=60, write_only=True)

    class Meta:
        model = Person
        fields = '__all__'
        # fields = ['name','family','age','email']
        # exclude = ['password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # میشه دوباره نویسی کردن متد create
    def create(self, validated_data):
        # اینو حذف کن و بقیه رو درج کن
        del validated_data['re_password']
        # داده ای که میرسه رو اینجا onpack میکنیم
        return Person.objects.create(**validated_data)

    # validate field
    def validate_username(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("نام کاربری نمیتواند کمتر از 6 کاراتر باشد")
        return value

    # validate data
    def validate(self, data):
        if data['password'] != data['re_password']:
            raise serializers.ValidationError('رمز عبور و تکرار آن یکسان نمی باشد')
        if len(data['name']) < 3:
            raise serializers.ValidationError('نام نمیتواند کمتر از 3 کاراتر باشد')
        return data


# -------------------------------------------------------------------------
def price_validate(value):
    if int(value) < 3000:
        raise serializers.ValidationError('قیمت نباید کمتر از 3000 باشد')


class ProductSerializer(serializers.ModelSerializer):
    # داری نمایش میدی این features هارو هم بیار

    features = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'features')
        extra_kwargs = {
            'price': {'validators': (price_validate,)}
        }

    def get_features(self, obj):
        res = obj.features.all()
        return ProductFeatureSerializer(instance=res, many=True).data


class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = '__all__'
