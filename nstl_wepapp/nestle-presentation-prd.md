# Product Requirements Document
## Nestle Baby & Me Uzbekistan - Веб-презентация стратегии 2025-2026

### 1. Описание продукта

**Название:** Презентация цифровой стратегии Nestle Baby & Me Uzbekistan
**Тип:** Веб-презентация для показа SMM-агентствам
**Цель:** Представить стратегию цифровой трансформации для решения проблемы низкого ER
**Хостинг:** Vercel
**Доступ:** Через браузер, адаптивный дизайн

### 2. Технические требования

#### 2.1 Стек технологий
- **Сборщик:** Vite 5
- **Framework:** React 18
- **Язык:** TypeScript
- **Стили:** Tailwind CSS + shadcn/ui
- **Деплой:** Vercel (или любой статический хостинг)
- **Поддержка браузеров:** Chrome, Safari, Firefox, Edge (последние версии)

#### 2.2 Основной функционал
- Навигация клавиатурой (стрелки ←/→, Space, Enter)
- Навигация кликом (клик в любом месте = следующий слайд)
- Роутинг через URL (/slide/1, /slide/2, и т.д.)
- CSS для печати (@media print - каждый слайд на отдельной странице)
- Полноэкранный режим презентации
- Индикатор прогресса (тонкая полоса внизу)

#### 2.3 Требования к производительности
- First Contentful Paint < 1s
- Размер бандла < 500KB
- Статическая генерация всех слайдов
- Оптимизированные изображения (WebP)

### 3. Структура проекта

```
nestle-presentation/
├── src/
│   ├── App.tsx             # Главный компонент с роутингом
│   ├── main.tsx            # Entry point
│   ├── index.css           # Глобальные стили + print CSS
│   ├── components/
│   │   ├── slides/         # Все компоненты слайдов
│   │   │   ├── index.ts    # Реестр экспорта
│   │   │   ├── S01_Title.tsx
│   │   │   ├── S02_MainProblem.tsx
│   │   │   └── ... (всего 44 компонента)
│   │   ├── ui/             # shadcn/ui компоненты
│   │   ├── SlideWrapper.tsx # Общий контейнер слайда
│   │   ├── ImagePlaceholder.tsx # Плейсхолдер для изображений
│   │   └── ProgressBar.tsx # Прогресс навигации
│   ├── lib/
│   │   ├── slides.ts       # Метаданные и порядок слайдов
│   │   ├── constants.ts    # Константы (цвета бренда)
│   │   └── utils.ts        # cn() для shadcn/ui
│   └── assets/
│       └── images/         # Изображения
├── public/                 # Статические файлы
├── index.html             # HTML template
├── vite.config.ts         # Конфигурация Vite
├── tailwind.config.ts     # Tailwind + shadcn/ui тема
├── components.json        # shadcn/ui конфигурация
└── package.json
```

### 4. Полный список слайдов (44 слайда)

#### БЛОК 1: ПРОБЛЕМА И КОНТЕКСТ (7 слайдов)

**Слайд 1: Титульный**
- Файл: `S01_Title.tsx`
- Контент:
  - Логотип Nestle Baby & Me
  - Заголовок: "Стратегия цифровой трансформации 2025-2026"
  - Подзаголовок: "От доброго советника к доверенному эксперту поколений"
- Стиль: Полноэкранный градиент (синий → белый), центрированный текст

**Слайд 2: Главная проблема**
- Файл: `S02_MainProblem.tsx`
- Контент:
  - Крупный заголовок: "ER 1.20% при 46K подписчиков"
  - Подзаголовок: "Самая большая аудитория, но средняя вовлеченность"
  - Визуализация: сравнительная диаграмма (Nestle 46K = 1.20% vs Kabrita 28K = 2.21%)
- Стиль: Белый фон, акцент красным на проблеме

**Слайд 3: Расшифровка проблемы**
- Файл: `S03_ProblemDetails.tsx`
- Контент:
  - "Наша боль: низкий качественный ER и LTV"
  - Что нужно: больше сохранений, больше вопросов в DM, глубокая связь
- Стиль: Иконки для каждого пункта, минималистичный дизайн

**Слайд 4: Красная зона WHO Code**
- Файл: `S04_RedZone.tsx`
- Контент:
  - Что НЕЛЬЗЯ: смеси 1-2 ступени
  - Что МОЖНО: тоддлеры 3-4 + прикорм
  - НОВОЕ: Агентство = фильтр безопасности для UGC
