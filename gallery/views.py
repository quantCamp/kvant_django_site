from django.shortcuts import render, get_object_or_404
from .models import Album


def album_list(request):

    sort = request.GET.get('sort', 'newest')
    sort_map = {
        'newest': '-created_at',
        'oldest': 'created_at',
        'title': 'title',
        '-title': '-title',
    }

    # Получаем поле для сортировки
    order_by = sort_map.get(sort, '-created_at')
    albums = Album.objects.all().order_by(order_by)

    return render(request, 'gallery/album_list.html', {
        'albums': albums,
        'current_sort': sort,
    })


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    photos = album.photos.all().order_by('uploaded_at')

    return render(request, 'gallery/album_detail.html', {
        'album': album,
        'photos': photos,
    })






