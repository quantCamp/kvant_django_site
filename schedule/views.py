from django.shortcuts import render
from schedule.models import ScheduleItem


# Create your views here.
def schedule_view(request):
    schedule_items = ScheduleItem.objects.all()
    return render(request, './schedule/schedule_list.html', context={'scheduleItems': schedule_items})
def schedule_detail(request, pk):
    schedule_details = ScheduleItem.objects.get(id=pk)
    return render(request, './schedule/schedule_detail.html', context={'scheduleItem': schedule_details})