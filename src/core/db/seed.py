from datetime import datetime

CATEGORIES = [
    {
        "title": "Классика",
        "slug": "classic"
    },
    {
        "title": "Гоночные фильмы",
        "slug": "racing"
    },
    {
        "title": "Кино Балабанова",
        "slug": "balabanov"
    }
]

MOVIES = [
    {
        "title": "Апокалипсис сегодня",
        "slug": "apocalypse-now",
        "description": (
            "Путешествие в сердце войны во Вьетнаме, где грань между разумом "
            "и безумием стирается."
        ),
        "poster": "/posters/apocalypse-now.webp",
        "banner": "/banners/apocalypse-now.webp",
        "duration": 147,
        "release_date": None,
        "release_year": 1979,
        "rating_age": 18,
        "country": "США",
        "category": "classic"
    },
    {
        "title": "Славные парни",
        "slug": "goodfellas",
        "description": (
            "История о Генри Хилле — начинающем гангстере, занимающемся "
            "грабежами вместе с подельниками."
        ),
        "poster": "/posters/goodfellas.webp",
        "banner": "/banners/goodfellas.webp",
        "duration": 140,
        "release_date": None,
        "release_year": 1990,
        "rating_age": 18,
        "country": "США",
        "category": "classic"
    },
    {
        "title": "Форд против Феррари",
        "slug": "ford-v-ferrari",
        "description": (
            "История противостояния двух автомобильных гигантов и гонки "
            "за победу в Ле-Мане."
        ),
        "poster": "/posters/ford-v-ferrari.webp",
        "banner": "/banners/ford-v-ferrari.webp",
        "duration": 152,
        "release_date": None,
        "release_year": 2019,
        "rating_age": 12,
        "country": "США",
        "category": "racing"
    },
    {
        "title": "Самый быстрый Indian",
        "slug": "the-worlds-fastest-indian",
        "description": (
            "История новозеландца Берта Монро, который установил мировой "
            "рекорд скорости на мотоцикле."
        ),
        "poster": "/posters/the-worlds-fastest-indian.webp",
        "banner": "/banners/the-worlds-fastest-indian.webp",
        "duration": 127,
        "release_date": None,
        "release_year": 2005,
        "rating_age": 12,
        "country": "США, Новая Зеландия",
        "category": "racing"
    },
    {
        "title": "Топ Ган: Мэверик",
        "slug": "top-gun-maverick",
        "description": (
            "Пит Митчелл по прозвищу Мэверик более 30 лет остаётся одним из "
            "лучших пилотов ВМФ. Бесстрашный лётчик-испытатель расширяет "
            "границы возможного и старательно избегает повышения в звании, "
            "которое заставило бы его приземлиться навсегда. Однако его нрав "
            "и готовность идти на риск не приветствуется командованием. "
            "После очередного инцидента Митчелла снова отправляют в «Топ Ган», "
            "но на этот раз в качестве учителя. Ему необходимо подготовить "
            "отряд выпускников «Топ Ган» для выполнения сложнейшей и смертельно "
            "опасной миссии. Среди кандидатов Мэверик встречает Брэдли Брэдшоу — "
            "сына своего погибшего друга и напарника Ника Брэдшоу по прозвищу Гусь."
        ),
        "poster": "/posters/top-gun-maverick.webp",
        "banner": "/banners/top-gun-maverick.webp",
        "duration": 131,
        "release_date": datetime(2025, 9, 1),
        "release_year": 2022,
        "rating_age": 12,
        "country": "США",
        "category": None
    },
    {
        "title": "Оппенгеймер",
        "slug": "oppenheimer",
        "description": (
            "История жизни американского физика-теоретика Роберта Оппенгеймера, "
            "который во времена Второй мировой войны руководил Манхэттенским "
            "проектом — секретными разработками ядерного оружия."
        ),
        "poster": "/posters/oppenheimer.webp",
        "banner": "/banners/oppenheimer.webp",
        "duration": 181,
        "release_date": datetime(2025, 10, 1),
        "release_year": 2023,
        "rating_age": 16,
        "country": "США",
        "category": None
    },
    {
        "title": "Побег из Шоушенка",
        "slug": "the-shawshank-redemption",
        "description": (
            "Банкир, несправедливо осуждённый, находит свободу – и надежду – "
            "в самых тёмных стенах. История о силе духа и долгом пути к свету."
        ),
        "poster": "/posters/the-shawshank-redemption.webp",
        "banner": "/banners/the-shawshank-redemption.webp",
        "duration": 142,
        "release_date": None,
        "release_year": 1994,
        "rating_age": 18,
        "country": "США",
        "category": "classic"
    },
    {
        "title": "Зелёная миля",
        "slug": "the-green-mile",
        "description": (
            "Тюрьма смертников, чудо посреди ужаса. История о сострадании, "
            "чудесах и боли, которую несут даже самые добрые сердца."
        ),
        "poster": "/posters/the-green-mile.webp",
        "banner": "/banners/the-green-mile.webp",
        "duration": 189,
        "release_date": None,
        "release_year": 1999,
        "rating_age": 12,
        "country": "США",
        "category": "classic"
    },
    {
        "title": "Крёстный отец",
        "slug": "the-godfather",
        "description": (
            "Американская мафия. Сила семьи. Драма о том, как сын дона Корлеоне "
            "втягивается в мир, где правят честь и кровь."
        ),
        "poster": "/posters/the-godfather.webp",
        "banner": "/banners/the-godfather.webp",
        "duration": 175,
        "release_date": None,
        "release_year": 1972,
        "rating_age": 16,
        "country": "США",
        "category": "classic"
    },
    {
        "title": "Крёстный отец 2",
        "slug": "the-godfather-2",
        "description": (
            "История семьи Корлеоне продолжается: параллельно – путь юного Вито "
            "и падение Майкла."
        ),
        "poster": "/posters/the-godfather-2.webp",
        "banner": "/banners/the-godfather-2.webp",
        "duration": 202,
        "release_date": datetime(2025, 12, 31),
        "release_year": 1974,
        "rating_age": None,
        "country": "США",
        "category": None
    },
    {
        "title": "Формула-1",
        "slug": "f1",
        "description": (
            "В прошлом звезда «Формулы-1», Сонни Хейс возвращается в большой спорт "
            "спустя 30 лет, чтобы помочь команде-аутсайдеру и стать наставником "
            "молодого гонщика."
        ),
        "poster": "/posters/f1.webp",
        "banner": "/banners/f1.webp",
        "duration": 156,
        "release_date": datetime(2025, 6, 3),
        "release_year": 2025,
        "rating_age": 12,
        "country": "США",
        "category": None
    },
    {
        "title": "Форсаж: Токийский дрифт",
        "slug": "fast-and-furious-tokyo-drift",
        "description": (
            "Мир подпольных гонок, дрифта и уличной культуры Токио."
        ),
        "poster": "/posters/fast-and-furious-tokyo-drift.webp",
        "banner": "/banners/fast-and-furious-tokyo-drift.webp",
        "duration": 104,
        "release_date": None,
        "release_year": 2006,
        "rating_age": 12,
        "country": "США, Япония",
        "category": "racing"
    },
    {
        "title": "Груз 200",
        "slug": "cargo-200",
        "description": (
            "Жесткий триллер о советской провинции середины 1980-х, об убийствах, "
            "насилии и распаде системы."
        ),
        "poster": "/posters/cargo-200.webp",
        "banner": "/banners/cargo-200.webp",
        "duration": 85,
        "release_date": datetime(2025, 12, 31),
        "release_year": 2007,
        "rating_age": 18,
        "country": "Россия",
        "category": "balabanov"
    },
    {
        "title": "Солнцестояние",
        "slug": "midsommar",
        "description": (
            "Шведский культ. Летний фестиваль. Драма о группе друзей, которые "
            "попадают в загадочный мир древних ритуалов."
        ),
        "poster": "/posters/midsommar.webp",
        "banner": "/banners/midsommar.webp",
        "duration": 147,
        "release_date": datetime(2025, 10, 31),
        "release_year": 2019,
        "rating_age": 18,
        "country": "США, Швеция",
        "category": None
    },
    {
        'title': 'Интерстеллар',
        'slug': 'interstellar',
        'description': 'Путешествие сквозь червоточины и расстояния, где каждая секунда ценнее жизни.',
        'poster': '/posters/interstellar.webp',
        'banner': '/banners/interstellar.webp',
        'duration': 169,
        'release_date': datetime(2025, 12, 31),
        'release_year': 2014,
        'rating_age': 12,
        'country': 'США',
        'category': None
    },
    {
        'title': 'Форрест Гамп',
        'slug': 'forrest-gump',
        'description': 'Простой парень с чистой душой проживает эпоху перемен и сам становится их частью. Невинность, любовь и великая американская история в одном сердце.',
        'poster': '/posters/forrest-gump.webp',
        'banner': '/banners/forrest-gump.webp',
        'duration': 142,
        'release_date': None,
        'release_year': 1994,
        'rating_age': 18,
        'country': 'США',
        'category': 'classic'
    },
    {
        'title': 'Однажды в Америке',
        'slug': 'once-upon-a-time-in-america',
        'description': 'Дружба, предательство и тень гангстерской эпохи. Долгий путь от детских улиц до мрачных разборок взрослых, где прошлое всегда догоняет.',
        'poster': '/posters/once-upon-a-time-in-america.webp',
        'banner': '/banners/once-upon-a-time-in-america.webp',
        'duration': 229,
        'release_date': None,
        'release_year': 1984,
        'rating_age': 18,
        'country': 'США',
        'category': 'classic'
    },
]
