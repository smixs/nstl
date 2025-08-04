import SlideWrapper from '@/components/SlideWrapper'
import ImagePlaceholder from '@/components/ImagePlaceholder'
import { Card, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { HiUsers, HiHeart } from 'react-icons/hi2'
import { FaCrown } from 'react-icons/fa'

export default function S05_UniqueAdvantage() {
  return (
    <SlideWrapper>
      {/* Фоновый паттерн с кругами поколений */}
      <div 
        className="absolute inset-0 z-0"
        style={{
          backgroundImage: `
            radial-gradient(circle at 10% 20%, rgba(0, 102, 204, 0.04) 0%, transparent 40%),
            radial-gradient(circle at 80% 40%, rgba(135, 206, 235, 0.04) 0%, transparent 40%),
            radial-gradient(circle at 50% 80%, rgba(255, 192, 203, 0.04) 0%, transparent 40%)
          `
        }}
      />
      
      <div className="relative z-10 flex flex-col h-full">
        {/* Заголовок */}
        <div className="text-center mb-8">
          <h2 className="text-4xl md:text-5xl font-bold text-primary leading-tight">
            20 ЛЕТ В УЗБЕКИСТАНЕ
          </h2>
          <p className="text-lg text-gray-600 mt-2 font-light">
            Три поколения доверия
          </p>
        </div>

        {/* Основной контент */}
        <div className="flex-grow grid grid-cols-2 gap-12 items-center">
          {/* Левая часть - карточки поколений */}
          <div className="space-y-6">
            {/* Поколение 1 */}
            <Card className="hover:shadow-md transition-all duration-300">
              <CardContent className="p-6">
                <div className="flex items-center space-x-4">
                  <div className="icon-container-primary">
                    <HiUsers className="w-8 h-8 icon-primary" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-lg font-semibold text-primary mb-1">Поколение мам</h3>
                    <p className="text-sm text-gray-600 leading-relaxed">
                      Сегодняшние мамы выросли на Nestlé
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Поколение 2 */}
            <Card className="hover:shadow-md transition-all duration-300">
              <CardContent className="p-6">
                <div className="flex items-center space-x-4">
                  <div className="icon-container-success">
                    <HiHeart className="w-8 h-8 icon-success" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-lg font-semibold text-primary mb-1">Поколение бабушек</h3>
                    <p className="text-sm text-gray-600 leading-relaxed">
                      Бабушки доверяют, потому что сами кормили NAN
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Поколение 3 */}
            <Card className="hover:shadow-md transition-all duration-300">
              <CardContent className="p-6">
                <div className="flex items-center space-x-4">
                  <div className="icon-container-secondary">
                    <FaCrown className="w-8 h-8 icon-secondary" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-lg font-semibold text-primary mb-1">3 поколения = 1 выбор</h3>
                    <p className="text-sm text-gray-600 leading-relaxed">
                      Передача доверия через поколения
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
          
          {/* Правая часть - изображение */}
          <div className="relative animate-slideRight animation-delay-600">
            <ImagePlaceholder
              src="/images/three-generations.jpg"
              alt="Три поколения семьи - бабушка, мама и ребенок"
              aspectRatio="4/3"
              className="rounded-3xl shadow-xl hover:shadow-2xl transition-all duration-300"
            />
            <div className="absolute top-4 right-4">
              <Badge className="bg-blue-200 text-blue-700 shadow-md">
                25 лет доверия
              </Badge>
            </div>
          </div>
        </div>

        {/* Нижний акцент */}
        <div className="text-center mt-8">
          <div className="bg-gray-50 rounded-full px-8 py-4 shadow-sm">
            <p className="text-sm font-medium text-primary">
              💝 Единственный бренд, которому доверяют ВСЕ поколения семьи
            </p>
          </div>
        </div>
      </div>
    </SlideWrapper>
  )
}