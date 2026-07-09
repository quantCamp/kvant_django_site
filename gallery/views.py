from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Album


def album_list(request):
    sort = request.GET.get('sort', 'newest')

    sort_map = {
        'newest': '-created_at',  # Сначала новые
        'oldest': 'created_at',  # Сначала старые
        'title': 'title',  # По названию (А-Я)
        '-title': '-title',  # По названию (Я-А)
    }

    order_by = sort_map.get(sort, '-created_at')

    albums = Album.objects.all().order_by(order_by)

    paginator = Paginator(albums, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'gallery/album_list.html', {
        'page_obj': page_obj,
        'albums': page_obj.object_list,
        'current_sort': sort,  # Передаём текущую сортировку в шаблон
    })


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    photos = album.photos.all().order_by('uploaded_at')

    return render(request, 'gallery/album_detail.html', {
        'album': album,
        'photos': photos,
    })






