# Create your views here.


from django.http import JsonResponse


def get_user_one(request):
    return JsonResponse({'user_id': 'sky5367', 'name': 'ksr'})