- Стиль: Красные и зеленые зоны, четкое разделение

**Слайд 5: Наше уникальное преимущество**
- Файл: `S05_UniqueAdvantage.tsx`
- Контент:
  - Крупно: "20 ЛЕТ В УЗБЕКИСТАНЕ"
  - 3 поколения = 1 выбор (визуализация)
- Стиль: Эмоциональная фотография трех поколений

**Слайд 6: Две мамы - два подхода**
- Файл: `S06_TwoMothers.tsx`
- Контент:
  - Striving Researchers: логика, наука, безопасность
  - Uncompromising Pioneers: инновации, премиум, тренды
- Стиль: Сплит-экран, два персонажа

**Слайд 7: Конкурентное поле**
- Файл: `S07_CompetitiveLandscape.tsx`
- Контент:
  - Kabrita: новичок с узкой нишей
  - Nutrilak: системное образование
  - Nestle: ЕДИНСТВЕННЫЙ с историей поколений
- Стиль: Радарная диаграмма или позиционная карта

#### БЛОК 2: ОБЗОР РЫНКА И КОНКУРЕНТОВ (13 слайдов)

**Слайд 8: Ландшафт рынка - The Engagement Battlefield**
- Файл: `S08_MarketLandscape.tsx`
- Контент: Лестница ER с позициями всех игроков
- Стиль: Визуальная лестница с эмодзи медалей

**Слайд 9: Анатомия лидеров - топ-3**
- Файл: `S09_LeadersAnatomy.tsx`
- Контент: Разбор стратегий Kabrita, Nutrilak, Nestle
- Стиль: 3 колонки с ключевыми метриками

**Слайд 10: 5 работающих механик рынка**
- Файл: `S10_MarketMechanics.tsx`
- Контент: Видео доминирует, решение проблем > описание, парадокс CTA и т.д.
- Стиль: Иконки и короткие выводы

**Слайд 11: Чему учиться у конкурентов**
- Файл: `S11_CompetitorLessons.tsx`
- Контент: Конкретные тактики от каждого конкурента
- Стиль: Чек-листы с галочками

**Слайд 12: Позиция Nestle - от "витрины" к "советнику"**
- Файл: `S12_NestlePosition.tsx`
- Контент: Таблица "Сейчас → Цель" с метриками
- Стиль: Прогресс-бары для визуализации целей

**Слайды 13-20: Профили конкурентов (по 1 на каждого)**
- Файлы: `S13_Kabrita.tsx`, `S14_Nutrilak.tsx`, `S15_Agusha.tsx`, `S16_Nutrilon.tsx`, `S17_Nuppi.tsx`, `S18_FrutoNyanya.tsx`, `S19_Bebivita.tsx`
- Контент: Детальный разбор каждого конкурента из документов
- Стиль: Единый шаблон с метриками, сильными/слабыми сторонами

#### БЛОК 3: СТРАТЕГИЯ РЕШЕНИЯ (10 слайдов)

**Слайд 21: Наше стратегическое преимущество**
- Файл: `S21_StrategicAdvantage.tsx`
- Контент: "25 ЛЕТ = 3 ПОКОЛЕНИЯ ДОВЕРИЯ"
- Стиль: Эмоциональный, крупная типографика

**Слайд 22: Уникальное RTB Nestle**
- Файл: `S22_UniqueRTB.tsx`
- Контент: "МЫ НЕ ПРОДАЕМ ПРОДУКТ, МЫ ПЕРЕДАЕМ ДОВЕРИЕ"
- Стиль: Минималистичный, акцент на тексте

**Слайд 23: Big Idea**
- Файл: `S23_BigIdea.tsx`
- Контент: "КРУГ ДОВЕРИЯ Baby & Me"
- Стиль: Визуализация круга с элементами бренда

**Слайд 24: Позиционирование Baby&Me**
- Файл: `S24_BabyMePositioning.tsx`
- Контент: Роль, миссия, обещание бренда
- Стиль: Структурированный список с иконками

**Слайд 25: 4 стратегических решения**
- Файл: `S25_FourSolutions.tsx`
- Контент: UGC-конкурс, AI-бот, персонализация, контент поколений
- Стиль: 4 карточки с иконками

