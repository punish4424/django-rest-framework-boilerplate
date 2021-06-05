from rest_framework.filters import BaseFilterBackend


class CustomFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        search_fields = getattr(view, 'custom_filter_fields', None)
        if search_fields:
            kwargs = {}
            for key, value in search_fields.items():
                query_value = request.query_params.get(key)
                if query_value:
                    kwargs[value] = query_value
            try:
                queryset = queryset.filter(**kwargs)
            except Exception as e:
                queryset = queryset.none()
        return queryset.distinct()
