from django.db import migrations
import datetime

def populate_schedule(apps, schema_editor):
    ScheduleItem = apps.get_model('schedule', 'ScheduleItem')
    items = [
        {
            'order': 1,
            'time_start': datetime.time(8, 30),
            'time_end': datetime.time(8, 40),
            'event_name': 'Подъём',
            'short_description': 'Доброе утро! Просыпаемся под любимую музыку.',
            'detailed_description': 'Время просыпаться, приводить себя в порядок и готовиться к новому насыщенному дню в Кванте. Утреннее приветствие от дежурных вожатых.'
        },
        {
            'order': 2,
            'time_start': datetime.time(8, 40),
            'time_end': datetime.time(9, 0),
            'event_name': 'Утренняя зарядка',
            'short_description': 'Заряд бодрости и энергии на свежем воздухе.',
            'detailed_description': 'Утренняя физическая разминка на спортивной площадке. Выполняем комплекс простых упражнений для бодрости и отличного настроения.'
        },
        {
            'order': 3,
            'time_start': datetime.time(9, 0),
            'time_end': datetime.time(9, 30),
            'event_name': 'Утренний туалет и уборка комнат',
            'short_description': 'Приводим себя и свои комнаты в порядок.',
            'detailed_description': 'Личная гигиена, заправка постелей, влажная уборка в комнатах. Подготовка отрядов к утренней проверке чистоты вожатыми.'
        },
        {
            'order': 4,
            'time_start': datetime.time(9, 30),
            'time_end': datetime.time(10, 0),
            'event_name': 'Завтрак',
            'short_description': 'Вкусный и полезный завтрак в столовой.',
            'detailed_description': 'Первый прием пищи в столовой лагеря. Сбалансированное меню, богатое витаминами и углеводами для продуктивного начала учебного дня.'
        },
        {
            'order': 5,
            'time_start': datetime.time(10, 0),
            'time_end': datetime.time(13, 0),
            'event_name': 'Учебные занятия (1-й блок)',
            'short_description': 'Лекции и семинары от лучших преподавателей.',
            'detailed_description': 'Профильные занятия по математике, физике, программированию или робототехнике. Решение олимпиадных задач и обсуждение теории.'
        },
        {
            'order': 6,
            'time_start': datetime.time(13, 0),
            'time_end': datetime.time(13, 30),
            'event_name': 'Свободное время',
            'short_description': 'Отдых между занятиями и подготовка к обеду.',
            'detailed_description': 'Личное время участников: можно отдохнуть, обсудить сложные задачи с преподавателями, поиграть в настольные игры или подготовиться к обеду.'
        },
        {
            'order': 7,
            'time_start': datetime.time(13, 30),
            'time_end': datetime.time(14, 0),
            'event_name': 'Обед',
            'short_description': 'Сытный горячий обед.',
            'detailed_description': 'Полноценный обед в лагерной столовой (первое, второе, салат и напиток). Восполняем силы после интеллектуальной работы.'
        },
        {
            'order': 8,
            'time_start': datetime.time(14, 0),
            'time_end': datetime.time(15, 30),
            'event_name': 'Тихий час (Отдых)',
            'short_description': 'Время тишины, сна и чтения книг.',
            'detailed_description': 'Время обязательного отдыха в жилых корпусах. Запрещается шуметь. Можно поспать, почитать книгу или заняться спокойными делами.'
        },
        {
            'order': 9,
            'time_start': datetime.time(15, 30),
            'time_end': datetime.time(16, 0),
            'event_name': 'Полдник',
            'short_description': 'Легкий и вкусный перекус.',
            'detailed_description': 'Свежая выпечка, фрукты, йогурты, соки или чай. Легкий перекус перед вторым блоком занятий и активными играми.'
        },
        {
            'order': 10,
            'time_start': datetime.time(16, 0),
            'time_end': datetime.time(18, 0),
            'event_name': 'Спецкурсы и спортивные мероприятия',
            'short_description': 'Развивающие курсы по выбору и спортивные игры.',
            'detailed_description': 'Практические спецкурсы, проектная деятельность, а также командные игры на стадионе (футбол, волейбол, настольный теннис, бадминтон).'
        },
        {
            'order': 11,
            'time_start': datetime.time(18, 0),
            'time_end': datetime.time(19, 0),
            'event_name': 'Отрядное время и подготовка к вечеру',
            'short_description': 'Работа в отрядах, подготовка творческих номеров.',
            'detailed_description': 'Отрядные сборы, репетиции номеров для вечерних общешкольных мероприятий, оформление отрядных уголков или подготовка стенгазет.'
        },
        {
            'order': 12,
            'time_start': datetime.time(19, 0),
            'time_end': datetime.time(19, 30),
            'event_name': 'Ужин',
            'short_description': 'Вкусный вечерний прием пищи.',
            'detailed_description': 'Полноценный ужин в столовой. Готовимся к самому яркому событию дня — вечернему общешкольному мероприятию.'
        },
        {
            'order': 13,
            'time_start': datetime.time(19, 30),
            'time_end': datetime.time(21, 30),
            'event_name': 'Вечернее мероприятие',
            'short_description': 'Конкурсы, квесты, дискотеки и концерты.',
            'detailed_description': 'Главное творческое или развлекательное событие дня: интеллектуальные шоу, концерты отрядов, тематические квесты или дискотека.'
        },
        {
            'order': 14,
            'time_start': datetime.time(21, 30),
            'time_end': datetime.time(22, 0),
            'event_name': 'Второй ужин (Сонник) и вечерняя свечка',
            'short_description': 'Кефир с булочкой и душевные разговоры в отряде.',
            'detailed_description': 'Традиционный легкий поздний ужин в столовой, после которого отряды собираются в круг для обсуждения итогов дня на отрядной свечке.'
        },
        {
            'order': 15,
            'time_start': datetime.time(22, 0),
            'time_end': datetime.time(22, 30),
            'event_name': 'Подготовка к отбою и Отбой',
            'short_description': 'Вечерний туалет и подготовка ко сну.',
            'detailed_description': 'Вечерние гигиенические процедуры, подготовка ко сну. В 22:30 во всех комнатах выключается свет. Время сна и полной тишины в лагере.'
        }
    ]
    for item in items:
        ScheduleItem.objects.create(**item)

def clear_schedule(apps, schema_editor):
    ScheduleItem = apps.get_model('schedule', 'ScheduleItem')
    ScheduleItem.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_schedule, clear_schedule),
    ]
