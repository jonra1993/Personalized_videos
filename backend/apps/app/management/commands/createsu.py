from django.core.management.base import BaseCommand
from apps.authentication_api.models import User

class Command(BaseCommand):
  def handle(self, *args, **options):
      if not User.objects.filter(email="admin@gmail.com").exists():
        User.objects.create_superuser( "admin@gmail.com", "admin")