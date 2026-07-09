import os
import shutil
import datetime
import django

# Setup django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quant_site.settings')
django.setup()

from about.models import SchoolApplication
from courses.models import Course
from faq.models import FAQCategory, FAQItem
from gallery.models import Album, Photo
from library.models import Category, Material
from news.models import NewsArticle, Comment
from schedule.models import ScheduleItem
from teachers.models import Teacher, TeacherFeedBack

print("Cleaning database...")
Comment.objects.all().delete()
NewsArticle.objects.all().delete()
Photo.objects.all().delete()
Album.objects.all().delete()
Material.objects.all().delete()
Category.objects.all().delete()
FAQItem.objects.all().delete()
FAQCategory.objects.all().delete()
ScheduleItem.objects.all().delete()
TeacherFeedBack.objects.all().delete()
Course.objects.all().delete()
Teacher.objects.all().delete()
SchoolApplication.objects.all().delete()
print("Cleaned!")

# Prepare media directory paths
media_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')
os.makedirs(os.path.join(media_root, 'teachers'), exist_ok=True)
os.makedirs(os.path.join(media_root, 'news'), exist_ok=True)
os.makedirs(os.path.join(media_root, 'gallery'), exist_ok=True)
os.makedirs(os.path.join(media_root, 'achievements'), exist_ok=True)
os.makedirs(os.path.join(media_root, 'library'), exist_ok=True)

# Helper to copy placeholders or make dummy images
placeholder_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'img', 'teachers', 'teacher_placeholder.png')

