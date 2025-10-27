from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Task
from .serializers import TaskSerializer


class TaskUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'slug'
    allowed_methods = ['GET', 'PUT', 'PATCH']

#    def get_object(self):
#        queryset = self.get_queryset()
#        slug = self.kwargs.get('slug')
#        session_key = self.request.session.session_key
#        if not session_key:
#            self.request.session.create()
#            session_key = self.request.session.session_key
#
#        obj = queryset.filter(slug=slug, session_key=session_key).first()
#        if not obj:
#            raise NotFound("Task not found.")
#        return obj

    def get_object(self):
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.create()
        slug = self.kwargs.get("slug")
        obj = Task.objects.filter(slug=slug, session_key=session_key).first()
        if not obj:
            raise NotFound("Task not found.")
        return obj    



class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'slug'


class TaskMixinView(
                mixins.CreateModelMixin,
                mixins.ListModelMixin,
                generics.GenericAPIView,
                    ):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'slug'
    allowed_methods = ['GET', 'POST', 'PATCH']

    def get_queryset(self):
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.create()
            session_key = self.request.session.session_key
        return Task.objects.filter(session_key=session_key)


    def perform_create(self, serializer):
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.create()
            session_key = self.request.session.session_key
        serializer.save(session_key=session_key)



    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if 'slug' in kwargs:
            return self.partial_update(request, *args, **kwargs)
        return Response({'detail': 'Method Is Not Allowed, Go Fuck Yourself.'}, status=405)