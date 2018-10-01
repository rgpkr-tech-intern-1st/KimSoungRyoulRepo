from rest_framework import serializers

from member.models import Account
from member.models.user_info import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    # 외래키는 1대1 관계이고 고정적으로 하나의 계정에 연결되어야하기때문에 read_only=True를 줘서
    # api에서 값수정을 못하게 막아야함 AccountSerializer.create()에서 값을 박아주는걸로 오버라이딩함
    # userInfo 는 api 에 보여주고 생성삭제 되는데 제약이 걸려있어야됨 나중에 수정하자
    account = serializers.CharField(read_only=True)

    class Meta:
        model = UserInfo
        fields = ('name', 'phone_num', 'owner_mileage_amount', 'account')


class AccountSerializer(serializers.ModelSerializer):
    userinfo = UserInfoSerializer(required=True, many=False, )

    # 회원 계정생성시에 권한그룹도 같이 껴넣어야함
    def create(self, validated_data):
        print('create 실행되나 ? ...........')
        account = Account(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            is_superuser=False,
            is_active=True,
            is_staff=False,
        )
        account.set_password(validated_data['password'])
        # print('--------------', str([ob.name for ob in validated_data['groups']]), '------------')
        account.save()
        for group in validated_data['groups']:
            account.groups.add(group)
        print(validated_data['userinfo'])
        UserInfo.objects.create(account_id=account.id,
                                name=validated_data['userinfo']['name'],
                                phone_num=validated_data['userinfo']['phone_num'],
                                owner_mileage_amount=validated_data['userinfo']['owner_mileage_amount']
                                )
        return account

    def update(self, instance, validated_data):
        print('update 실행됨..... 구현된 내용은 없음')
        return instance

    class Meta:
        model = Account
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'groups', 'userinfo')
