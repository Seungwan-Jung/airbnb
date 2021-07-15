from . import models
from django.views.generic import ListView
# Create your views here.

class HomeView(ListView):

    """ HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans= 5
    ordering = "created"
    context_object_name="rooms"