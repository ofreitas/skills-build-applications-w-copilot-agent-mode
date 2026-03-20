from django.utils import timezone
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

def run():
    # Clear existing data
    User.objects.all().delete()
    Team.objects.all().delete()
    Activity.objects.all().delete()
    Workout.objects.all().delete()
    Leaderboard.objects.all().delete()

    # Create Teams
    team1 = Team.objects.create(name="OctoRunners", description="Running enthusiasts")
    team2 = Team.objects.create(name="FitSquad", description="General fitness team")

    # Create Users
    user1 = User.objects.create(email="alice@example.com", name="Alice", team=team1.name)
    user2 = User.objects.create(email="bob@example.com", name="Bob", team=team2.name)

    # Create Activities
    Activity.objects.create(user=user1, type="Running", duration=30, date=timezone.now().date())
    Activity.objects.create(user=user2, type="Cycling", duration=45, date=timezone.now().date())

    # Create Workouts
    Workout.objects.create(name="Morning Cardio", description="A quick cardio session", difficulty="Easy")
    Workout.objects.create(name="Strength Blast", description="Strength training routine", difficulty="Hard")

    # Create Leaderboard entries
    Leaderboard.objects.create(user=user1, score=100)
    Leaderboard.objects.create(user=user2, score=80)

    print("Test data created successfully.")
