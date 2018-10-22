# Create your views here.
import random

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.app_settings import swagger_settings
from drf_yasg.inspectors import FieldInspector, SwaggerAutoSchema, CoreAPICompatInspector, NotHandled
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from payments.infrastructure.serializers import CreditCardPaymentSerializer, NaverPayPaymentSerializer, \
    TestModelSerializer, TestASerializer
from payments.models.entity.payment import CreditCardPayment, NaverPayPayment, TestModel, TestA


class DjangoFilterDescriptionInspector(CoreAPICompatInspector):
    def get_filter_parameters(self, filter_backend):
        if isinstance(filter_backend, DjangoFilterBackend):
            result = super(DjangoFilterDescriptionInspector, self).get_filter_parameters(filter_backend)
            for param in result:
                if not param.get('description', ''):
                    param.description = "Filter the returned list by {field_name}".format(field_name=param.name)

            return result

        return NotHandled


class NoSchemaTitleInspector(FieldInspector):
    def process_result(self, result, method_name, obj, **kwargs):
        # remove the `title` attribute of all Schema objects
        if isinstance(result, openapi.Schema.OR_REF):
            # traverse any references and alter the Schema object in place
            schema = openapi.resolve_ref(result, self.components)
            schema.pop('title', None)

            # no ``return schema`` here, because it would mean we always generate
            # an inline `object` instead of a definition reference

        # return back the same object that we got - i.e. a reference if we got a reference
        return result


class NoTitleAutoSchema(SwaggerAutoSchema):
    field_inspectors = [NoSchemaTitleInspector] + swagger_settings.DEFAULT_FIELD_INSPECTORS


class NoPagingAutoSchema(NoTitleAutoSchema):
    def should_page(self):
        return False


class CreditCardPaymentHistoryViewSet(ModelViewSet):
    # object = Payment
    queryset = CreditCardPayment.objects.all()
    serializer_class = CreditCardPaymentSerializer


class NaverPayPaymentViewSet(viewsets.ViewSet):

    @method_decorator(name='list', decorator=swagger_auto_schema(
        operation_summary='이건 서머리222 ',
    ))
    def list(self, request):
        queryset = NaverPayPayment.objects.all()
        serializer = NaverPayPaymentSerializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(name='retrieve', decorator=swagger_auto_schema(
        operation_summary='이건 서머리222 ',
    ))
    def retrieve(self, request, pk=None):
        queryset = NaverPayPayment.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = NaverPayPaymentSerializer(user)
        return Response(serializer.data)


class TestModelListAPIView(generics.ListAPIView):
    serializer_class = TestModelSerializer

    @swagger_auto_schema(
        operation_id='이거 없으면 swagger 등록안됨 이건 operation_ID',
        operation_description="레디스 테스트용 api",
        responses={404: 'TestModel not found'},
        operation_summary='레디스 테스트용 API 입니다')
    def get(self, request, *args, **kwargs):
        random_num = random.randrange(1, 100000)
        queryset = TestModel.objects.filter(id__gt=random_num - 1000, id__lte=random_num)
        # queryset = TestModel.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TestModelRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TestASerializer

    queryset = TestA.objects.all()

    @swagger_auto_schema(
        operation_id='ManyToMany 테스트용 d',
        operation_description="다대다 테스트 API",
        responses={404: 'TestModel not found'},
        operation_summary='TestModel ManyToMany 테스트용 API 입니다')
    def get(self, request, *args, **kwargs):
        test_a = TestA.objects.prefetch_related('test_b_set').filter(pk=1)
        print(test_a)

        seri = serializers.serialize("json", test_a)
        print('직렬화 된상태: ', seri[0])

        return HttpResponse(seri, content_type='application/json')
        # return super().get(request, *args, **kwargs)
