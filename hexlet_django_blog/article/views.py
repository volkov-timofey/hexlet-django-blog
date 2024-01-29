from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
        
def index(request, tags, article_id):
    return render(request, 'articles/index.html', context={
            'name': f'Статья номер {article_id}. Тег {tags}'
        })
    
