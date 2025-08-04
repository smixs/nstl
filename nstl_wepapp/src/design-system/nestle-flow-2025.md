# NESTLE FLOW 2025 - Система дизайна

## 1. ФИЛОСОФИЯ ДИЗАЙНА

### Основные принципы:
- **Воздушность и простор** - много белого пространства, элементы "дышат"
- **Мягкость и округлость** - никаких острых углов, все плавное
- **Глубина через слои** - использование теней и прозрачности вместо границ
- **Органичные формы** - вдохновение природой, материнством
- **Микровзаимодействия** - плавные анимации на каждом действии

## 2. ЦВЕТОВАЯ СИСТЕМА В OKLCH

### Основная палитра:
```css
:root {
  /* Фирменные цвета Nestle в OKLCH */
  --nestle-blue: oklch(0.5234 0.1876 237.4521);           /* #0066CC */
  --nestle-blue-light: oklch(0.9456 0.0234 237.4521);    /* #E6F2FF */
  --nestle-blue-pastel: oklch(0.7123 0.1234 237.4521);   /* #4D94FF */
  
  /* Baby & Me розовые оттенки */
  --baby-pink: oklch(0.9567 0.0456 345.6789);            /* #FFE6F0 */
  --baby-pink-deep: oklch(0.8234 0.0789 345.6789);       /* #FFB8D6 */
  --baby-pink-vibrant: oklch(0.7456 0.1234 345.6789);    /* #FF85B3 */
  
  /* Успех и природа */
  --success-green: oklch(0.6789 0.1876 142.3456);        /* #00AA55 */
  --success-green-light: oklch(0.8901 0.0876 142.3456);  /* #66D998 */
  --success-green-pastel: oklch(0.9234 0.0456 142.3456); /* #B8F5D1 */
  
  /* Предупреждения */
  --danger-red-soft: oklch(0.7234 0.1456 25.3456);       /* #FF8A95 */
  --danger-red-light: oklch(0.8901 0.0789 25.3456);      /* #FFD6D9 */
  
  /* Нейтральные */
  --background-main: oklch(0.9876 0.0012 240.0000);      /* #FAFBFC */
  --background-card: oklch(1.0000 0 0);                   /* #FFFFFF */
  --text-primary: oklch(0.2345 0.0123 240.0000);         /* #1A2332 */
  --text-secondary: oklch(0.5678 0.0089 240.0000);       /* #667085 */
  --text-tertiary: oklch(0.7890 0.0056 240.0000);        /* #98A2B3 */
  
  /* Тени в OKLCH */
  --shadow-color: oklch(0.4567 0.0234 240.0000 / 0.08);
  --shadow-color-hover: oklch(0.4567 0.0234 240.0000 / 0.15);
}
```

### Градиенты:
```css
/* Фирменные градиенты */
--gradient-nestle: linear-gradient(135deg, var(--nestle-blue) 0%, var(--nestle-blue-pastel) 100%);
--gradient-baby: linear-gradient(135deg, var(--baby-pink) 0%, var(--baby-pink-vibrant) 100%);
--gradient-success: linear-gradient(135deg, var(--success-green-light) 0%, var(--success-green) 100%);
--gradient-warm: linear-gradient(135deg, var(--baby-pink) 0%, var(--nestle-blue-light) 100%);

/* Радиальные градиенты для декора */
--radial-blue: radial-gradient(circle, oklch(0.5234 0.1876 237.4521 / 0.15) 0%, transparent 70%);
--radial-pink: radial-gradient(circle, oklch(0.7456 0.1234 345.6789 / 0.10) 0%, transparent 70%);
```

## 3. ТИПОГРАФИКА

### Шрифтовая система:
```css
:root {
  /* Основной шрифт - современный и дружелюбный */
  --font-primary: 'Poppins', 'Inter', system-ui, sans-serif;
  --font-secondary: 'Plus Jakarta Sans', 'Inter', sans-serif;
  
  /* Размеры по типу */
  --text-hero: clamp(3rem, 5vw, 5rem);        /* 48-80px */
  --text-title: clamp(2.5rem, 4vw, 4rem);     /* 40-64px */
  --text-heading: clamp(2rem, 3vw, 3rem);     /* 32-48px */
  --text-subheading: clamp(1.5rem, 2vw, 2rem); /* 24-32px */
  --text-body-lg: 1.25rem;                     /* 20px */
  --text-body: 1rem;                           /* 16px */
  --text-small: 0.875rem;                      /* 14px */
  --text-tiny: 0.75rem;                        /* 12px */
  
  /* Высота строки */
  --leading-tight: 1.2;
  --leading-normal: 1.6;
  --leading-relaxed: 1.8;
  
  /* Вес шрифта */
  --font-light: 300;
  --font-regular: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
}
```

