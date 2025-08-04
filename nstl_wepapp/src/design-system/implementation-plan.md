# ПЛАН ИМПЛЕМЕНТАЦИИ NESTLE FLOW 2025

## ФАЗА 1: БАЗОВАЯ ИНФРАСТРУКТУРА (День 1)

### 1.1 Обновление глобальных стилей
```typescript
// src/styles/design-tokens.css
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

:root {
  /* OKLCH Color System */
  --nestle-blue: oklch(0.5234 0.1876 237.4521);
  --nestle-blue-light: oklch(0.9456 0.0234 237.4521);
  --nestle-blue-pastel: oklch(0.7123 0.1234 237.4521);
  --nestle-blue-dark: oklch(0.3456 0.2134 237.4521);
  
  --baby-pink: oklch(0.9567 0.0456 345.6789);
  --baby-pink-deep: oklch(0.8234 0.0789 345.6789);
  --baby-pink-vibrant: oklch(0.7456 0.1234 345.6789);
  
  --success-green: oklch(0.6789 0.1876 142.3456);
  --success-green-light: oklch(0.8901 0.0876 142.3456);
  --success-green-pastel: oklch(0.9234 0.0456 142.3456);
  
  --danger-red-soft: oklch(0.7234 0.1456 25.3456);
  --danger-red-light: oklch(0.8901 0.0789 25.3456);
  
  /* Shadows */
  --shadow-sm: 0 2px 8px oklch(0.4567 0.0234 240 / 0.04);
  --shadow-md: 0 4px 16px oklch(0.4567 0.0234 240 / 0.08);
  --shadow-lg: 0 8px 32px oklch(0.4567 0.0234 240 / 0.12);
  --shadow-xl: 0 16px 48px oklch(0.4567 0.0234 240 / 0.16);
  --shadow-2xl: 0 24px 64px oklch(0.4567 0.0234 240 / 0.20);
  
  /* Animations */
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out-expo: cubic-bezier(0.87, 0, 0.13, 1);
  --spring: cubic-bezier(0.43, 0.09, 0.38, 1.19);
}
```

### 1.2 Новая структура проекта
```
src/
├── components/
│   ├── ui/                      # Базовые UI компоненты
│   │   ├── Card/
│   │   │   ├── Card.tsx
│   │   │   ├── Card.module.css
│   │   │   └── index.ts
│   │   ├── Button/
│   │   ├── Pill/
│   │   ├── IconContainer/
│   │   ├── GlassCard/
│   │   └── AnimatedText/
│   ├── layout/                  # Компоненты макета
│   │   ├── SlideLayout/
│   │   ├── HeroLayout/
│   │   ├── ProblemSolutionLayout/
│   │   ├── FeatureLayout/
│   │   └── MetricsLayout/
│   ├── decorative/              # Декоративные элементы
│   │   ├── BackgroundShapes/
│   │   ├── FloatingElements/
│   │   ├── GradientOrb/
│   │   └── ParallaxContainer/
│   └── slides/                  # 44 слайда
│       └── [переработанные слайды]
├── hooks/                       # Кастомные хуки
│   ├── useParallax.ts
│   ├── useIntersectionObserver.ts
│   └── useMousePosition.ts
├── styles/
│   ├── design-tokens.css
│   ├── animations.css
│   └── utilities.css
└── utils/
    ├── animations.ts
    └── colors.ts
```

## ФАЗА 2: СОЗДАНИЕ БАЗОВЫХ КОМПОНЕНТОВ

