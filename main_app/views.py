from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form })

def add_widget(request):
    widget_form = WidgetForm(request.POST)
    widget_form.save()
    return redirect('/')