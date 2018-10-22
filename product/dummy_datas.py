from product.models import Restaurant, Food, FoodOption


def set_dummy_data():
    print('---더미데이터 생성---')
    dummy_restaurant = Restaurant.objects.create(name='피나치공', restaurant_owner='김철수',
                                                 descriptions='37년전통 치킨')

    dummy_food1 = Food.objects.create(name='짜장면', price=3800, food_owned_restaurant=dummy_restaurant)
    FoodOption.objects.create(name='곱빼기', price=1000, related_food=dummy_food1)
    FoodOption.objects.create(name='사천 짜장', price=500, related_food=dummy_food1)

    dummy_food2 = Food.objects.create(name='탕수육', price=12500, food_owned_restaurant=dummy_restaurant)
    FoodOption.objects.create(name='웰던', price=1500, related_food=dummy_food2)
    FoodOption.objects.create(name='미디움', price=1200, related_food=dummy_food2)