### 2.1 Компонент Card с новым дизайном
```tsx
// src/components/ui/Card/Card.tsx
import React, { forwardRef } from 'react'
import { cn } from '@/lib/utils'
import styles from './Card.module.css'

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: 'default' | 'glass' | 'gradient' | 'neumorphic'
  hover?: 'lift' | 'tilt' | 'glow' | 'magnetic'
  padding?: 'sm' | 'md' | 'lg' | 'xl'
  animated?: boolean
  delay?: number
}

export const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ 
    className, 
    variant = 'default', 
    hover = 'lift',
    padding = 'lg',
    animated = true,
    delay = 0,
    children,
    ...props 
  }, ref) => {
    return (
      <div
        ref={ref}
        className={cn(
          styles.card,
          styles[`card--${variant}`],
          styles[`card--hover-${hover}`],
          styles[`card--padding-${padding}`],
          animated && styles['card--animated'],
          className
        )}
        style={{ '--animation-delay': `${delay}ms` } as React.CSSProperties}
        {...props}
      >
        {variant === 'glass' && <div className={styles.cardGlare} />}
        <div className={styles.cardContent}>
          {children}
        </div>
        {variant === 'gradient' && <div className={styles.cardShine} />}
      </div>
    )
  }
)
```

```css
/* Card.module.css */
.card {
  position: relative;
  background: var(--background-card);
  border-radius: 24px;
  box-shadow: var(--shadow-md);
  transition: all 0.4s var(--ease-out-expo);
  overflow: hidden;
}

.card--animated {
  opacity: 0;
  animation: fadeInUp 0.8s var(--ease-out-expo) forwards;
  animation-delay: var(--animation-delay);
}

.card--glass {
  background: oklch(1 0 0 / 0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid oklch(1 0 0 / 0.3);
}

.card--gradient {
  background: linear-gradient(135deg, var(--baby-pink) 0%, var(--nestle-blue-light) 100%);
  color: var(--text-primary);
}

.card--neumorphic {
  background: linear-gradient(145deg, #ffffff, #f0f0f0);
  box-shadow: 
    20px 20px 60px oklch(0.8234 0 0 / 0.15),
    -20px -20px 60px oklch(1 0 0 / 1);
}

/* Hover эффекты */
.card--hover-lift:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-xl);
}

.card--hover-tilt {
  transform-style: preserve-3d;
  transform: perspective(1000px);
}

.card--hover-tilt:hover {
  transform: perspective(1000px) rotateX(-5deg) rotateY(5deg);
}

.card--hover-glow:hover {
  box-shadow: 
    var(--shadow-xl),
    0 0 40px oklch(0.5234 0.1876 237.4521 / 0.2);
}

.card--hover-magnetic {
  transition: transform 0.3s var(--ease-out-expo);
}

/* Padding варианты */
.card--padding-sm { padding: var(--space-md); }
.card--padding-md { padding: var(--space-lg); }
.card--padding-lg { padding: var(--space-xl); }
.card--padding-xl { padding: var(--space-2xl); }

/* Декоративные элементы */
.cardGlare {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(
    45deg,
    transparent 30%,
    oklch(1 0 0 / 0.1) 50%,
    transparent 70%
  );
  transform: rotate(45deg) translateX(-100%);
  transition: transform 1.5s var(--ease-out-expo);
}

.card:hover .cardGlare {
  transform: rotate(45deg) translateX(100%);
}

.cardShine {
  position: absolute;
  top: 0;
  right: 0;
  width: 100px;
  height: 100px;
  background: radial-gradient(
    circle at center,
    oklch(1 0 0 / 0.4) 0%,
    transparent 70%
  );
  filter: blur(20px);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.card:hover .cardShine {
  opacity: 1;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### 2.2 Компонент Pill (метка)
```tsx
// src/components/ui/Pill/Pill.tsx
import React from 'react'
import { cn } from '@/lib/utils'
import styles from './Pill.module.css'

interface PillProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: 'dark' | 'light' | 'gradient' | 'outline'
  size?: 'sm' | 'md' | 'lg'
  icon?: React.ReactNode
  animated?: boolean
}

