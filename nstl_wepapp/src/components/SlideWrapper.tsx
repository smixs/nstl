import { ReactNode } from 'react'
import { cn } from '@/lib/utils'
import BackgroundShapes from '@/components/decorative/BackgroundShapes'

interface SlideWrapperProps {
  children: ReactNode
  className?: string
  variant?: 'default' | 'gradient' | 'dark'
  showShapes?: boolean
}

export default function SlideWrapper({ 
  children, 
  className,
  variant = 'default',
  showShapes = true 
}: SlideWrapperProps) {
  const variants = {
    default: 'bg-background-main text-text-primary',
    gradient: 'bg-gradient-to-br from-nestle-blue via-nestle-blue-pastel to-nestle-light-blue text-white',
    dark: 'bg-text-primary text-white'
  }

  return (
    <div className={cn(
      "w-full h-screen flex flex-col overflow-hidden relative",
      variants[variant],
      className
    )}>
      {/* Background decorative shapes */}
      {showShapes && variant === 'default' && <BackgroundShapes />}
      
      {/* Main content area with 10% padding from edges */}
      <div className="flex-1 flex flex-col justify-center px-[10%] py-[10%] relative z-10">
        <div className="max-w-7xl mx-auto w-full">
          {children}
        </div>
      </div>
    </div>
  )
}