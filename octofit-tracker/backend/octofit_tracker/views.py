from django.http import JsonResponse
from django.views import View
from .models import User, Team, Activity, Leaderboard, Workout

class UserView(View):
    def get(self, request):
        users = User.get_all()
        return JsonResponse({'users': users}, safe=False)

class TeamView(View):
    def get(self, request):
        teams = Team.get_all()
        return JsonResponse({'teams': teams}, safe=False)

class ActivityView(View):
    def get(self, request):
        activities = Activity.get_all()
        return JsonResponse({'activities': activities}, safe=False)

class LeaderboardView(View):
    def get(self, request):
        leaderboard = Leaderboard.get_all()
        return JsonResponse({'leaderboard': leaderboard}, safe=False)

class WorkoutView(View):
    def get(self, request):
        workouts = Workout.get_all()
        return JsonResponse({'workouts': workouts}, safe=False)
