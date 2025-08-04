import { useState, useEffect } from 'react'
import { slides } from '@/components/slides'
import ProgressBar from '@/components/ProgressBar'
import { cn } from '@/lib/utils'

function App() {
  const [currentSlide, setCurrentSlide] = useState(0)

  // Навигация с клавиатуры
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
        setCurrentSlide(prev => Math.min(prev + 1, slides.length - 1))
      } else if (e.key === 'ArrowLeft') {
        setCurrentSlide(prev => Math.max(prev - 1, 0))
      }
    }
    
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [])

  // URL синхронизация
  useEffect(() => {
    const params = new URLSearchParams(window.location.search)
    const slideParam = params.get('slide')
    if (slideParam) {
      const slideIndex = parseInt(slideParam) - 1
      if (slideIndex >= 0 && slideIndex < slides.length) {
        setCurrentSlide(slideIndex)
      }
    }
  }, [])

  useEffect(() => {
    const params = new URLSearchParams(window.location.search)
    params.set('slide', String(currentSlide + 1))
    window.history.replaceState({}, '', `${window.location.pathname}?${params}`)
  }, [currentSlide])

  // Клик для следующего слайда
  const handleClick = () => {
    setCurrentSlide(prev => Math.min(prev + 1, slides.length - 1))
  }

  return (
    <div className="presentation min-h-screen bg-white">
      {/* Прогресс бар */}
      <ProgressBar current={currentSlide} total={slides.length} />
      
      {/* Подсказка навигации на первом слайде */}
      {currentSlide === 0 && (
        <div className="fixed bottom-8 left-1/2 transform -translate-x-1/2 bg-black/70 text-white px-6 py-3 rounded-full text-sm print:hidden animate-pulse">
          Используйте стрелки ← → или кликните для навигации
        </div>
      )}

      {/* КРИТИЧНО: Все слайды в DOM для печати! */}
      {slides.map((SlideComponent, index) => (
        <div
          key={index}
          className={cn(
            "slide w-full min-h-screen cursor-pointer",
            currentSlide === index ? "block" : "hidden print:block"
          )}
          onClick={handleClick}
        >
          <SlideComponent />
        </div>
      ))}
    </div>
  )
}

export default App