**Слайды 26-29: Детализация каждого решения**
- Файлы: `S26_UGCContest.tsx`, `S27_AIBot.tsx`, `S28_Personalization.tsx`, `S29_GenerationsContent.tsx`
- Контент: Подробное описание механик из документа
- Стиль: Схемы, примеры, визуализации

**Слайд 30: Tone of Voice**
- Файл: `S30_ToneOfVoice.tsx`
- Контент: Принципы коммуникации бренда
- Стиль: Примеры текстов с правильным тоном

#### БЛОК 4: ТАКТИЧЕСКАЯ РЕАЛИЗАЦИЯ (8 слайдов)

**Слайд 31: Контентные рубрики**
- Файл: `S31_ContentRubrics.tsx`
- Контент: "Круг доверия", "Голос мамы", "Как меня кормили", "Растем вместе"
- Стиль: Карточки с превью контента

**Слайд 32: Форматы для Instagram**
- Файл: `S32_InstagramFormats.tsx`
- Контент: Reels 60%, карусели, stories, посты
- Стиль: Круговая диаграмма + примеры

**Слайд 33: Telegram-стратегия**
- Файл: `S33_TelegramStrategy.tsx`
- Контент: Канал, бот, интеграция, цели
- Стиль: Схема экосистемы Telegram

**Слайд 34: Работа с педиатрами**
- Файл: `S34_DoctorsStrategy.tsx`
- Контент: Unbranded only, фокус на образовании
- Стиль: Примеры контента от врачей

**Слайд 35: Примеры креативов**
- Файл: `S35_CreativeExamples.tsx`
- Контент: 3-4 мокапа постов/reels
- Стиль: Телефоны с контентом

**Слайд 36: Community Management 3.0**
- Файл: `S36_CommunityManagement.tsx`
- Контент: Голосовые в Direct, AI первая линия
- Стиль: Схема процесса обработки запросов

**Слайд 37: Визуальная трансформация**
- Файл: `S37_VisualTransformation.tsx`
- Контент: До/после примеры визуального стиля
- Стиль: Сравнительные изображения

**Слайд 38: Механики вовлечения**
- Файл: `S38_EngagementMechanics.tsx`
- Контент: Конкурсы, челленджи, голосования, UGC
- Стиль: Timeline активностей

#### БЛОК 5: БЕЗОПАСНОСТЬ И КОНТРОЛЬ (3 слайда)

**Слайд 39: Система безопасности UGC**
- Файл: `S39_UGCSafety.tsx`
- Контент: 3-ступенчатая проверка, обучение WHO Code
- Стиль: Схема процесса проверки

**Слайд 40: Защита от рисков**
- Файл: `S40_RiskProtection.tsx`
- Контент: Сценарии и планы действий
- Стиль: Таблица риск/решение

**Слайд 41: Compliance процесс**
- Файл: `S41_ComplianceProcess.tsx`
- Контент: Еженедельные отчеты, мониторинг, реагирование
- Стиль: Чек-листы и таймлайны

#### БЛОК 6: МЕТРИКИ И РЕЗУЛЬТАТЫ (3 слайда)

**Слайд 42: KPI лестница**
- Файл: `S42_KPILadder.tsx`
- Контент: ER 1.20% → 1.80%, Video 35% → 60% и т.д.
- Стиль: Визуализация роста метрик

**Слайд 43: Как измеряем качество**
- Файл: `S43_QualityMetrics.tsx`
- Контент: Сохранения, DM, время в боте
- Стиль: Дашборд с метриками

**Слайд 44: 90-дневный план**
- Файл: `S44_90DayPlan.tsx`
- Контент: Фазы запуска по 30 дней
- Стиль: Roadmap с майлстоунами

### 5. Дизайн-система

#### 5.1 Цветовая палитра
```css
--nestle-blue: #0066CC
--nestle-light-blue: #E6F2FF
--baby-pink: #FFE6F0
--success-green: #00AA55
--danger-red: #DC3545
--text-primary: #1A1A1A
--text-secondary: #666666
--background: #FFFFFF
--gradient: linear-gradient(135deg, #0066CC 0%, #E6F2FF 100%)
```

#### 5.2 Типографика
- Заголовки: Inter Bold (48-72px)
- Подзаголовки: Inter Semibold (32-40px)
- Основной текст: Inter Regular (20-24px)
- Подписи: Inter Light (16-18px)

