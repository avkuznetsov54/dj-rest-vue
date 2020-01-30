from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from mortgages.models import MortgagePrograms
from mortgages.serializers import MortgageProgramsSerializer


class MyPagination(PageNumberPagination):
    page_size = 100


class MortgageProgramsView(generics.ListAPIView):
    serializer_class = MortgageProgramsSerializer
    queryset = MortgagePrograms.objects.all()
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated, )

    def filter_queryset(self, queryset):
        for k, v in self.request.query_params.items():
            params = {}
            # if k == "cursor":
            #     continue

            # если 'v' равно пустой строке то прекращаем итерацию что не занести её в queryset, а то 500 error
            if v == '':
                continue
            if k == 'property_value':
                k1 = 'min_sum_credit' + '__lte'
                params.update({k1: v})
                k2 = 'max_sum_credit' + '__gte'
                params.update({k2: v})
            if k == 'rate':
                k = k + '__lte'
                params.update({k: v})
            if k == 'first_payment':
                k = k + '__lte'
                params.update({k: v})
            queryset = queryset.filter(**params)
            # тоже самое что:
            # queryset = queryset.filter(model__icontains="asdf")

        # return queryset.order_by('-rate')
        return queryset
