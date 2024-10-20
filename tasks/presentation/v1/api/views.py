from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.persistence.controllers.comment_controller import CommentController
from tasks.persistence.controllers.task_controller import TaskController
from tasks.presentation.v1.api.serializer import TaskSerializer, CommentSerializer


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        tags=['Tasks'],
        responses={200: TaskSerializer(many=True)},
    ),
)
class TaskListAPIView(APIView):
    _controller = TaskController()

    def get(self, request):
        tasks = self._controller.list_tasks(request)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        tags=['Tasks'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
                'assigned_to': openapi.Schema(type=openapi.TYPE_INTEGER),
                'deadline': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
                'reminder': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
            },
        ),
        responses={201: TaskSerializer},
    )
)
class TaskCreateAPIView(APIView):
    _controller = TaskController()

    def post(self, request):
        task = TaskController.create_task(request.data, request.user)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        tags=['Tasks'],
        responses={200: TaskSerializer},
    )
)
class TaskRetrieveAPIView(APIView):
    _controller = TaskController()

    def get(self, request, task_id):
        task = self._controller.get_task(task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


@method_decorator(
    name='put',
    decorator=swagger_auto_schema(
        tags=['Tasks'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING),
                'description': openapi.Schema(type=openapi.TYPE_STRING),
                'assigned_to': openapi.Schema(type=openapi.TYPE_INTEGER),
                'deadline': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
                'reminder': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
            },
        ),
        responses={200: TaskSerializer},
    )
)
class TaskUpdateAPIView(APIView):
    _controller = TaskController()

    def put(self, request, task_id):
        task = self._controller.get_task(task_id)
        updated_task = self._controller.update_task(task, request.data)
        serializer = TaskSerializer(updated_task)
        return Response(serializer.data)


@method_decorator(
    name='delete',
    decorator=swagger_auto_schema(
        tags=['Tasks'],
        responses={204: 'No Content'},
    )
)
class TaskDeleteAPIView(APIView):
    _controller = TaskController()

    def delete(self, request, task_id):
        task = self._controller.get_task(task_id)
        self._controller.delete_task(task)
        return Response(status=status.HTTP_204_NO_CONTENT)


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        tags=['Comments'],
        responses={200: CommentSerializer(many=True)},
    )
)
class CommentListView(APIView):
    _task_controller = TaskController()
    _comment_controller = CommentController()

    def get(self, request, task_id):
        task = self._task_controller.get_task(task_id)
        comments = self._comment_controller.list_comments(task)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        tags=['Comments'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'content': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={201: CommentSerializer},
    )
)
class CommentPostView(APIView):
    _task_controller = TaskController()
    _comment_controller = CommentController()

    def post(self, request, task_id: int):
        self._task_controller.get_task(task_id)
        comment = self._comment_controller.create_comment(request, task_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        tags=['Tasks'],
        manual_parameters=[
            openapi.Parameter(
                'files', openapi.IN_FORM,
                description="File to be attached",
                type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_FILE)
            )
        ],
        responses={200: openapi.Response(description="Files attached successfully")},
    )
)
class TaskAttachFilesAPIView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, task_id: int):
        files = request.FILES.getlist('files')
        TaskController.attach_files(task_id, files)
        return Response({'message': 'Files attached successfully'}, status=status.HTTP_200_OK)
