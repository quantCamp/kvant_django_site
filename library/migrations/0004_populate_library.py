from django.db import migrations
import os

def populate_library(apps, schema_editor):
    from django.conf import settings
    Category = apps.get_model('library', 'Category')
    Material = apps.get_model('library', 'Material')

    media_root = settings.MEDIA_ROOT
    library_dir = os.path.join(media_root, 'library')
    os.makedirs(library_dir, exist_ok=True)

    # Create dummy pdf files
    cheat_sheet_orm_path = os.path.join(library_dir, 'django_orm_cheat_sheet.pdf')
    with open(cheat_sheet_orm_path, 'w', encoding='utf-8') as f:
        f.write("%PDF-1.4 ... Django ORM Cheat Sheet Placeholder Content")

    cheat_sheet_git_path = os.path.join(library_dir, 'git_cheat_sheet.pdf')
    with open(cheat_sheet_git_path, 'w', encoding='utf-8') as f:
        f.write("%PDF-1.4 ... Git Cheat Sheet Placeholder Content")

    # Categories
    django_py = Category.objects.create(name="Django & Python")
    frontend = Category.objects.create(name="Фронтенд & Стили")
    books = Category.objects.create(name="Шпаргалки & Книги")

    # Materials
    # Django & Python
    Material.objects.create(
        title="Официальная документация Django",
        description="Главный справочник по веб-фреймворку Django на английском и русском языках. Всё о вьюхах, моделях, шаблонах и безопасности.",
        material_type="link",
        link="https://docs.djangoproject.com/ru/",
        category=django_py
    )
    Material.objects.create(
        title="Руководство по Django от Metanit",
        description="Подробное русскоязычное руководство для начинающих: от установки Python и Django до развертывания проекта на сервере.",
        material_type="link",
        link="https://metanit.com/python/django/",
        category=django_py
    )

    # Фронтенд & Стили
    Material.objects.create(
        title="Документация MDN Web Docs",
        description="Основной справочник по HTML, CSS и JavaScript от сообщества Mozilla. Лучшие практики и детальное описание стандартов.",
        material_type="link",
        link="https://developer.mozilla.org/",
        category=frontend
    )
    Material.objects.create(
        title="CSS-Tricks",
        description="Популярный блог и справочник по CSS. Множество полезных приемов, примеров верстки, разборов Flexbox и Grid.",
        material_type="link",
        link="https://css-tricks.com/",
        category=frontend
    )

    # Шпаргалки & Книги
    Material.objects.create(
        title="Шпаргалка по Django ORM",
        description="Полезный справочник в формате PDF по основным методам выборки, фильтрации, агрегации и связям таблиц в Django ORM.",
        material_type="file",
        file="library/django_orm_cheat_sheet.pdf",
        category=books
    )
    Material.objects.create(
        title="Шпаргалка по командам Git",
        description="Справочник по основным консольным командам Git для создания репозитория, управления ветками, слияния и коммитов.",
        material_type="file",
        file="library/git_cheat_sheet.pdf",
        category=books
    )

def clear_library(apps, schema_editor):
    Category = apps.get_model('library', 'Category')
    Category.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_rename_file_name_material_file'),
    ]

    operations = [
        migrations.RunPython(populate_library, clear_library),
    ]
