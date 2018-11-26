import json

from django.utils.decorators import method_decorator
from django.views import View
from django.core import serializers
from django.http import JsonResponse, HttpResponse, Http404
from datetime import datetime

from django.forms.models import model_to_dict

from django.views.decorators.csrf import csrf_exempt

from crud_operations.models import ToDo


class TasksList(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        tasks = ToDo.objects.all()
        tasks_json = serializers.serialize('json', tasks)
        return JsonResponse(tasks_json, safe=False)

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_task = datetime.strptime(request.POST.get('start_task'), '%Y-%m-%d')
        deadline = datetime.strptime(request.POST.get('deadline'), '%Y-%m-%d')
        todo = True if request.POST.get('todo') == 'true' else False
        in_progress = True if request.POST.get('in_progress') == 'true' else False
        done = True if request.POST.get('done') == 'true' else False

        ToDo.objects.create(
            title=title,
            description=description,
            start_task=start_task,
            deadline=deadline,
            todo=todo,
            in_progress=in_progress,
            done=done
        )

        task = ToDo.objects.filter(pk=pk)
        task_json = serializers.serialize('json', task)
        return JsonResponse(task_json)


class TaskOperations(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def put(self, request, pk):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        title = body.get('title')
        description = body.get('description')
        start_task = datetime.strptime(body.get('start_task'), '%Y-%m-%d')
        deadline = datetime.strptime(body.get('deadline'), '%Y-%m-%d')
        todo = True if body.get('todo') == 'true' else False
        in_progress = True if body.get('in_progress') == 'true' else False
        done = True if body.get('done') == 'true' else False

        ToDo.objects.update(
            title=title,
            description=description,
            start_task=start_task,
            deadline=deadline,
            todo=todo,
            in_progress=in_progress,
            done=done
        )
        task = ToDo.objects.get(pk=pk)
        return JsonResponse(model_to_dict(task))

    def delete(self, request, pk):
        try:
            task = ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            raise Http404

        task.delete()

        return HttpResponse(status=204)

