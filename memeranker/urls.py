from django.urls import path
from .views import RankMemes, UploadMeme, get_two_memes, like_meme, TopMemes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RankMemes.as_view(), name='rank'),
    path('upload', UploadMeme.as_view(), name='upload'),
    path('get_two_memes', get_two_memes, name="get_two_memes"),
    path('like', like_meme, name="like_meme"),
    path('top', TopMemes.as_view(), name="top"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