## 4. СИСТЕМА ОТСТУПОВ И СЕТКА

### Базовая единица - 8px:
```css
:root {
  --space-unit: 0.5rem; /* 8px */
  --space-xxs: calc(var(--space-unit) * 0.5);   /* 4px */
  --space-xs: var(--space-unit);                 /* 8px */
  --space-sm: calc(var(--space-unit) * 1.5);     /* 12px */
  --space-md: calc(var(--space-unit) * 2);       /* 16px */
  --space-lg: calc(var(--space-unit) * 3);       /* 24px */
  --space-xl: calc(var(--space-unit) * 4);       /* 32px */
  --space-2xl: calc(var(--space-unit) * 6);      /* 48px */
  --space-3xl: calc(var(--space-unit) * 8);      /* 64px */
  --space-4xl: calc(var(--space-unit) * 10);     /* 80px */
  --space-5xl: calc(var(--space-unit) * 12);     /* 96px */
}
```

### Контейнеры и макет:
```css
.slide-container {
  max-width: 1440px;
  padding: var(--space-4xl) var(--space-5xl);
  min-height: 100vh;
  position: relative;
  overflow: hidden;
}

/* Адаптивная сетка */
.grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: var(--space-xl);
}
```

## 5. КОМПОНЕНТНАЯ СИСТЕМА

### 5.1 Карточки (Cards)
```css
.card {
  background: var(--background-card);
  border-radius: 24px;
  padding: var(--space-xl);
  box-shadow: 0 4px 24px var(--shadow-color);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 40px var(--shadow-color-hover);
}

/* Вариации карточек */
.card--glass {
  background: oklch(1.0000 0 0 / 0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid oklch(1.0000 0 0 / 0.3);
}

.card--gradient {
  background: var(--gradient-warm);
  color: var(--background-card);
}

.card--neumorphic {
  background: linear-gradient(145deg, #ffffff, #f0f0f0);
  box-shadow: 
    20px 20px 60px oklch(0.8234 0 0 / 0.15),
    -20px -20px 60px oklch(1.0000 0 0 / 1);
}
```

### 5.2 Кнопки и интерактивные элементы
```css
.button {
  padding: var(--space-md) var(--space-xl);
  border-radius: 100px;
  font-weight: var(--font-semibold);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.button--primary {
  background: var(--gradient-nestle);
  color: white;
  box-shadow: 0 4px 16px oklch(0.5234 0.1876 237.4521 / 0.3);
}

.button--primary:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 8px 24px oklch(0.5234 0.1876 237.4521 / 0.4);
}

/* Пульсирующий эффект для CTA */
@keyframes pulse {
  0% { box-shadow: 0 0 0 0 oklch(0.5234 0.1876 237.4521 / 0.4); }
  70% { box-shadow: 0 0 0 10px oklch(0.5234 0.1876 237.4521 / 0); }
  100% { box-shadow: 0 0 0 0 oklch(0.5234 0.1876 237.4521 / 0); }
}

.button--pulse {
  animation: pulse 2s infinite;
}
```

### 5.3 Пилюли (Pills) для меток
```css
.pill {
  display: inline-flex;
  align-items: center;
  padding: var(--space-xs) var(--space-lg);
  border-radius: 100px;
  font-size: var(--text-small);
  font-weight: var(--font-medium);
  transition: all 0.3s ease;
}

.pill--dark {
  background: var(--text-primary);
  color: var(--background-card);
}

.pill--blue {
  background: oklch(0.5234 0.1876 237.4521 / 0.1);
  color: var(--nestle-blue);
  border: 1px solid oklch(0.5234 0.1876 237.4521 / 0.2);
}

.pill--gradient {
  background: var(--gradient-baby);
  color: white;
}
```

