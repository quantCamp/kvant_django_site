from django.db import migrations

def populate_faq(apps, schema_editor):
    FAQCategory = apps.get_model('faq', 'FAQCategory')
    FAQItem = apps.get_model('faq', 'FAQItem')

    # Categories
    general = FAQCategory.objects.create(name="Общие вопросы", order=1)
    academic = FAQCategory.objects.create(name="Учебный процесс", order=2)
    rules = FAQCategory.objects.create(name="Быт и правила лагеря", order=3)

    # Q&As
    FAQItem.objects.create(
        category=general,
        question="Что брать с собой в школу?",
        answer="Возьмите с собой тетради для лекций, письменные принадлежности, спортивную одежду, средства личной гигиены и хорошее настроение! Полный список рекомендованных вещей опубликован в нашей официальной группе ВКонтакте.",
        order=1
    )
    FAQItem.objects.create(
        category=general,
        question="Где территориально проходит смена?",
        answer="Летняя смена «Квант» базируется на территории благоустроенного детского оздоровительного лагеря с развитой инфраструктурой: современными корпусами, учебными классами, футбольным и баскетбольным полями, а также просторной столовой.",
        order=2
    )

    FAQItem.objects.create(
        category=academic,
        question="Какие предметы изучаются в «Кванте»?",
        answer="Основной упор сделан на физику, олимпиадную и профильную математику, информатику и основы программирования. Во второй половине дня работают творческие, научные и спортивные спецкурсы по выбору.",
        order=1
    )
    FAQItem.objects.create(
        category=academic,
        question="Будут ли оценки и экзамены?",
        answer="У нас нет классических школьных оценок или строгих экзаменов. Вместо них проводятся интересные математические бои, физические викторины, зачетная олимпиада и защита научно-исследовательских проектов.",
        order=2
    )

    FAQItem.objects.create(
        category=rules,
        question="Разрешено ли пользоваться телефонами?",
        answer="Пользоваться телефонами разрешено только во время отдыха и тишины в отрядах. Во время лекций, семинаров и общешкольных мероприятий просим выключать мобильные устройства, чтобы они не отвлекали от процесса.",
        order=1
    )
    FAQItem.objects.create(
        category=rules,
        question="Как организовано питание участников?",
        answer="В лагере предоставляется пятиразовое горячее питание (завтрак, обед, полдник, ужин, сонник) в соответствии со стандартами детского диетического питания. В меню всегда присутствуют свежие овощи, фрукты, мясо, рыба и молочные продукты.",
        order=2
    )

def clear_faq(apps, schema_editor):
    FAQCategory = apps.get_model('faq', 'FAQCategory')
    FAQCategory.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_alter_faqcategory_options_alter_faqitem_options_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_faq, clear_faq),
    ]
