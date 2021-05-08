from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import modelform_factory 

from .models import Meme
from .helpers import two_randint

class RankMemes(generic.TemplateView):
    
    template_name = 'rank.html'

class UploadMeme(generic.CreateView):

    model = Meme
    fields = ['image']
    template_name = 'upload.html'
    success_url = reverse_lazy('rank')

    def post(self, request, *args, **kwargs):

        for file in request.FILES.getlist('image'):
            form_of_image = modelform_factory(self.model, fields=self.fields)
            data = {"image":file}
            new_form = form_of_image(files=data)
            if new_form.is_valid():
                new_form.save()
            
        return HttpResponseRedirect(self.success_url)

def get_two_memes(request):

    num_of_rows = Meme.objects.count()
    rand_id1, rand_id2 = two_randint(num_of_rows)

    meme1 = Meme.objects.all()[rand_id1].image.url
    meme2 = Meme.objects.all()[rand_id2].image.url

    return JsonResponse({"meme_urls":[meme1, meme2]})

def like_meme(request):

    try:
        liked_meme = Meme.objects.get(image=request.GET["imgurl"])
        liked_meme.likes += 1
        liked_meme.save()
        return JsonResponse({"result":"Success"})
    except Exception as e:
        print(e)
        return JsonResponse({"result":"Failed"})        

class TopMemes(generic.ListView):
    
    model = Meme
    paginate_by = 10
    ordering = ["-likes"]
    template_name = "top.html"