### 5.4 Иконки в контейнерах
```css
.icon-container {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--gradient-nestle);
  box-shadow: 0 8px 24px oklch(0.5234 0.1876 237.4521 / 0.3);
  transition: all 0.3s ease;
}

.icon-container:hover {
  transform: rotate(10deg) scale(1.1);
}

.icon-container--large {
  width: 80px;
  height: 80px;
}

.icon-container--glass {
  background: oklch(1.0000 0 0 / 0.1);
  backdrop-filter: blur(10px);
  border: 2px solid oklch(0.5234 0.1876 237.4521 / 0.2);
}
```

## 6. ДЕКОРАТИВНЫЕ ЭЛЕМЕНТЫ

### 6.1 Фоновые фигуры
```css
.bg-shape {
  position: absolute;
  z-index: -1;
  opacity: 0.6;
  animation: float 20s ease-in-out infinite;
}

.bg-shape--circle {
  width: 600px;
  height: 600px;
  border-radius: 50%;
  background: var(--radial-blue);
  bottom: -300px;
  right: -300px;
}

.bg-shape--blob {
  width: 400px;
  height: 400px;
  background: var(--radial-pink);
  border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
  animation: morph 15s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(10deg); }
}

@keyframes morph {
  0%, 100% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; }
  50% { border-radius: 70% 30% 50% 50% / 30% 70% 50% 50%; }
}
```

### 6.2 Разделители и акценты
```css
.divider {
  height: 1px;
  background: linear-gradient(
    to right,
    transparent,
    oklch(0.8901 0 0 / 0.3) 20%,
    oklch(0.8901 0 0 / 0.3) 80%,
    transparent
  );
  margin: var(--space-2xl) 0;
}

.accent-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--gradient-nestle);
  display: inline-block;
  margin: 0 var(--space-xs);
  animation: pulse 3s ease-in-out infinite;
}
```

## 7. АНИМАЦИИ И ПЕРЕХОДЫ

