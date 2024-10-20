from django.urls import path

from tasks.presentation.v1.api.views import CommentListView, TaskListAPIView, TaskCreateAPIView, TaskRetrieveAPIView, \
    TaskUpdateAPIView, TaskDeleteAPIView, TaskAttachFilesAPIView, CommentPostView

urlpatterns = [
    path('tasks/list/', TaskListAPIView.as_view(), name='task-list'),
    path('tasks/post/', TaskCreateAPIView.as_view(), name='task-create'),
    path('tasks/retrieve/<int:task_id>/', TaskRetrieveAPIView.as_view(), name='task-retrieve'),
    path('tasks/update/<int:task_id>/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('tasks/delete/<int:task_id>/', TaskDeleteAPIView.as_view(), name='task-delete'),
    path('tasks/attach/files/<int:task_id>/', TaskAttachFilesAPIView.as_view(), name='task-attach-files'),

    path('tasks/<int:task_id>/comments/list/', CommentListView.as_view(), name='task-comments-list'),
    path('tasks/<int:task_id>/comments/create/', CommentPostView.as_view(), name='task-comments-post')
]
