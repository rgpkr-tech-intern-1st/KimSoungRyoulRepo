# management/commands/addpost.py

from django.core.management.base import BaseCommand

from payments.models.entity.payment import TestModel


class Command(BaseCommand):
    help = 'Add as many posts as you want'

    def add_arguments(self, parser):
        parser.add_argument('model_cnt', type=int)

    def handle(self, *args, **options):
        model_cnt = options['model_cnt']
        if model_cnt > 0:
            TestModel.objects.bulk_create(
                [TestModel(text="Sample Text #{}".format(i)) for i in range(model_cnt)]
            )
            self.stdout.write(self.style.SUCCESS('Successfully add {} posts'.format(model_cnt)))
