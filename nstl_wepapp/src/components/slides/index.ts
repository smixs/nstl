import S01_Title from './S01_Title'
import S02_MainProblem from './S02_MainProblem'
import S03_ProblemDetails from './S03_ProblemDetails'
import S05_UniqueAdvantage from './S05_UniqueAdvantage'
import S13_Kabrita from './S13_Kabrita'

export const slides = [
  S01_Title,
  S02_MainProblem,
  S03_ProblemDetails,
  S05_UniqueAdvantage,
  S13_Kabrita,
] as const

export const slideNames = [
  'Титульный слайд',
  'Главная проблема',
  'Детализация проблемы',
  'Уникальное преимущество',
  'Профиль конкурента: Kabrita',
] as const