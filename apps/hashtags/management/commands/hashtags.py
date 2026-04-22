from django.core.management.base import BaseCommand, CommandError
from apps.hashtags.models import Hashtags

from faker import Faker



class Command(BaseCommand):

    help = 'Creates default hashtags'



    def get_words(self):
        fake = Faker()

        words = set()

        while len(words) < 50:
            words.add(fake.word().lower())
        
        return words

    def handle(self, *args, **options):
        words = self.get_words()
        
        for word in words:
            name = f"#{word}"
            
            # Use get_or_create to prevent UniqueConstraint errors on re-runs
            Hashtags.objects.get_or_create(name=name)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully processed {len(words)} hashtags'))
