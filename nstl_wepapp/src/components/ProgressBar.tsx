import { cn } from '@/lib/utils'

interface ProgressBarProps {
  current: number
  total: number
  className?: string
}

export default function ProgressBar({ current, total, className }: ProgressBarProps) {
  const progress = ((current + 1) / total) * 100

  return (
    <div className={cn("fixed bottom-0 left-0 right-0 z-50 print:hidden", className)}>
      {/* Progress bar background */}
      <div className="h-1 bg-gray-200/50 backdrop-blur-sm">
        <div 
          className="h-full bg-gradient-to-r from-[var(--color-primary)] to-[var(--color-primary-dark)] transition-all duration-500 ease-out"
          style={{ width: `${progress}%` }}
        />
      </div>
      
      {/* Slide counter */}
      <div className="absolute bottom-2 right-4 text-xs text-gray-500 bg-white/90 backdrop-blur-sm px-2 py-1 rounded-full shadow-sm">
        {current + 1} / {total}
      </div>
    </div>
  )
}