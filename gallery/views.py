from django.shortcuts import render, get_object_or_404
from gallery.models import Album

def album_list(request):

    albums = Album.objects.all().order_by('-created_at')
    return render(request, 'gallery/album_list.html', context={
        'albums': albums
    })


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    photos = album.photos.all().order_by('uploaded_at')
    return render(request, 'gallery/album_detail.html', context={
        'album': album,
        'photos': photos
    })