export const Pill: React.FC<PillProps> = ({
  className,
  variant = 'dark',
  size = 'md',
  icon,
  animated = false,
  children,
  ...props
}) => {
  return (
    <div
      className={cn(
        styles.pill,
        styles[`pill--${variant}`],
        styles[`pill--${size}`],
        animated && styles['pill--animated'],
        className
      )}
      {...props}
    >
      {icon && <span className={styles.pillIcon}>{icon}</span>}
      <span className={styles.pillText}>{children}</span>
    </div>
  )
}
```

### 2.3 Компонент IconContainer
```tsx
// src/components/ui/IconContainer/IconContainer.tsx
import React from 'react'
import { cn } from '@/lib/utils'
import styles from './IconContainer.module.css'

interface IconContainerProps extends React.HTMLAttributes<HTMLDivElement> {
  size?: 'sm' | 'md' | 'lg' | 'xl'
  variant?: 'gradient' | 'glass' | 'solid'
  color?: 'blue' | 'pink' | 'green'
  animated?: boolean
  pulse?: boolean
}

export const IconContainer: React.FC<IconContainerProps> = ({
  className,
  size = 'md',
  variant = 'gradient',
  color = 'blue',
  animated = true,
  pulse = false,
  children,
  ...props
}) => {
  return (
    <div
      className={cn(
        styles.container,
        styles[`container--${size}`],
        styles[`container--${variant}`],
        styles[`container--${color}`],
        animated && styles['container--animated'],
        pulse && styles['container--pulse'],
        className
      )}
      {...props}
    >
      <div className={styles.iconWrapper}>
        {children}
      </div>
      {variant === 'gradient' && <div className={styles.shimmer} />}
    </div>
  )
}
```

## ФАЗА 3: КОМПОНЕНТЫ МАКЕТА

### 3.1 SlideLayout - базовый макет слайда
```tsx
// src/components/layout/SlideLayout/SlideLayout.tsx
import React, { useEffect, useRef } from 'react'
import { cn } from '@/lib/utils'
import { useIntersectionObserver } from '@/hooks/useIntersectionObserver'
import { BackgroundShapes } from '@/components/decorative/BackgroundShapes'
import styles from './SlideLayout.module.css'

interface SlideLayoutProps {
  children: React.ReactNode
  variant?: 'default' | 'centered' | 'split' | 'hero'
  background?: 'shapes' | 'gradient' | 'dots' | 'none'
  className?: string
}

export const SlideLayout: React.FC<SlideLayoutProps> = ({
  children,
  variant = 'default',
  background = 'shapes',
  className
}) => {
  const slideRef = useRef<HTMLDivElement>(null)
  const isVisible = useIntersectionObserver(slideRef, { threshold: 0.5 })

  return (
    <div
      ref={slideRef}
      className={cn(
        styles.slide,
        styles[`slide--${variant}`],
        isVisible && styles['slide--visible'],
        className
      )}
    >
      {background === 'shapes' && <BackgroundShapes />}
      {background === 'gradient' && <div className={styles.gradientBg} />}
      {background === 'dots' && <div className={styles.dotPattern} />}
      
      <div className={styles.content}>
        {children}
      </div>
    </div>
  )
}
```

### 3.2 HeroLayout для заглавных слайдов
```tsx
// src/components/layout/HeroLayout/HeroLayout.tsx
import React from 'react'
import { SlideLayout } from '../SlideLayout'
import { GradientOrb } from '@/components/decorative/GradientOrb'
import styles from './HeroLayout.module.css'

interface HeroLayoutProps {
  logo?: React.ReactNode
  title: React.ReactNode
  subtitle?: React.ReactNode
  cta?: React.ReactNode
  decorativeElements?: boolean
}

