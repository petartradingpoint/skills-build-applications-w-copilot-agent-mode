from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Create Users
        ironman = User.objects.create(email='ironman@marvel.com', username='IronMan', team=marvel)
        captain = User.objects.create(email='captain@marvel.com', username='CaptainAmerica', team=marvel)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Do 50 pushups')
        running = Workout.objects.create(name='Running', description='Run 5km')
        pushups.suggested_for.set([ironman, batman])
        running.suggested_for.set([captain, superman])

        # Create Activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=batman, type='Pushups', duration=15, date=timezone.now().date())
        Activity.objects.create(user=superman, type='Running', duration=25, date=timezone.now().date())
        Activity.objects.create(user=captain, type='Pushups', duration=20, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, points=120)
        Leaderboard.objects.create(user=batman, points=110)
        Leaderboard.objects.create(user=superman, points=100)
        Leaderboard.objects.create(user=captain, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
