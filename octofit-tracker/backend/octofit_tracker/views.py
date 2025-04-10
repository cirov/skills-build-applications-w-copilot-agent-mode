from django.http import JsonResponse
from django.views import View
from .models import User

class UserView(View):
    def get(self, request):
        users = User.get_all()
        return JsonResponse({'users': users, 'url': 'https://redesigned-space-pancake-6x75pvrp535g6r-8000.app.github.dev'}, safe=False)

class TeamView(View):
    def get(self, request):
        teams = Team.get_all()
        return JsonResponse({'teams': teams, 'url': 'https://redesigned-space-pancake-6x75pvrp535g6r-8000.app.github.dev'}, safe=False)

class ActivityView(View):
    def get(self, request):
        activities = Activity.get_all()
        return JsonResponse({'activities': activities, 'url': 'https://redesigned-space-pancake-6x75pvrp535g6r-8000.app.github.dev'}, safe=False)

class LeaderboardView(View):
    def get(self, request):
        leaderboard = Leaderboard.get_all()
        return JsonResponse({'leaderboard': leaderboard, 'url': 'https://redesigned-space-pancake-6x75pvrp535g6r-8000.app.github.dev'}, safe=False)

class WorkoutView(View):
    def get(self, request):
        workouts = Workout.get_all()
        return JsonResponse({'workouts': workouts, 'url': 'https://redesigned-space-pancake-6x75pvrp535g6r-8000.app.github.dev'}, safe=False)