export const HeroLayout: React.FC<HeroLayoutProps> = ({
  logo,
  title,
  subtitle,
  cta,
  decorativeElements = true
}) => {
  return (
    <SlideLayout variant="hero" background="gradient">
      <div className={styles.container}>
        {logo && (
          <div className={styles.logo}>
            {logo}
          </div>
        )}
        
        <h1 className={styles.title}>
          {title}
        </h1>
        
        {subtitle && (
          <div className={styles.subtitle}>
            {subtitle}
          </div>
        )}
        
        {cta && (
          <div className={styles.cta}>
            {cta}
          </div>
        )}
        
        {decorativeElements && (
          <>
            <GradientOrb 
              size="large" 
              color="blue" 
              position={{ bottom: -200, right: -200 }}
              animated 
            />
            <div className={styles.floatingDots}>
              <span className={styles.dot} />
              <span className={styles.dot} />
              <span className={styles.dot} />
            </div>
          </>
        )}
      </div>
    </SlideLayout>
  )
}
```

## ФАЗА 4: ДЕКОРАТИВНЫЕ КОМПОНЕНТЫ

### 4.1 BackgroundShapes
```tsx
// src/components/decorative/BackgroundShapes/BackgroundShapes.tsx
import React from 'react'
import { useParallax } from '@/hooks/useParallax'
import styles from './BackgroundShapes.module.css'

export const BackgroundShapes: React.FC = () => {
  const { x, y } = useParallax()
  
  return (
    <div className={styles.container}>
      <div 
        className={styles.shape1}
        style={{
          transform: `translate(${x * 20}px, ${y * 20}px)`
        }}
      />
      <div 
        className={styles.shape2}
        style={{
          transform: `translate(${x * -30}px, ${y * -30}px)`
        }}
      />
      <div 
        className={styles.shape3}
        style={{
          transform: `translate(${x * 15}px, ${y * -15}px)`
        }}
      />
    </div>
  )
}
```

### 4.2 GradientOrb
```tsx
// src/components/decorative/GradientOrb/GradientOrb.tsx
import React from 'react'
import { cn } from '@/lib/utils'
import styles from './GradientOrb.module.css'

interface GradientOrbProps {
  size?: 'small' | 'medium' | 'large' | 'xlarge'
  color?: 'blue' | 'pink' | 'green' | 'mixed'
  position?: {
    top?: number
    right?: number
    bottom?: number
    left?: number
  }
  animated?: boolean
  blur?: boolean
}

export const GradientOrb: React.FC<GradientOrbProps> = ({
  size = 'medium',
  color = 'blue',
  position = {},
  animated = true,
  blur = true
}) => {
  return (
    <div
      className={cn(
        styles.orb,
        styles[`orb--${size}`],
        styles[`orb--${color}`],
        animated && styles['orb--animated'],
        blur && styles['orb--blur']
      )}
      style={position}
    />
  )
}
```

## ФАЗА 5: КАСТОМНЫЕ ХУКИ

### 5.1 useParallax
```typescript
// src/hooks/useParallax.ts
import { useState, useEffect } from 'react'

export const useParallax = (factor = 1) => {
  const [position, setPosition] = useState({ x: 0, y: 0 })

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 2 * factor
      const y = (e.clientY / window.innerHeight - 0.5) * 2 * factor
      setPosition({ x, y })
    }

    window.addEventListener('mousemove', handleMouseMove)
    return () => window.removeEventListener('mousemove', handleMouseMove)
  }, [factor])

  return position
}
```

### 5.2 useIntersectionObserver
```typescript
// src/hooks/useIntersectionObserver.ts
import { useEffect, useState, RefObject } from 'react'

interface IntersectionObserverOptions {
  threshold?: number | number[]
  rootMargin?: string
}