#### 5.3 Компоненты
- **SlideWrapper:** Общий контейнер с padding и максимальной шириной
- **ProgressBar:** Тонкая полоса прогресса внизу экрана (shadcn Progress)
- **NavigationHint:** Подсказка навигации (появляется на первом слайде)
- **ImagePlaceholder:** Плейсхолдер для изображений с lazy loading

### 5.4 Система плейсхолдеров для изображений

#### Компонент ImagePlaceholder
```typescript
interface ImagePlaceholderProps {
  src?: string;
  alt: string;
  aspectRatio?: "16/9" | "4/3" | "1/1" | "3/4";
  className?: string;
}
```

#### Варианты использования:
1. **С изображением:** Показывает реальное изображение
2. **Без изображения:** Показывает плейсхолдер с текстом "[Изображение: {alt}]"
3. **При загрузке:** Показывает скелетон из shadcn/ui

#### Типичный layout слайда с изображением:
```
┌─────────────────────────────────────┐
│  Заголовок слайда                   │
├─────────────────────────────────────┤
│                           │         │
│  Текстовый контент       │  Изобр. │
│  (60% ширины)           │  (40%)  │
│                           │         │
└─────────────────────────────────────┘
```

### 6. CSS для печати

```css
@media print {
  /* КРИТИЧНО: Показать ВСЕ слайды при печати */
  .slide {
    display: block !important; /* Переопределить display: none */
    page-break-after: always;
    page-break-inside: avoid;
    width: 100%;
    height: 100vh;
    position: relative;
    margin: 0;
    padding: 0;
  }
  
  /* Последний слайд без разрыва */
  .slide:last-child {
    page-break-after: auto;
  }
  
  /* Скрыть элементы навигации */
  .progress-bar,
  .navigation-hint,
  button,
  .navigation-controls { 
    display: none !important;
  }
  
  /* Оптимизация размеров для A4 */
  body {
    margin: 0;
    padding: 0;
    background: white;
  }
  
  /* Форсировать размер шрифтов */
  * {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
}

/* ВАЖНО: Структура HTML для печати */
/* В App.tsx нужно рендерить ВСЕ слайды в DOM, 
   но показывать только текущий через CSS */
```

### 6.1 Архитектура для печати

**Проблема:** При стандартном роутинге показывается только текущий слайд

**Решение:** Рендерить все слайды в DOM, управлять видимостью через CSS

```tsx
// App.tsx структура:
<div className="presentation">
  {slides.map((Slide, index) => (
    <div 
      key={index}
      className={`slide ${currentSlide === index ? 'active' : 'hidden'}`}
      style={{ display: currentSlide === index ? 'block' : 'none' }}
    >
      <Slide />
    </div>
  ))}
</div>

// CSS для экрана:
.slide.hidden { display: none; }
.slide.active { display: block; }

// CSS для печати переопределит это (см. выше)
```

### 7. Инструкции для разработчика

#### 7.1 Быстрый старт
```bash
# Создание проекта
npm create vite@latest nestle-presentation -- --template react-ts
cd nestle-presentation

# Установка зависимостей
npm install -D tailwindcss postcss autoprefixer
npm install react-router-dom lucide-react class-variance-authority clsx tailwind-merge

# Инициализация Tailwind
npx tailwindcss init -p

# Установка shadcn/ui
npx shadcn-ui@latest init
npx shadcn-ui@latest add button card progress skeleton
```

#### 7.2 Основные задачи

1. **КРИТИЧНО - Архитектура для печати:**
   - ВСЕ слайды должны быть в DOM одновременно
   - Управление видимостью через CSS, не через роутинг
   - При печати CSS должен показать все слайды с page-break
   
2. **Навигация:** 
   - Используйте состояние currentSlide для показа активного слайда
   - Клавиатура и клики меняют currentSlide, не URL
   - URL может синхронизироваться для шаринга (?slide=5)

3. **Компоненты слайдов:** Каждый слайд - отдельный компонент в папке components/slides

4. **Плейсхолдеры:** Создайте ImagePlaceholder компонент с fallback для отсутствующих изображений

5. **shadcn/ui:** Используйте готовые компоненты для UI элементов

6. **Оптимизация:** Lazy loading изображений, но все слайды в DOM

7. **Тестирование печати:** 
   - Откройте Ctrl+P
   - Убедитесь, что видны ВСЕ 44 слайда
   - Каждый на отдельной странице

### 8. Примеры ключевых слайдов

