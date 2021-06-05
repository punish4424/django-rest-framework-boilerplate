from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class ReadNestedViewMixin(GenericViewSet):
    read_serializer_class = None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.read_serializer_class(instance, context={"request": request})
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.read_serializer_class(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)

        serializer = self.read_serializer_class(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        instance = self.get_object()
        serializer = self.read_serializer_class(instance, context={"request": request})
        return Response(serializer.data)