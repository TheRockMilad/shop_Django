from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person, Product
from .serializer import PersonSerializer, ProductSerializer, ProductFeature
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from CustomPermissions import CustomPermissionForProductFeature


# Create your views here.

@api_view(['GET', 'POST'])
def api_index(request):
    context = {
        'name': 'Milad'
    }
    return Response(context)


# =====================================================

class IndexApi(APIView):
    def get(self, request):
        context = {
            'name': 'Milad',
            'family': "Hosseini",
            'age': 32
        }
        return Response(context)

    def post(self, request):
        context = {
            'name': 'Milad',
            'family': "Hosseini",
            'age': 32
        }
        return Response(context)


# =====================================================
# Call by parameter
class IndexApi2(APIView):
    def get(self, request, name, family, age):
        context = {
            'name': name,
            'family': family,
            'age': age
        }
        return Response(context)


# =====================================================
# داده ارسال با querystring
class IndexApi3(APIView):
    def get(self, request):
        # name = request_query.params.get('name')
        # name = request.GET['name']
        name = request.GET.get('name')
        family = request.GET.get('family')
        age = request.GET.get('age')
        context = {
            'name': name,
            'family': family,
            'age': age
        }
        return Response(context)


# =====================================================
class PersonList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        people = Person.objects.all()
        # عملیات سریالایز انجام بشه
        # داده های آبجکتی تبدیل به بشن به فایل استریم ها
        ser_data = PersonSerializer(instance=people, many=True)
        # اینجا میگیم فقط دیتا رو برگردون
        return Response(data=ser_data.data)


# =====================================================
class SearchPersonById(APIView):
    def get(self, request, code):
        try:
            person = Person.objects.get(id=code)
            # instance
            # سریالایز کردن
            ser_data = PersonSerializer(instance=person)
            return Response(data=ser_data.data)
        except:
            return Response('Not Found')

    # =====================================================
    # class PersonAdd(APIView):
    #     # این request درخواستی است که ارسال میشه و میاد به سمت تابع
    #     # از سمت درخواست کننده api
    #     def post(self, request):
    #         # عمل deserialize
    #         ser_data = PersonSerializer(data=request.POST)
    #         if ser_data.is_valid():
    #             Person.objects.create(
    #                 name=ser_data.validated_data['name'],
    #                 family=ser_data.validated_data['family'],
    #                 email=ser_data.validated_data['email'],
    #                 age=ser_data.validated_data["age"],
    #                 username=ser_data.validated_data['username'],
    #                 password=ser_data.validated_data['password'],
    #             )
    #             return Response(data=ser_data.data,status=status.HTTP_201_CREATED)
    #         return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)

    # روش دوم درج


class PersonAdd(APIView):
    permission_classes = [IsAdminUser]

    # این request درخواستی است که ارسال میشه و میاد به سمت تابع
    # از سمت درخواست کننده api

    def post(self, request):
        # عمل deserialize
        ser_data = PersonSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


# =====================================================
class ProductAdd(APIView):
    # Class Authentication
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request):
        # دیتا و فایل با هم
        ser_data = ProductSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateTokenForAllUser(APIView):
    def get(self, request):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
        return Response(status=status.HTTP_200_OK)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class ProductList(APIView):
    def get(self, request):
        Products = Product.objects.all()
        # عملیات سریالایز انجام بشه
        # داده های آبجکتی تبدیل به بشن به فایل استریم ها
        ser_data = ProductSerializer(instance=Products, many=True)
        # اینجا میگیم فقط دیتا رو برگردون
        return Response(data=ser_data.data)


class DeleteProductFeature(APIView):
    permission_classes = [CustomPermissionForProductFeature]

    def delete(self, request, pk):
        try:
            product_feature = ProductFeature.objects.get(pk=pk)

            product_feature.delete()
            return Response("حذف با موفقیت انجام شد")
        except ProductFeature.DoesNotExist:
            return Response("ویژگی مورد نظر یافت نشد")