#### Пример 0: Правильная структура App.tsx для печати
```tsx
// КРИТИЧНО: Все слайды в DOM для печати!
function App() {
  const [currentSlide, setCurrentSlide] = useState(0);
  
  // Навигация
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowRight') setCurrentSlide(prev => Math.min(prev + 1, slides.length - 1));
      if (e.key === 'ArrowLeft') setCurrentSlide(prev => Math.max(prev - 1, 0));
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <div className="presentation">
      {/* Прогресс бар */}
      <ProgressBar current={currentSlide} total={slides.length} />
      
      {/* ВСЕ слайды рендерятся, но показывается только текущий */}
      {slides.map((SlideComponent, index) => (
        <div
          key={index}
          className={cn(
            "slide",
            currentSlide === index ? "block" : "hidden",
            // При печати CSS переопределит hidden на block
          )}
        >
          <SlideComponent />
        </div>
      ))}
    </div>
  );
}
```

#### Пример 1: Титульный слайд (S01_Title.tsx)
```tsx
// Структура компонента:
<SlideWrapper className="bg-gradient-to-br from-nestle-blue to-nestle-light-blue">
  <div className="flex items-center justify-center h-full text-center">
    <div>
      <Logo className="mx-auto mb-8" />
      <h1 className="text-6xl font-bold text-white mb-4">
        Стратегия цифровой трансформации 2025-2026
      </h1>
      <p className="text-2xl text-white/90">
        От доброго советника к доверенному эксперту поколений
      </p>
    </div>
  </div>
</SlideWrapper>
```

#### Пример 2: Слайд с плейсхолдером (S30_ToneOfVoice.tsx)
```tsx
// Структура с изображением:
<SlideWrapper>
  <h2 className="text-4xl font-bold mb-8">Tone of Voice</h2>
  <div className="grid grid-cols-5 gap-8">
    <div className="col-span-3 space-y-6">
      <Card className="p-6">
        <h3 className="font-semibold mb-2">Экспертный, но доступный</h3>
        <p>Объясняем сложное простым языком...</p>
      </Card>
      <Card className="p-6">
        <h3 className="font-semibold mb-2">Уважительный</h3>
        <p>Подчеркиваем ценность родительства...</p>
      </Card>
    </div>
    <div className="col-span-2">
      <ImagePlaceholder 
        src="/images/tone-examples.jpg"
        alt="Примеры постов с правильным тоном"
        aspectRatio="3/4"
      />
    </div>
  </div>
</SlideWrapper>
```

#### Пример 3: Слайд с метриками (S42_KPILadder.tsx)
```tsx
// Структура с прогресс-барами из shadcn:
<SlideWrapper>
  <h2 className="text-4xl font-bold mb-12">KPI лестница</h2>
  <div className="space-y-8">
    <div>
      <div className="flex justify-between mb-2">
        <span>Engagement Rate</span>
        <span>1.20% → 1.80%</span>
      </div>
      <Progress value={67} className="h-4" />
    </div>
    <div>
      <div className="flex justify-between mb-2">
        <span>Video share</span>
        <span>35% → 60%</span>
      </div>
      <Progress value={58} className="h-4" />
    </div>
  </div>
</SlideWrapper>
```

### 8.1 Рекомендуемые shadcn/ui компоненты

- **Card:** Для контентных блоков и карточек с информацией
- **Progress:** Для визуализации метрик и KPI
- **Button:** Для интерактивных элементов (если нужны)
- **Skeleton:** Для плейсхолдеров при загрузке изображений
- **Badge:** Для тегов и лейблов
- **Separator:** Для визуального разделения контента
- **Alert:** Для важных сообщений (например, WHO Code предупреждения)

### 9. Чек-лист готовности

- [ ] Vite проект настроен с React и TypeScript
- [ ] shadcn/ui компоненты установлены и работают
- [ ] Все 44 слайда созданы и работают
- [ ] **КРИТИЧНО: При печати (Ctrl+P) отображаются ВСЕ 44 слайда**
- [ ] **Каждый слайд при печати на отдельной странице**
- [ ] **Все слайды рендерятся в DOM (не только текущий)**
- [ ] Плейсхолдеры для изображений показываются корректно
- [ ] Навигация клавиатурой функционирует
- [ ] URL синхронизируется с текущим слайдом (?slide=N)
- [ ] Изображения загружаются лениво
- [ ] Проект успешно билдится для продакшена
- [ ] Презентация корректно отображается на проекторе (1920x1080)
- [ ] Мобильная версия работает (для просмотра, не презентации)