export const useIntersectionObserver = (
  ref: RefObject<HTMLElement>,
  options: IntersectionObserverOptions = {}
): boolean => {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsVisible(entry.isIntersecting)
      },
      {
        threshold: options.threshold || 0,
        rootMargin: options.rootMargin || '0px'
      }
    )

    const element = ref.current
    if (element) {
      observer.observe(element)
    }

    return () => {
      if (element) {
        observer.unobserve(element)
      }
    }
  }, [ref, options.threshold, options.rootMargin])

  return isVisible
}
```

## ФАЗА 6: ПЕРЕРАБОТКА СЛАЙДОВ

### 6.1 Новый S01_Title
```tsx
// src/components/slides/S01_Title.tsx
import React from 'react'
import { HeroLayout } from '@/components/layout/HeroLayout'
import { GlassCard } from '@/components/ui/GlassCard'
import { AnimatedText } from '@/components/ui/AnimatedText'
import { Logo } from '@/components/ui/Logo'

export default function S01_Title() {
  return (
    <HeroLayout
      logo={<Logo variant="glass" size="large" animated />}
      title={
        <AnimatedText
          text="Стратегия цифровой трансформации"
          gradient="blue-to-pink"
          stagger={0.05}
        />
      }
      subtitle={
        <GlassCard padding="lg" animated delay={600}>
          <AnimatedText
            text="2025—2026"
            size="xl"
            weight="light"
            delay={800}
          />
          <AnimatedText
            text="От доброго советника к доверенному эксперту поколений"
            size="lg"
            color="secondary"
            delay={1000}
          />
        </GlassCard>
      }
    />
  )
}
```

### 6.2 Новый S02_MainProblem
```tsx
// src/components/slides/S02_MainProblem.tsx
import React from 'react'
import { ProblemSolutionLayout } from '@/components/layout/ProblemSolutionLayout'
import { Card } from '@/components/ui/Card'
import { Pill } from '@/components/ui/Pill'
import { MetricChart } from '@/components/ui/MetricChart'
import { IconContainer } from '@/components/ui/IconContainer'
import { TrendDown, TrendUp } from 'lucide-react'

export default function S02_MainProblem() {
  return (
    <ProblemSolutionLayout
      pill={<Pill variant="dark" icon="•••">Главная проблема</Pill>}
      title="ER 1.20% при 46K подписчиков"
      subtitle="Самая большая аудитория, но средняя вовлеченность"
    >
      <div className="grid grid-cols-2 gap-8">
        <Card variant="glass" hover="tilt" animated delay={200}>
          <div className="flex items-center justify-between mb-6">
            <div>
              <div className="text-5xl font-bold text-nestle-blue">46K</div>
              <div className="text-lg text-text-secondary">подписчиков</div>
            </div>
            <IconContainer color="blue" variant="glass">
              <TrendDown className="w-6 h-6" />
            </IconContainer>
          </div>
          
          <MetricChart
            value={1.20}
            maxValue={5}
            label="Engagement Rate"
            color="danger"
            animated
          />
          
          <div className="mt-6 text-center">
            <h3 className="text-2xl font-bold text-nestle-blue">Nestlé</h3>
            <Pill variant="outline" size="sm">Низкая вовлеченность</Pill>
          </div>
        </Card>

        <Card variant="glass" hover="tilt" animated delay={400}>
          <div className="flex items-center justify-between mb-6">
            <div>
              <div className="text-5xl font-bold">28K</div>
              <div className="text-lg text-text-secondary">подписчиков</div>
            </div>
            <IconContainer color="green" variant="glass">
              <TrendUp className="w-6 h-6" />
            </IconContainer>
          </div>
          
          <MetricChart
            value={2.21}
            maxValue={5}
            label="Engagement Rate"
            color="success"
            animated
          />
          
          <div className="mt-6 text-center">
            <h3 className="text-2xl font-bold">Kabrita</h3>
            <Pill variant="outline" size="sm">Высокая вовлеченность</Pill>
          </div>
        </Card>
      </div>
      
      <Card variant="gradient" className="mt-8" animated delay={600}>
        <div className="text-center">
          <p className="text-xl font-medium">
            🎯 Парадокс: больше подписчиков ≠ больше вовлеченности
          </p>
        </div>
      </Card>
    </ProblemSolutionLayout>
  )
}
```

## ФАЗА 7: СИСТЕМА АНИМАЦИЙ

### 7.1 Анимации появления
```css
/* src/styles/animations.css */