def copy_image(relative_path):
    dest = os.path.join(media_root, relative_path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(placeholder_src):
        shutil.copy(placeholder_src, dest)
        print(f"Copied placeholder to {relative_path}")
    else:
        # Create a dummy 1x1 PNG file if placeholder is not found
        with open(dest, 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15c4\x00\x00\x00\rIDATx\x9cc`\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82')
        print(f"Created dummy image at {relative_path}")

def create_dummy_file(relative_path, content=b"Dummy PDF Content"):
    dest = os.path.join(media_root, relative_path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, 'wb') as f:
        f.write(content)
    print(f"Created dummy document at {relative_path}")

print("Seeding Teachers...")
copy_image("teachers/kalacheva.jpg")
teacher_kalacheva = Teacher.objects.create(
    first_name="Наталья",
    last_name="Калачева",
    patronymic="Вячеславовна",
    age=45,
    photo="teachers/kalacheva.jpg",
    short_info="Директор ЛФМШ «Квант», к.п.н., доцент",
    bio="Кандидат педагогических наук, доцент кафедры математических методов в геологии Института геологии и нефтегазовых технологий КФУ. Руководит летней физико-математической школой «Квант».",
    achievments="Кандидат педагогических наук, Дипломант Всероссийских конкурсов программ организации отдыха детей.",
    contact_email="kvant@kpfu.ru"
)

copy_image("teachers/sochneva.jpg")
teacher_sochneva = Teacher.objects.create(
    first_name="Валентина",
    last_name="Сочнева",
    patronymic="Алексеевна",
    age=80,
    photo="teachers/sochneva.jpg",
    short_info="Научный руководитель ЛФМШ «Квант», к.ф.-м.н., доцент",
    bio="Основатель и научный руководитель школы «Квант» с 1972 года. Кандидат физико-математических наук, доцент кафедры общей математики Института математики и механики им. Н.И.Лобачевского КФУ.",
    achievments="Заслуженный работник высшей школы РФ, Кавалер ордена Дружбы, основатель олимпиадного движения в РТ.",
    contact_email="vsochneva@kpfu.ru"
)

copy_image("teachers/abzalilov.jpg")
teacher_abzalilov = Teacher.objects.create(
    first_name="Дамир",
    last_name="Абзалилов",
    patronymic="Фидаилевич",
    age=50,
    photo="teachers/abzalilov.jpg",
    short_info="Преподаватель математики, д.ф.-м.н.",
    bio="Доктор физико-математических наук, профессор Института математики и механики им. Н.И. Лобачевского КФУ. Известный специалист в области математического моделирования и теории графов.",
    achievments="Доктор физико-математических наук, автор более 100 научных трудов.",
    contact_email="damir.abzalilov@kpfu.ru"
)

copy_image("teachers/romanenko.jpg")
teacher_romanenko = Teacher.objects.create(
    first_name="Алексей",
    last_name="Романенко",
    patronymic="Дмитриевич",
    age=28,
    photo="teachers/romanenko.jpg",
    short_info="Преподаватель олимпиадной математики",
    bio="Выпускник школы «Квант», аспирант и ассистент кафедры общей математики КФУ. Ведет факультативы по решению сложных задач с модулями и параметрами.",
    achievments="Многократный призер студенческих олимпиад по математике, куратор математического направления ЛФМШ «Квант».",
    contact_email="alexey.romanenko@kpfu.ru"
)

copy_image("teachers/ivanov.jpg")
teacher_ivanov = Teacher.objects.create(
    first_name="Сергей",
    last_name="Иванов",
    patronymic="Петрович",
    age=35,
    photo="teachers/ivanov.jpg",
    short_info="Преподаватель физики, к.ф.-м.н.",
    bio="Кандидат физико-математических наук, старший научный сотрудник Института физики КФУ. Специализируется на экспериментальной и олимпиадной физике.",
    achievments="Лауреат грантов поддержки молодых ученых, автор курсов по экспериментальной физике.",
    contact_email="sergey.ivanov@kpfu.ru"
)

copy_image("teachers/smirnov.jpg")
teacher_smirnov = Teacher.objects.create(
    first_name="Антон",
    last_name="Смирнов",
    patronymic="Игоревич",
    age=26,
    photo="teachers/smirnov.jpg",
    short_info="Преподаватель программирования и веб-разработки",
    bio="Разработчик в крупной IT-компании, выпускник школы «Квант». Преподает веб-разработку на Python и олимпиадное программирование.",
    achievments="Призер четвертьфинала ACM ICPC, сертифицированный Django-разработчик.",
    contact_email="anton.smirnov@kpfu.ru"
)

print("Seeding Courses...")
course_physics = Course.objects.create(
    title="Физика (6–10 классы)",
    short_description="Базовые понятия физики, механики и гидростатики, знакомство с экспериментом.",
    description=(
        "Основная задача курса – первое знакомство со школьным предметом Физика. "
        "В рамках курса школьники узнают, как с помощью приемов логики, рассуждения, наблюдения "
        "получить знания об окружающем мире; познакомятся с базовыми понятиями физики, такими как сила, "
        "вектор, равновесие, рычаги, блоки; узнают, чем эксперимент отличается от простого наблюдения; "
        "научатся выводить закономерности механики. Лабораторные работы, запланированные в этом курсе, "
        "наглядно покажут, как с помощью наблюдений и измерений можно подтвердить или опровергнуть научные гипотезы, "
        "познакомят с основами статистической обработки результатов измерений."
    ),
    icon="⚡"
)
course_physics.teachers.add(teacher_ivanov)

course_olympiad_physics = Course.objects.create(
    title="Олимпиадная физика (8, 10 классы)",
    short_description="Подготовка к олимпиадам высокого уровня, олимпиадный практикум.",
    description=(
        "Наша программа – это переход на качественно новый уровень понимания физики. "
        "Мы сфокусируемся на том, что нужно будущему призёру и студенту топового вуза: "
        "Детально разберём ключевые разделы физики 8, 9, 10 и 11 класса (механика, МКТ, термодинамика, "
        "основы электродинамики), уделяя внимание самым сложным аспектам. "
        "Практические занятия будут посвящены сложным экспериментальным задачам по механике, оптике, электромагнетизму."
    ),
    icon="⚛️"
)
course_olympiad_physics.teachers.add(teacher_ivanov, teacher_sochneva)

course_math = Course.objects.create(
    title="Математика (6–10 классы)",
    short_description="Углубление знаний в комбинаторике, теории множеств, арифметике остатков и геометрии.",
    description=(
        "Курс по математике посвящен углублению и расширению знаний по ключевым разделам математики, "
        "традиционно вызывающим трудности у школьников: комбинаторика, теория множеств, теория делимости "
        "и основы алгебры многочленов. После обучения у учащихся будет сформирована культура математического рассуждения, "
        "они научатся видеть логические связи между широким спектром сфер математики и применять полученные знания "
        "для решения нестандартных задач."
    ),
    icon="📐"
)
course_math.teachers.add(teacher_sochneva, teacher_romanenko, teacher_abzalilov)

course_olympiad_prog = Course.objects.create(
    title="Олимпиадное программирование (7–10 классы)",
    short_description="Изучение классических алгоритмов, структур данных и участие в онлайн-контестах.",
    description=(
        "Программа рассчитана на школьников, принимающих участие в олимпиадах и конкурсах по информатике "
        "и желающих углубить свои знания в области алгоритмов. В лаборатории школьники изучат классические алгоритмы, "
        "научатся оценивать их эффективность и применять для решения сложных олимпиадных задач на языках C++ или Python. "
        "Практика проходит в виде тематических онлайн-контестов на базе платформы Codeforces."
    ),
    icon="💻"
)
course_olympiad_prog.teachers.add(teacher_smirnov)

course_web_dev = Course.objects.create(
    title="Веб-разработка на Python (7–10 классы)",
    short_description="Создание веб-сервисов с помощью фреймворка Django и верстки HTML/CSS.",
    description=(
        "Программа предназначена для школьников, желающих познакомиться с промышленной веб-разработкой. "
        "Участники пройдут путь от написания простых скриптов до создания полноценных веб-сервисов с "
        "серверной логикой (backend) и визуальным интерфейсом (frontend). Курс ориентирован на получение "
        "практических навыков создания реальных IT-продуктов с использованием фреймворка Django."
    ),
    icon="🌐"
)
course_web_dev.teachers.add(teacher_smirnov)

course_diff_eq = Course.objects.create(
    title="Дифференциальные уравнения (10 класс)",
    short_description="Применение математического аппарата для моделирования реальных процессов.",
    description=(
        "Задача курса – научиться применять математику для изучения самых разных наук: от биологии и физики "
        "до экономики и социологии. Мы погрузимся в увлекательный процесс исследования явлений и процессов "
        "через призму математических моделей, выраженных в виде дифференциальных уравнений и систем. "
        "В программу включены: понятие производной, интеграла, линейные дифференциальные уравнения, "
        "модели Мальтуса и Ферхюльста, модель 'хищник-жертва' и др."
    ),
    icon="📈"
)
course_diff_eq.teachers.add(teacher_sochneva, teacher_abzalilov)

print("Seeding Schedule...")
schedule_data = [
    (1, datetime.time(7, 15), None, "Подъём", "Утро начинается с бодрого настроения", "Утро в ЛФМШ «Квант» начинается в 7:15. Все участники просыпаются, заправляют постели и готовятся к зарядке."),
    (2, datetime.time(7, 30), datetime.time(7, 55), "Зарядка", "Спортивная зарядка для бодрости на весь день", "Зарядка проводится вожатыми на свежем воздухе. Включает разминку, пробежку и комплекс физических упражнений для подготовки организма к продуктивному учебному дню."),
    (3, datetime.time(8, 0), datetime.time(8, 45), "Завтрак. Уборка. Подготовка к занятиям", "Вкусный и сбалансированный завтрак, уборка комнат", "Завтрак в столовой лагеря. После завтрака школьники возвращаются в свои комнаты для наведения порядка и подготовки учебных принадлежностей к занятиям."),
    (4, datetime.time(9, 0), datetime.time(9, 30), "Линейка", "Утренний сбор лагеря, анонсы и награждения", "Традиционная утренняя линейка: подъем флага, объявление планов на день, анонсы вечерних мероприятий и награждение победителей вчерашних соревнований."),
    (5, datetime.time(10, 0), datetime.time(11, 20), "Учебное занятие №1", "Первая профильная пара в лабораториях", "Основное учебное занятие по направлениям: физика, математика, информатика в соответствии с программой выбранной лаборатории."),
    (6, datetime.time(11, 30), datetime.time(12, 50), "Учебное занятие №2", "Вторая профильная пара в лабораториях", "Продолжение профильных занятий, практическая работа, олимпиадный разбор или экспериментальная часть курса."),
    (7, datetime.time(13, 0), datetime.time(13, 45), "Обед", "Сытный комплексный обед", "Горячий обед в столовой, восполняющий силы после умственной нагрузки на занятиях."),
    (8, datetime.time(13, 45), datetime.time(14, 30), "Свободное время", "Время для отдыха и общения", "Личное время школьников, которое они могут потратить на отдых, звонки родителям, настольные игры или прогулки по территории лагеря."),
    (9, datetime.time(14, 30), datetime.time(15, 50), "Учебное занятие №3", "Третья учебная пара / Курс по выбору", "Специальный курс по выбору для старших классов, или обязательное практическое занятие в соответствии с программой лаборатории."),
    (10, datetime.time(16, 0), datetime.time(16, 15), "Полдник", "Легкий перекус", "Полдник: свежие фрукты, выпечка, сок или чай."),
    (11, datetime.time(16, 30), datetime.time(18, 45), "Факультативы. Турниры. Спортивные мероприятия", "Спортивные игры, клубы, интеллектуальные факультативы", "Занятия по интересам во второй половине дня: спортивные секции (волейбол, футбол, бадминтон, лапта, ринго, настольный теннис), интеллектуальные факультативы, творческие кружки (фото, настолки, шахматы)."),
    (12, datetime.time(19, 0), datetime.time(20, 0), "Ужин", "Вечерний прием пищи в столовой", "Ужин в столовой лагеря. Обсуждение планов на вечер."),
    (13, datetime.time(20, 30), datetime.time(22, 0), "Концерты. КВН. Конкурсы. Вечерний кинозал", "Культурно-массовая программа", "Вечерняя развлекательная программа: дискотеки, концерты, подготовленные вожатыми и школьниками, игры КВН, интеллектуальные конкурсы «Что? Где? Когда?», песенный фестиваль «Квантовидение»."),
    (14, datetime.time(22, 0), datetime.time(22, 30), "Подготовка ко сну", "Гигиенические процедуры, подготовка ко сну", "Школьники готовятся ко сну, принимают душ, наводят порядок в комнатах."),
    (15, datetime.time(23, 0), None, "Отбой", "Время сна и восстановления сил", "В лагере гасится свет, наступает тишина. Отбой.")
]

for order, t_start, t_end, name, s_desc, d_desc in schedule_data:
    ScheduleItem.objects.create(
        order=order,
        time_start=t_start,
        time_end=t_end,
        event_name=name,
        short_description=s_desc,
        detailed_description=d_desc
    )

print("Seeding FAQ...")
faq_cat1 = FAQCategory.objects.create(name="Поступление и отбор", order=1)
FAQItem.objects.create(
    category=faq_cat1,
    question="Кто может стать участником школы «Квант»?",
    answer="Участие в программе Летней школы «Квант» могут принять школьники, заканчивающие 6–10 классы, увлеченные физикой, математикой и информатикой, участники олимпиад, конкурсов, конференций.",
    order=1
)
FAQItem.objects.create(
    category=faq_cat1,
    question="Как осуществляется набор в школу?",
    answer="Набор осуществляется на конкурсной основе по направлениям: физика, олимпиадная физика, математика, олимпиадное программирование и веб-разработка. Для поступления необходимо заполнить заявку на сайте и прикрепить портфолио достижений.",
    order=2
)

faq_cat2 = FAQCategory.objects.create(name="Условия и проживание", order=2)
FAQItem.objects.create(
    category=faq_cat2,
    question="Где территориально будет проходить школа в 2026 году?",
    answer="Летняя физико-математическая школа «Квант» будет проходить на базе ДОЛ «Ландыш» ПАО «Татнефть» (Лениногорский район, Республика Татарстан, с. Глазово).",
    order=1
)
FAQItem.objects.create(
    category=faq_cat2,
    question="Какова стоимость путевки?",
    answer="Для школьников, обучающихся в Республике Татарстан, участие в программе бесплатное. Школьники из других регионов РФ могут быть зачислены на платной основе при наличии свободных мест. Стоимость путевки для них определяется оргкомитетом.",
    order=2
)

faq_cat3 = FAQCategory.objects.create(name="Обучение и досуг", order=3)
FAQItem.objects.create(
    category=faq_cat3,
    question="Какая учебная нагрузка ожидает ребят?",
    answer="Каждый день ребят ждут три учебных занятия по 80 минут (согласно распорядку дня), а также обязательный курс экспериментальной физики или математический практикум.",
    order=1
)
FAQItem.objects.create(
    category=faq_cat3,
    question="Чем заняты дети во второй половине дня?",
    answer="Во второй половине дня работают кружки по интересам (настольные игры, шахматы, фото), проводятся спортивные соревнования (футбол, волейбол, бадминтон, лапта), а вечером – культурно-массовые мероприятия (КВН, ЧГК, песенный конкурс Квантовидение, дискотеки).",
    order=2
)

print("Seeding Library...")
lib_cat1 = Category.objects.create(name="Книги и учебники")
create_dummy_file("library/math_6_lectures.pdf", b"Lectures on math for 6th grade")
Material.objects.create(
    title="Лекции по математике для 6 класса",
    description="Сборник лекций по комбинаторике, теории множеств и делимости чисел.",
    material_type="file",
    file="library/math_6_lectures.pdf",
    category=lib_cat1
)

create_dummy_file("library/physics_olympiad.pdf", b"Physics olympiad problems with answers")
Material.objects.create(
    title="Олимпиадные задачи по физике",
    description="Книга с подборкой олимпиадных задач прошлых лет с решениями.",
    material_type="file",
    file="library/physics_olympiad.pdf",
    category=lib_cat1
)

lib_cat2 = Category.objects.create(name="Презентации курсов")
Material.objects.create(
    title="Презентация курса веб-разработки на Django",
    description="Слайды вводного занятия по клиент-серверной архитектуре и основам Django.",
    material_type="link",
    link="https://django-intro-presentation.kpfu.ru",
    category=lib_cat2
)

lib_cat3 = Category.objects.create(name="Домашние задания")
Material.objects.create(
    title="Контест по динамическому программированию",
    description="Ссылка на тренировочный контест по теме ДП на платформе Codeforces.",
    material_type="link",
    link="https://codeforces.com/group/kvant-dp-contest",
    category=lib_cat3
)

print("Seeding News...")
copy_image("news/start_55.jpg")
article_1 = NewsArticle.objects.create(
    title="Старт 55-й Летней школы «Квант»!",
    text=(
        "С радостью объявляем о начале работы 55-й Летней физико-математической школы «Квант»! "
        "В этом году наша смена проходит на базе прекрасного ДОЛ «Ландыш» в Лениногорском районе. "
        "К нам приехали более 150 талантливых школьников со всей республики и других регионов России. "
        "Впереди 18 дней интенсивной учебы, увлекательных экспериментов, лекций ведущих ученых КФУ "
        "и ярких вечерних мероприятий. Всем удачи, новых открытий и крепкой квантовской дружбы!"
    ),
    img="news/start_55.jpg"
)

copy_image("news/opening.jpg")
article_2 = NewsArticle.objects.create(
    title="Вечерний концерт-открытие и первые лекции",
    text=(
        "Вчера в лагере прошло торжественное открытие смены. Вожатые и школьники подготовили зажигательные "
        "творческие номера. А уже сегодня с утра начались первые учебные занятия в лабораториях. "
        "Научный руководитель школы Валентина Алексеевна Сочнева прочитала лекцию об истории школы и олимпиадном движении. "
        "Школьники направления «Веб-разработка» создали свои первые HTML-странички, а физики приступили к "
        "экспериментальным лабораторным работам по кинематике."
    ),
    img="news/opening.jpg"
)

copy_image("news/kvantovision.jpg")
article_3 = NewsArticle.objects.create(
    title="Квантовидение-2026: как это было",
    text=(
        "Завершился один из самых долгожданных творческих конкурсов школы – песенный фестиваль «Квантовидение». "
        "В этом году ребята продемонстрировали невероятный уровень подготовки, представив оригинальные аранжировки "
        "и авторские песни о квантовской жизни. Победителем стал сводный хор лаборатории «Олимпиадная физика-10» "
        "с песней, посвященной дифференциальным уравнениям. Поздравляем победителей!"
    ),
    img="news/kvantovision.jpg"
)

# Comments
Comment.objects.create(
    article=article_1,
    text="Ура! Наконец-то Квант!"
)
Comment.objects.create(
    article=article_1,
    text="Ландыш — отличный лагерь, очень завидую ребятам!"
)
Comment.objects.create(
    article=article_1,
    text="Желаю всем отличной смены и успешной сдачи зачетов!"
)

Comment.objects.create(
    article=article_3,
    text="Песня про диффуры — это шедевр! Будем петь ее весь год."
)
Comment.objects.create(
    article=article_3,
    text="Все выступили просто супер, спасибо вожатым за помощь в подготовке!"
)

print("Seeding Gallery...")
copy_image("gallery/opening_cover.jpg")
album_1 = Album.objects.create(
    title="Открытие смены Квант-2026",
    description="Фотоотчет с торжественного открытия 55-й Летней школы «Квант» на базе ДОЛ «Ландыш».",
    cover_image="gallery/opening_cover.jpg"
)

copy_image("gallery/opening_1.jpg")
Photo.objects.create(
    album=album_1,
    img="gallery/opening_1.jpg",
    caption="Построение на линейке открытия"
)

copy_image("gallery/opening_2.jpg")
Photo.objects.create(
    album=album_1,
    img="gallery/opening_2.jpg",
    caption="Выступление вожатых с приветственным танцем"
)

copy_image("gallery/opening_3.jpg")
Photo.objects.create(
    album=album_1,
    img="gallery/opening_3.jpg",
    caption="Общее фото отрядов"
)

copy_image("gallery/study_cover.jpg")
album_2 = Album.objects.create(
    title="Будни лабораторий и эксперименты",
    description="Учебные занятия, лабораторные работы по физике и программированию.",
    cover_image="gallery/study_cover.jpg"
)

copy_image("gallery/study_1.jpg")
Photo.objects.create(
    album=album_2,
    img="gallery/study_1.jpg",
    caption="Лабораторная работа по механике в действии"
)

copy_image("gallery/study_2.jpg")
Photo.objects.create(
    album=album_2,
    img="gallery/study_2.jpg",
    caption="Разбор олимпиадной задачи на доске"
)

copy_image("gallery/study_3.jpg")
Photo.objects.create(
    album=album_2,
    img="gallery/study_3.jpg",
    caption="Кодинг на Python в компьютерном классе"
)

print("Seeding Applications...")
copy_image("achievements/diploma1.jpg")
SchoolApplication.objects.create(
    parent_name="Петров Иван Сергеевич",
    student_name="Петров Алексей Иванович",
    student_age=14,
    phone="+79172223344",
    email="petrov@mail.ru",
    achievements="achievements/diploma1.jpg"
)

copy_image("achievements/diploma2.jpg")
SchoolApplication.objects.create(
    parent_name="Сидорова Анна Дмитриевна",
    student_name="Сидорова Мария Алексеевна",
    student_age=12,
    phone="+79875556677",
    email="sidorova@yandex.ru",
    achievements="achievements/diploma2.jpg"
)

print("Seeding Teacher Feedback...")
TeacherFeedBack.objects.create(
    teacher=teacher_sochneva,
    question="Валентина Алексеевна, подскажите, пожалуйста, какой учебник по матанализу лучше всего почитать перед сменой?"
)
TeacherFeedBack.objects.create(
    teacher=teacher_smirnov,
    question="Антон Игоревич, будет ли на курсе Django изучаться интеграция с внешними API?"
)

print("Database seeded successfully!")
