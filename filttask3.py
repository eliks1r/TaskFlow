from django.shortcuts import render
from django.db.models import Q

def task_list(request):
    form = TaskFilterForm(request.GET)
    tasks = Task.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        status = form.cleaned_data.get('status')
        min_priority = form.cleaned_data.get('min_priority')
        max_priority = form.cleaned_data.get('max_priority')
        deadline_before = form.cleaned_data.get('deadline_before')
        deadline_after = form.cleaned_data.get('deadline_after')

        if search_query:
            tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        if status:
            tasks = tasks.filter(status=status)
        if min_priority is not None:
            tasks = tasks.filter(priority__gte=min_priority)
        if max_priority is not None:
            tasks = tasks.filter(priority__lte=max_priority)
        if deadline_before:
            tasks = tasks.filter(deadline__lte=deadline_before)
        if deadline_after:
            tasks = tasks.filter(deadline__gte=deadline_after)

    return render(request, 'tasks/task_list.html', {'form': form, 'tasks': tasks})