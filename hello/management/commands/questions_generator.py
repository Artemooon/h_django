import random

from django.core.management.base import BaseCommand
from faker import Faker
from hello.models import Question


class Command(BaseCommand):
    help = 'Add randoms questions to DB'

    def add_arguments(self, parser):
        parser.add_argument('addquestions', nargs='?', type=int, default=10)

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(options['addquestions']):
            rand_int = random.randint(0, 1)
            q_text = fake.paragraph(nb_sentences=1).replace(".", "?")
            Question.objects.create(question_text=q_text, pub_date=fake.date_time(),
                                    is_opened=bool(rand_int))
        self.stdout.write(self.style.SUCCESS('Successfully created %s questions' % options['addquestions']))
