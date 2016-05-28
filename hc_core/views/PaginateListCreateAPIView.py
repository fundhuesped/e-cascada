from rest_framework import generics


class PaginateListCreateAPIView(generics.ListCreateAPIView):

    def initial(self, request, *args, **kwargs):
        all = self.request.query_params.get('all')  # si el valor es true, entonces quiere todos los valores
        if all == 'True' or all == 'true':
            self.pagination_class = None
        super(PaginateListCreateAPIView, self).initial(request, *args, **kwargs)
