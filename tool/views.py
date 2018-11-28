from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from tool.forms import SearchForm, DataAddForm
import csv

from tool.models import Genes


class StartView(FormView):

    def get(self, request):

        form = SearchForm()
        return render(request, 'start.html', {'form': form})


    def post(self, request):

        form = SearchForm(request.POST)

        if form.is_valid():
            search = form.cleaned_data['search']
            search1 = search.replace('\r', '')
            search2 = search1.split('\n')

            uploaded_genes = Genes.objects.filter(Gname__in=search2)


            ctx = {
                'gene': uploaded_genes
                  }


            return render(request, 'start.html', ctx)
        else:
            form = SearchForm()
            return render(request, 'start.html', {'form': form})


class DataAddView(FormView):

    def get(self, request):
        form = DataAddForm()
        return render(request, 'data_add.html', {'form': form})


    def post(self, request):
        form = DataAddForm(request.POST)
        if form.is_valid():
            upload = form.cleaned_data['input_data']

            with open(upload) as f:
                reader = csv.reader(f, delimiter="\t")
                d = list(reader)
                for lis in d:
                    string = ''.join(lis)
                    #record = []
                    if string.find('!'):
                        #record.append(lis[2])
                        #record.append(lis[5])
                        genename = lis[6]
                        annotation = lis[9]
                        newdata = Genes.objects.create(Gname=genename, annotation = annotation)
            return render(request, 'data_add.html', {'form': form})