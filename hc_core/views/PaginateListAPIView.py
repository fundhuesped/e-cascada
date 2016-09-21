from rest_framework import generics

class PaginateListAPIView(generics.ListAPIView):

    def initial(self, request, *args, **kwargs):
        all_items = self.request.query_params.get('all')
        # si el valor es true, entonces quiere todos los valores
        if all_items == 'True' or all_items == 'true':
            self.pagination_class = None
        super(PaginateListAPIView, self).initial(request, *args, **kwargs)
