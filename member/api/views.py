# Create your views here.
import coreapi
import coreschema
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, authentication, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from member.models import Account
from member.models.user_info import UserInfo
from member.serializers import UserInfoSerializer, AccountSerializer


class UserInfoAPIView(GenericAPIView):
    """
        View to list all users in the system.

        * Requires token authentication.
        * Only admin users are able to access this view.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    queryset = UserInfo.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UserInfoSerializer
        return UserInfoSerializer

    def get_object(self):
        return UserInfo.objects.all()

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        userinfo_names = [userinfo.name for userinfo in UserInfo.objects.all()]
        # userinfos = serializers.serialize("json", UserInfo.objects.all())

        return Response(userinfo_names)


class UserInfoViewSet(viewsets.ModelViewSet):
    schema = AutoSchema(manual_fields=[
        coreapi.Field(
            name="name",
            required=True,
            example='qqqqqqqqqq',
            schema=coreschema.String(),
            description='회원 계정 입니다 서술'
        ),
        coreapi.Field(
            name="phone_num",
            description="cvvcvcv",
            example="010-2324-6602",
        )
    ]
    )

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_id='회원 정보 전부 조회,',
    operation_summary='API 간략하게 설명하는 부분 ',
    operation_description="회원 정보 전부 조회 합니다 "
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_id='회원 가입',
    operation_summary='API 간략하게 설명하는 부분 ',
    operation_description="회원 정보 전부 조회 합니다 "
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_id='회원 정보 전부 수정,',
    operation_summary='API 간략하게 설명하는 부분 ',
    operation_description="회원 정보 전부 조회 합니다 "
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_id='회원 정보 부분 수정,',
    operation_summary='API 간략하게 설명하는 부분 ',
    operation_description="회원 정보 전부 조회 합니다 "
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_id='회원 탈퇴',
    operation_summary='API 간략하게 설명하는 부분 ',
    operation_description="회원 정보 전부 조회 합니다 "
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_id='회원 한명정보 조회',
    operation_summary='API 간략하게 설명하는 부분 ',
    operation_description="회원 정보 전부 조회 합니다 ",
))
class AccountViewSet(viewsets.ModelViewSet):
    """
    param -- asdfasdfasd

    create:
    회원 생성

    retrieve:
    회원 정보 1개를 반환

    list:
    모든 유저들의 리스트 반환

    update:
    수정  PUT 주석입니다

    partial_update:
    이건 patch 문서 주석입니다

    delete:
    삭제 api 주석입니다

    """
    # schema = AutoSchema(manual_fields=[
    #     coreapi.Field(
    #         name="userinfo",
    #         required=True,
    #         location="body",
    #         example='qqqqqqqqqq',
    #         schema=coreschema.String(),
    #         description='회원 계정 입니다 서술'
    #     ),
    #     ]
    # )

    model = Account
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
