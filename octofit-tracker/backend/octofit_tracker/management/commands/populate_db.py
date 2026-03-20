from django.core.management.base import BaseCommand
from octofit_tracker.populate_db import run

class Command(BaseCommand):
    help = 'Populate the database with test data for Octofit Tracker'

    def handle(self, *args, **options):
        run()
        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
