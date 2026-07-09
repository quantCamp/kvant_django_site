from django.db import migrations
import os
from PIL import Image, ImageDraw

def create_dummy_image(path, color, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Create image
    img = Image.new('RGB', (800, 600), color=color)
    # Draw border
    draw = ImageDraw.Draw(img)
    draw.rectangle([20, 20, 780, 580], outline="#ffffff", width=4)
    # save
    img.save(path)

def populate_gallery(apps, schema_editor):
    from django.conf import settings
    Album = apps.get_model('gallery', 'Album')
    Photo = apps.get_model('gallery', 'Photo')

    media_root = settings.MEDIA_ROOT
    gallery_dir = os.path.join(media_root, 'gallery')

    # Create dummy images
    create_dummy_image(os.path.join(gallery_dir, 'opening_cover.png'), '#3b82f6', 'Opening Cover')
    create_dummy_image(os.path.join(gallery_dir, 'opening_1.png'), '#60a5fa', 'Opening 1')
    create_dummy_image(os.path.join(gallery_dir, 'opening_2.png'), '#93c5fd', 'Opening 2')
    create_dummy_image(os.path.join(gallery_dir, 'opening_3.png'), '#2563eb', 'Opening 3')

    create_dummy_image(os.path.join(gallery_dir, 'studies_cover.png'), '#10b981', 'Studies Cover')
    create_dummy_image(os.path.join(gallery_dir, 'studies_1.png'), '#34d399', 'Studies 1')
    create_dummy_image(os.path.join(gallery_dir, 'studies_2.png'), '#6ee7b7', 'Studies 2')
    create_dummy_image(os.path.join(gallery_dir, 'studies_3.png'), '#059669', 'Studies 3')

    # Create Database Entries
    album1 = Album.objects.create(
        title="Открытие смены 2026",
        description="Яркие моменты церемонии открытия летней смены ЛФМШ «Квант». Знакомство с вожатыми, поднятие флага и первые отрядные выступления.",
        cover_image="gallery/opening_cover.png"
    )
    Photo.objects.create(album=album1, img="gallery/opening_1.png", caption="Поднятие флага школы")
    Photo.objects.create(album=album1, img="gallery/opening_2.png", caption="Творческое представление вожатых")
    Photo.objects.create(album=album1, img="gallery/opening_3.png", caption="Пермый отрядный сбор")

    album2 = Album.objects.create(
        title="Наши учебные будни",
        description="Как проходят занятия в Кванте. Увлекательные лекции, решения олимпиадных задач на семинарах и защита проектов.",
        cover_image="gallery/studies_cover.png"
    )
    Photo.objects.create(album=album2, img="gallery/studies_1.png", caption="Лекция по физике")
    Photo.objects.create(album=album2, img="gallery/studies_2.png", caption="Решение сложных математических задач")
    Photo.objects.create(album=album2, img="gallery/studies_3.png", caption="Занятие по робототехнике")

def clear_gallery(apps, schema_editor):
    Album = apps.get_model('gallery', 'Album')
    Album.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_gallery, clear_gallery),
    ]
