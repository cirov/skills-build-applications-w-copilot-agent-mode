from django.conf import settings

class User:
    @staticmethod
    def create(email, name, password):
        return settings.MONGO_DB['users'].insert_one({
            'email': email,
            'name': name,
            'password': password
        })

    @staticmethod
    def get_all():
        return list(settings.MONGO_DB['users'].find())

class Team:
    @staticmethod
    def create(name, members):
        return settings.MONGO_DB['teams'].insert_one({
            'name': name,
            'members': members
        })

    @staticmethod
    def get_all():
        return list(settings.MONGO_DB['teams'].find())

class Activity:
    @staticmethod
    def create(user_id, activity_type, duration):
        return settings.MONGO_DB['activity'].insert_one({
            'user_id': user_id,
            'activity_type': activity_type,
            'duration': duration
        })

    @staticmethod
    def get_all():
        return list(settings.MONGO_DB['activity'].find())

class Leaderboard:
    @staticmethod
    def create(team_id, score):
        return settings.MONGO_DB['leaderboard'].insert_one({
            'team_id': team_id,
            'score': score
        })

    @staticmethod
    def get_all():
        return list(settings.MONGO_DB['leaderboard'].find())

class Workout:
    @staticmethod
    def create(name, description):
        return settings.MONGO_DB['workouts'].insert_one({
            'name': name,
            'description': description
        })

    @staticmethod
    def get_all():
        return list(settings.MONGO_DB['workouts'].find())
