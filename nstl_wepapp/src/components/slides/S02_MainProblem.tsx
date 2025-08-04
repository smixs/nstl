import SlideWrapper from '@/components/SlideWrapper'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { HiChartBar, HiUsers } from 'react-icons/hi2'
import { FaChartLine } from 'react-icons/fa'

export default function S02_MainProblem() {
  return (
    <SlideWrapper>
      {/* Фоновое изображение */}
      <div 
        className="absolute inset-0 z-0"
        style={{
          backgroundImage: 'linear-gradient(135deg, #0066CC 0%, #FFE6F0 100%)',
          opacity: 0.05
        }}
      />
      
      <div className="relative z-10 space-y-12">
        {/* Заголовок */}
        <div className="text-center animate-fadeIn">
          <h2 className="text-2xl md:text-3xl lg:text-4xl font-bold mb-4 text-secondary">
            ER 1.20% при 46K подписчиков
          </h2>
          <p className="text-base md:text-lg text-gray-600 font-light">
            Самая большая аудитория, но средняя вовлеченность
          </p>
        </div>

        {/* Карточки сравнения */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
          {/* Nestle */}
          <Card className="hover:shadow-md transition-all duration-300">
            <CardHeader className="pb-4">
              <div className="icon-container-primary mb-4">
                <HiUsers className="w-7 h-7 icon-primary" />
              </div>
              <CardTitle className="text-xl">Nestlé Baby & Me</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex items-center justify-between">
                <span className="text-gray-600">Подписчики</span>
                <Badge variant="default">46K</Badge>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-gray-600">ER</span>
                <Badge variant="destructive">1.20%</Badge>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-gray-600">Активные</span>
                <Badge variant="secondary">~552</Badge>
              </div>
              
              {/* Визуальный индикатор */}
              <div className="relative h-16 bg-gray-50 rounded-xl overflow-hidden shadow-inner mt-4">
                <div 
                  className="absolute bottom-0 left-0 bg-pink-400 transition-all duration-1000 ease-out"
                  style={{ height: '100%', width: '30%' }}
                >
                  <span className="absolute right-2 top-1/2 transform -translate-y-1/2 text-white font-bold text-xs">
                    30%
                  </span>
                </div>
              </div>
              
              <p className="text-sm text-gray-500 pt-2">
                Большая аудитория, но низкая вовлеченность
              </p>
            </CardContent>
          </Card>

          {/* Kabrita */}
          <Card className="hover:shadow-md transition-all duration-300">
            <CardHeader className="pb-4">
              <div className="icon-container-success mb-4">
                <FaChartLine className="w-7 h-7 icon-success" />
              </div>
              <CardTitle className="text-xl">Kabrita</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex items-center justify-between">
                <span className="text-gray-600">Подписчики</span>
                <Badge variant="success">28K</Badge>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-gray-600">ER</span>
                <Badge variant="success">2.21%</Badge>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-gray-600">Активные</span>
                <Badge variant="success">~619</Badge>
              </div>
              
              {/* Визуальный индикатор */}
              <div className="relative h-16 bg-gray-50 rounded-xl overflow-hidden shadow-inner mt-4">
                <div 
                  className="absolute bottom-0 left-0 bg-green-400 transition-all duration-1000 ease-out"
                  style={{ height: '100%', width: '55%' }}
                >
                  <span className="absolute right-2 top-1/2 transform -translate-y-1/2 text-white font-bold text-xs">
                    55%
                  </span>
                </div>
              </div>
              
              <p className="text-sm text-gray-500 pt-2">
                Меньше подписчиков, но выше вовлеченность
              </p>
            </CardContent>
          </Card>
        </div>

        {/* Вывод */}
        <div className="text-center animate-slideUp animation-delay-600">
          <div className="bg-gray-50 rounded-full px-10 py-5 shadow-sm">
            <p className="text-sm md:text-base text-gray-900 font-medium">
              🎯 Парадокс: больше подписчиков ≠ больше вовлеченности
            </p>
          </div>
        </div>
      </div>
    </SlideWrapper>
  )
}