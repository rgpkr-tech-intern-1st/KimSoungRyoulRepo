# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from member.models import Account


def index(requests):
    return render(request=requests, template_name='index.html')


class AccountListView(ListView):

    # 제너릭 뷰=> BaseView

    # template_name = app_name/model_list.html 이 기본설정

    def get_queryset(self):
        print(' 쿼리셋 가져오기 ')
        return Account.objects.filter(is_superuser=True)


# Function based View
def detail(request, pk):
    account_obj = get_object_or_404(Account, pk=pk)
    return render(request, 'member/account_detail.html', {
        'account': account_obj,
    })


# Class based View
class AccountDetailView(DetailView):
    # 해당 모델 - URLConf 의 PK 변수를 활용하여 해당 모델의 특정 record를 컨텍스트 변수(object)에 담는다.
    model = Account

    # 디폴트 템플릿명: <app_label>/<model_name>_detail.html
    # template_name = 'member/detail.html'

    # 디폴트 컨텍스트 변수명 :  object
    # context_object_name = 'account'
