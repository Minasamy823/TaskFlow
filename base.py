from rest_framework.request import Request


class RequestManager:

    def build_filters_from_request(self,
                                   request: Request,
                                   filters_fields: list,
                                   ) -> dict:
        filters = {}
        for field in request.GET:
            if field in filters_fields:
                filters[filters_fields[field]] = request.GET.get(field)

        return filters
