from django.shortcuts import render
from rest_framework.views import APIView
from .models import Status
from .serializers import StatusSerializer
from rest_framework.response import Response
from rest_framework import generics, mixins, parsers, viewsets

# Create your views here.

# APIView is a class-based view that provides behaviour for handling http methods.
# class StatusAPIView(APIView):
    
#     def get(self, request, format = None):
#         status_list = Status.objects.all()
#         status_serializer = StatusSerializer(status_list, many=True)
#         return Response(status_serializer.data)

# class StatusListCreateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# ListAPIView is a generic view that provides a GET method handler.
# class StatusListAPIView(generics.ListAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
    
# CreateAPIView is a generic view that provides a POST method handler.
# class StatusCreateAPIView(generics.CreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
    
# RetrieveAPIView is a generic view that provides a GET method handler with referance or id.
# class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)
    
# UpdateAPIView is a generic view that provides a PUT and PATCH method handler with referance or id.
# class StatusUpdateAPIView(generics.UpdateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'

# DestroyAPIView is a generic view that provides a DELETE method handler with referance or id.
# class StatusDeleteAPIView(generics.DestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'

# class StatusListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
    
#     parser_class = [parsers.MultiPartParser, parsers.FormParser]
    
    
    
# class StatusDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
    
#     parser_class = [parsers.MultiPartParser, parsers.FormParser]

# ViewSet is a class-based view that provides behaviour for handling http methods.

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
    # parser_class = [parsers.MultiPartParser, parsers.FormParser]
    
    # def get_queryset(self):
    #     qs = Status.objects.all()
    #     query = self.request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(content__icontains=query)
    #     return qs
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
