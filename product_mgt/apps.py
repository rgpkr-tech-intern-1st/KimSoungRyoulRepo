from django.apps import AppConfig


class ProductMgtConfig(AppConfig):
    name = 'product_mgt'
    # print SQL queries in shell_plus
    SHELL_PLUS_PRINT_SQL = True
