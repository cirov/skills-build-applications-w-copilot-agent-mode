"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import UserView, TeamView, ActivityView, LeaderboardView, WorkoutView

urlpatterns = [
    path('users/', UserView.as_view(), name='user-list'),
    path('teams/', TeamView.as_view(), name='team-list'),
    path('activities/', ActivityView.as_view(), name='activity-list'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard-list'),
    path('workouts/', WorkoutView.as_view(), name='workout-list'),
]
