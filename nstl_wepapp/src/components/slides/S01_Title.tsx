import SlideWrapper from '@/components/SlideWrapper'
import ImagePlaceholder from '@/components/ImagePlaceholder'

export default function S01_Title() {
  return (
    <SlideWrapper variant="gradient">
      {/* Фоновый паттерн */}
      <div 
        className="absolute inset-0 z-0"
        style={{
          backgroundImage: `
            radial-gradient(circle at 20% 50%, rgba(0, 102, 204, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(255, 230, 240, 0.2) 0%, transparent 50%),
            radial-gradient(circle at 40% 20%, rgba(0, 170, 85, 0.05) 0%, transparent 50%)
          `
        }}
      />
      
      <div className="relative z-10 flex flex-col items-center justify-center h-full text-center">
        {/* Логотип Nestle Baby & Me */}
        <div className="mb-12 animate-fadeIn">
          <ImagePlaceholder
            src="/images/nestle-baby-me-logo.png"
            alt="Nestle Baby & Me Logo"
            aspectRatio="3/1"
            className="w-80 mx-auto drop-shadow-2xl"
          />
        </div>
        
        {/* Заголовок */}
        <div className="bg-white/95 rounded-3xl p-16 shadow-md animate-slideUp">
          <h1 className="text-3xl md:text-4xl lg:text-5xl font-bold mb-6 leading-tight text-[var(--color-primary-dark)]">
            Стратегия цифровой<br />трансформации
          </h1>
          
          {/* Год */}
          <div className="text-xl md:text-2xl lg:text-3xl font-light text-gray-700 mb-6 tracking-wider">
            2025—2026
          </div>
          
          {/* Подзаголовок */}
          <p className="text-base md:text-lg lg:text-xl text-gray-600 max-w-2xl leading-relaxed">
            От доброго советника к доверенному эксперту поколений
          </p>
        </div>
        
        {/* Декоративный элемент внизу */}
        <div className="absolute bottom-[10%] left-1/2 transform -translate-x-1/2">
          <div className="flex items-center space-x-4">
            <div className="w-3 h-3 bg-white rounded-full animate-pulse shadow-md"></div>
            <div className="w-2.5 h-2.5 bg-white/70 rounded-full animate-pulse animation-delay-200 shadow-md shadow-white/30"></div>
            <div className="w-2 h-2 bg-white/40 rounded-full animate-pulse animation-delay-400 shadow-sm shadow-white/20"></div>
          </div>
        </div>
        
        {/* Навигационная подсказка на первом слайде */}
        <div className="absolute bottom-8 right-[10%] text-white/60 text-sm animate-bounce">
          Используйте стрелки ← → или кликните для навигации
        </div>
      </div>
    </SlideWrapper>
  )
}