/* Базовые анимации */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInScale {
  from {
    opacity: 0;
    transform: scale(0.8);
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

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(60px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Продвинутые анимации */
@keyframes morphing {
  0% {
    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  }
  50% {
    border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%;
  }
  100% {
    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  33% {
    transform: translateY(-30px) rotate(-5deg);
  }
  66% {
    transform: translateY(-20px) rotate(5deg);
  }
}

@keyframes shimmer {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(200%);
  }
}

@keyframes pulse-soft {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.05);
    opacity: 0.8;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

/* Stagger анимации для списков */
.stagger-children > * {
  opacity: 0;
  animation: fadeInUp 0.6s var(--ease-out-expo) forwards;
}

.stagger-children > *:nth-child(1) { animation-delay: 0ms; }
.stagger-children > *:nth-child(2) { animation-delay: 100ms; }
.stagger-children > *:nth-child(3) { animation-delay: 200ms; }
.stagger-children > *:nth-child(4) { animation-delay: 300ms; }
.stagger-children > *:nth-child(5) { animation-delay: 400ms; }
```

### 7.2 Переходы между слайдами
```typescript
// src/utils/slideTransitions.ts
export const slideTransitions = {
  fade: {
    enter: 'opacity-0',
    enterActive: 'opacity-100 transition-opacity duration-500',
    exit: 'opacity-100',
    exitActive: 'opacity-0 transition-opacity duration-500'
  },
  
  slideLeft: {
    enter: 'translate-x-full opacity-0',
    enterActive: 'translate-x-0 opacity-100 transition-all duration-700 ease-out-expo',
    exit: 'translate-x-0 opacity-100',
    exitActive: '-translate-x-full opacity-0 transition-all duration-700 ease-in-expo'
  },
  
  scale: {
    enter: 'scale-95 opacity-0',
    enterActive: 'scale-100 opacity-100 transition-all duration-500 ease-out-expo',
    exit: 'scale-100 opacity-100',
    exitActive: 'scale-105 opacity-0 transition-all duration-500 ease-in-expo'
  },
  
  morph: {
    enter: 'scale-0 rotate-180 opacity-0',
    enterActive: 'scale-100 rotate-0 opacity-100 transition-all duration-800 ease-spring',
    exit: 'scale-100 rotate-0 opacity-100',
    exitActive: 'scale-0 -rotate-180 opacity-0 transition-all duration-800 ease-spring'
  }
}
```

## ФАЗА 8: ИНТЕГРАЦИЯ И ОПТИМИЗАЦИЯ

### 8.1 Обновленный App.tsx
```tsx
// src/App.tsx
import React, { useState, useEffect, useCallback } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { ProgressBar } from '@/components/ui/ProgressBar'
import { NavigationHint } from '@/components/ui/NavigationHint'
import { slides } from '@/lib/slides'
import { useKeyboardNavigation } from '@/hooks/useKeyboardNavigation'
import { useSwipeGesture } from '@/hooks/useSwipeGesture'
import './styles/design-tokens.css'
import './styles/animations.css'
import './styles/utilities.css'

function App() {
  const [currentSlide, setCurrentSlide] = useState(0)
  const [isTransitioning, setIsTransitioning] = useState(false)

  // Навигация
  const navigateToSlide = useCallback((index: number) => {
    if (index >= 0 && index < slides.length && !isTransitioning) {
      setIsTransitioning(true)
      setCurrentSlide(index)
      window.history.pushState(null, '', `/slide/${index + 1}`)
      
      setTimeout(() => setIsTransitioning(false), 800)
    }
  }, [isTransitioning])

  const nextSlide = () => navigateToSlide(currentSlide + 1)
  const prevSlide = () => navigateToSlide(currentSlide - 1)

  // Клавиатурная навигация
  useKeyboardNavigation({ onNext: nextSlide, onPrev: prevSlide })
  
  // Свайп жесты для мобильных
  useSwipeGesture({ onSwipeLeft: nextSlide, onSwipeRight: prevSlide })

  // URL синхронизация
  useEffect(() => {
    const path = window.location.pathname
    const match = path.match(/\/slide\/(\d+)/)
    if (match) {
      const slideNumber = parseInt(match[1], 10) - 1
      if (slideNumber >= 0 && slideNumber < slides.length) {
        setCurrentSlide(slideNumber)
      }
    }
  }, [])

  return (
    <div className="presentation">
      <ProgressBar current={currentSlide} total={slides.length} />
      
      <AnimatePresence mode="wait">
        <motion.div
          key={currentSlide}
          initial={{ opacity: 0, x: 100 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -100 }}
          transition={{ 
            duration: 0.6, 
            ease: [0.43, 0.13, 0.23, 0.96] 
          }}
          className="slide-container"
          onClick={nextSlide}
        >
          {React.createElement(slides[currentSlide])}
        </motion.div>
      </AnimatePresence>

      {currentSlide === 0 && <NavigationHint />}

      {/* Скрытые слайды для печати */}
      <div className="print-only">
        {slides.map((SlideComponent, index) => (
          <div key={index} className="print-slide">
            <SlideComponent />
          </div>
        ))}
      </div>
    </div>
  )
}

export default App
```

### 8.2 Стили для печати
```css
/* src/styles/print.css */
@media print {
  .presentation {
    display: block !important;
  }

  .print-only {
    display: block !important;
  }

  .print-slide {
    page-break-after: always;
    page-break-inside: avoid;
    width: 100%;
    height: 100vh;
    position: relative;
    display: block !important;
  }

  .print-slide:last-child {
    page-break-after: auto;
  }

  /* Скрыть интерактивные элементы */
  .progress-bar,
  .navigation-hint,
  button,
  .hover\:* {
    display: none !important;
  }

  /* Оптимизация для печати */
  * {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    color-adjust: exact;
  }

  /* Убрать анимации */
  *,
  *::before,
  *::after {
    animation: none !important;
    transition: none !important;
  }
}
```

## ROADMAP ИМПЛЕМЕНТАЦИИ

### День 1: Базовая инфраструктура
- [ ] Установка зависимостей (framer-motion, @radix-ui)
- [ ] Создание design-tokens.css с OKLCH цветами
- [ ] Настройка новой структуры папок
- [ ] Базовые утилиты и хуки

### День 2: UI компоненты
- [ ] Card со всеми вариантами
- [ ] Pill и Badge
- [ ] IconContainer
- [ ] Button и интерактивные элементы

### День 3: Компоненты макета
- [ ] SlideLayout
- [ ] HeroLayout
- [ ] ProblemSolutionLayout
- [ ] FeatureLayout

### День 4: Декоративные элементы
- [ ] BackgroundShapes
- [ ] GradientOrb
- [ ] FloatingElements
- [ ] ParallaxContainer

### День 5-7: Переработка всех 44 слайдов
- [ ] Блок 1: Проблема и контекст (слайды 1-7)
- [ ] Блок 2: Обзор рынка (слайды 8-20)
- [ ] Блок 3: Стратегическое решение (слайды 21-30)
- [ ] Блок 4: Тактическая реализация (слайды 31-38)
- [ ] Блок 5: Безопасность и контроль (слайды 39-41)
- [ ] Блок 6: Метрики и результаты (слайды 42-44)

### День 8: Финальная оптимизация
- [ ] Performance optimization
- [ ] Печать и экспорт в PDF
- [ ] Тестирование на разных устройствах
- [ ] Деплой на Vercel

Этот план создает современную, воздушную и профессиональную презентацию в стиле 2025 года!