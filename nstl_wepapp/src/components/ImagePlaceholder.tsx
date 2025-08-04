import { useState } from 'react'
import { cn } from '@/lib/utils'

interface ImagePlaceholderProps {
  src?: string
  alt: string
  aspectRatio?: '16/9' | '4/3' | '1/1' | '3/4' | '3/1'
  className?: string
}

export default function ImagePlaceholder({
  src,
  alt,
  aspectRatio = '16/9',
  className
}: ImagePlaceholderProps) {
  const [isLoading, setIsLoading] = useState(true)
  const [hasError, setHasError] = useState(false)

  const aspectRatioClasses = {
    '16/9': 'aspect-[16/9]',
    '4/3': 'aspect-[4/3]',
    '1/1': 'aspect-square',
    '3/4': 'aspect-[3/4]',
    '3/1': 'aspect-[3/1]'
  }

  if (!src || hasError) {
    return (
      <div 
        className={cn(
          "bg-gray-100 rounded-lg flex items-center justify-center",
          aspectRatioClasses[aspectRatio],
          className
        )}
      >
        <div className="text-center p-8">
          <svg
            className="mx-auto h-12 w-12 text-gray-400 mb-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
            />
          </svg>
          <p className="text-gray-500 text-sm">[Изображение: {alt}]</p>
        </div>
      </div>
    )
  }

  return (
    <div className={cn("relative overflow-hidden rounded-lg", aspectRatioClasses[aspectRatio], className)}>
      {isLoading && (
        <div className="absolute inset-0 bg-gray-200 animate-pulse" />
      )}
      <img
        src={src}
        alt={alt}
        onLoad={() => setIsLoading(false)}
        onError={() => {
          setIsLoading(false)
          setHasError(true)
        }}
        className={cn(
          "w-full h-full object-cover",
          isLoading && "opacity-0"
        )}
      />
    </div>
  )
}