### 7.1 Появление элементов
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInScale {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-60px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Классы для использования */
.animate-in {
  animation: fadeInUp 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

.animate-in-scale {
  animation: fadeInScale 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

.animate-in-left {
  animation: slideInLeft 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

/* Задержки для последовательной анимации */
.delay-100 { animation-delay: 100ms; }
.delay-200 { animation-delay: 200ms; }
.delay-300 { animation-delay: 300ms; }
.delay-400 { animation-delay: 400ms; }
.delay-500 { animation-delay: 500ms; }
```

### 7.2 Hover эффекты
```css
/* Магнитный эффект */
.magnetic {
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.magnetic:hover {
  transform: translate(
    calc(var(--mouse-x) * 0.3),
    calc(var(--mouse-y) * 0.3)
  );
}

/* 3D поворот */
.tilt {
  transform-style: preserve-3d;
  transition: transform 0.3s ease;
}

.tilt:hover {
  transform: perspective(1000px) rotateX(-10deg) rotateY(10deg);
}
```

## 8. МАКЕТЫ СЛАЙДОВ

### 8.1 Hero слайд (заглавный)
```
┌─────────────────────────────────────────┐
│           [Logo с glass эффектом]       │
│                                         │
│     Заголовок с градиентом              │
│     в две строки                        │
│                                         │
│     [Glass карточка с подзаголовком]    │
│                                         │
│     • • •  (анимированные точки)        │
│                                         │
│ [Большой круг с градиентом справа снизу]│
└─────────────────────────────────────────┘
```

### 8.2 Проблема/Решение
```
┌─────────────────────────────────────────┐
│ [Pill: Проблема]  Заголовок слайда      │
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │   Большая карточка с проблемой      │ │
│ │   [Иконка] Описание                 │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ ┌───────┐ ┌───────┐ ┌───────┐         │
│ │Решение│ │Решение│ │Решение│         │
│ │   1   │ │   2   │ │   3   │         │
│ └───────┘ └───────┘ └───────┘         │
│                                         │
│ [Декоративный blob слева]               │
└─────────────────────────────────────────┘
```

### 8.3 Преимущества (асимметричная композиция)
```
┌─────────────────────────────────────────┐
│ [Pill] Заголовок                        │
│                                         │
│     ┌─────┐                             │
│     │Карта│    [Центральное фото        │
│     │  1  │     в круглой рамке]        │
│     └─────┘                             │
│                      ┌─────┐            │
│ ┌─────┐             │Карта│            │
│ │Карта│             │  3  │            │
│ │  2  │             └─────┘            │
│ └─────┘                                 │
│              ┌─────┐                    │
│              │Карта│                    │
│              │  4  │                    │
│              └─────┘                    │
└─────────────────────────────────────────┘
```

### 8.4 Данные и метрики
```
┌─────────────────────────────────────────┐
│ [Pill] Метрики успеха                   │
│                                         │
│ ┌─────────────┐ ┌─────────────────────┐ │
│ │             │ │  ┌─────┐             │ │
│ │   График    │ │  │ KPI │  Описание   │ │
│ │  с градиент │ │  │ 85% │  метрики    │ │
│ │   столбцами │ │  └─────┘             │ │
│ │             │ │                      │ │
│ │             │ │  ┌─────┐             │ │
│ └─────────────┘ │  │ KPI │  Описание   │ │
│                 │  │ 2.5x│  метрики    │ │
│                 │  └─────┘             │ │
│                 └─────────────────────┘ │
└─────────────────────────────────────────┘
```

## 9. ИНТЕРАКТИВНЫЕ ЭЛЕМЕНТЫ

### 9.1 Прогресс-бар
```css
.progress-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: oklch(0.9456 0 0 / 0.2);
  z-index: 100;
}

.progress-bar__fill {
  height: 100%;
  background: var(--gradient-nestle);
  transition: width 0.3s ease;
  box-shadow: 0 0 10px oklch(0.5234 0.1876 237.4521 / 0.5);
}
```

### 9.2 Навигационные подсказки
```css
.nav-hint {
  position: absolute;
  bottom: var(--space-xl);
  right: var(--space-xl);
  display: flex;
  align-items: center;
  gap: var(--space-md);
  padding: var(--space-sm) var(--space-lg);
  background: var(--background-card);
  border-radius: 100px;
  box-shadow: 0 4px 16px var(--shadow-color);
  font-size: var(--text-small);
  color: var(--text-secondary);
  animation: bounce 2s ease-in-out infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}
```

## 10. АДАПТИВНОСТЬ

### Брейкпоинты:
```css
/* Mobile First подход */
:root {
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
  --breakpoint-2xl: 1536px;
}

/* Адаптивная типографика */
@media (max-width: 768px) {
  :root {
    --text-hero: 2.5rem;
    --text-title: 2rem;
    --text-heading: 1.5rem;
    --space-unit: 0.375rem; /* 6px на мобильных */
  }
  
  .slide-container {
    padding: var(--space-xl) var(--space-lg);
  }
  
  .card {
    padding: var(--space-lg);
  }
}
```

## 11. СПЕЦИАЛЬНЫЕ ЭФФЕКТЫ

### 11.1 Параллакс на декоративных элементах
```javascript
// Добавить в App.tsx
const handleMouseMove = (e) => {
  const x = (e.clientX / window.innerWidth - 0.5) * 2;
  const y = (e.clientY / window.innerHeight - 0.5) * 2;
  
  document.documentElement.style.setProperty('--mouse-x', x);
  document.documentElement.style.setProperty('--mouse-y', y);
};
```

### 11.2 Градиентные маски для изображений
```css
.image-mask {
  -webkit-mask-image: radial-gradient(circle, black 60%, transparent 100%);
  mask-image: radial-gradient(circle, black 60%, transparent 100%);
}

.image-gradient-overlay {
  position: relative;
}

.image-gradient-overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    oklch(0.5234 0.1876 237.4521 / 0.1) 100%
  );
  pointer-events: none;
}
```

## 12. ДОСТУПНОСТЬ

### ARIA и семантика:
```html
<!-- Пример доступной карточки -->
<article class="card" role="article" aria-label="Преимущество 1">
  <div class="icon-container" aria-hidden="true">
    <svg>...</svg>
  </div>
  <h3 class="card__title">Научное наследие</h3>
  <p class="card__description">
    25 лет исследований в области детского питания
  </p>
</article>
```

### Фокус и клавиатурная навигация:
```css
:focus-visible {
  outline: 2px solid var(--nestle-blue);
  outline-offset: 4px;
  border-radius: 8px;
}

.card:focus-visible {
  transform: translateY(-6px);
  box-shadow: 
    0 12px 40px var(--shadow-color-hover),
    0 0 0 4px oklch(0.5234 0.1876 237.4521 / 0.2);
}
```

---

Этот дизайн создает современную, воздушную и профессиональную презентацию, которая передает инновационность и заботу бренда Nestle Baby & Me.