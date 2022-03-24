from django.core.management.base import BaseCommand
import json
from django.contrib.auth.models import User
from api.models import Post, Journey
from datetime import datetime


class Command(BaseCommand):

    @staticmethod
    def set_author(item_data):
        item_data["created_by"] = User.objects.get(
            pk=item_data["created_by_id"])
        del item_data["created_by_id"]

    @staticmethod
    def set_journey(item_data):
        item_data["journey"] = Journey.objects.get(
            pk=item_data["journey_id"])
        del item_data["journey_id"]

    @staticmethod
    def set_created_at(item_data):
        item_data["created_at"] = datetime.fromisoformat(
            item_data["created_at"])

    def handle(self, *model_labels, **options):
        with open("./sample_data.json") as json_file:
            data = json.load(json_file)
            for item_type, items in data.items():
                for item_data in items:
                    print(
                        f"Importing '{item_type}' (pk:{item_data['id']}) "
                        "in database")
                    match item_type:
                        case "users":
                            User(**item_data).save()
                        case "posts":
                            Command.set_author(item_data)
                            Command.set_journey(item_data)
                            Command.set_created_at(item_data)
                            Post(**item_data).save()
                        case "journeys":
                            Command.set_author(item_data)
                            Command.set_created_at(item_data)
                            Journey(**item_data).save()
