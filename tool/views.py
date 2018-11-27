from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from tool.forms import SearchForm


class StartView(FormView):

    def get(self, request):

        form = SearchForm()
        return render(request, 'start.html', {'form': form})


    def post(self, request):

        form = SearchForm(request.POST)

        if form.is_valid():
            lis = []
            for i in form:
                lis.append(i)
                print(lis[0])
                return render(request, 'start.html', {'form': form})
        else:
            form = SearchForm()
            return render(request, 'start.html', {'form': form})