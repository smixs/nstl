/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Soft Pastel Colors - Beautiful and gentle
        'soft-blue': '#A8D8EA',        // Soft sky blue
        'soft-pink': '#FFAAA5',        // Soft coral pink
        'soft-yellow': '#FFE5AD',      // Soft warm yellow
        'soft-purple': '#E6B5E8',      // Soft lavender
        'soft-green': '#B8E6B8',       // Soft mint green
        'soft-orange': '#FFD3B6',      // Soft peach
        
        // Darker versions for text/accents
        'blue-pastel': '#7FC4E3',      // Darker soft blue
        'pink-pastel': '#FF8B85',      // Darker soft pink
        'yellow-pastel': '#FFD687',    // Darker soft yellow
        'purple-pastel': '#D99BDB',    // Darker soft purple
        'green-pastel': '#93D993',     // Darker soft green
        'orange-pastel': '#FFC09F',    // Darker soft peach
        
        // Neutral colors
        'gray-50': '#FAFAFA',
        'gray-100': '#F5F5F5',
        'gray-200': '#EEEEEE',
        'gray-300': '#E0E0E0',
        'gray-400': '#BDBDBD',
        'gray-500': '#9E9E9E',
        'gray-600': '#757575',
        'gray-700': '#616161',
        'gray-800': '#424242',
        'gray-900': '#212121',
        
        // Legacy mappings for existing code
        'nestle-blue': '#A8D8EA',
        'baby-pink': '#FFAAA5',
        'success-green': '#B8E6B8',
        'danger-red': '#FFAAA5',
      },
      fontFamily: {
        sans: ['Poppins', 'Inter', 'system-ui', 'sans-serif'],
        display: ['Poppins', 'Inter', 'system-ui', 'sans-serif'],
        body: ['Plus Jakarta Sans', 'Inter', 'system-ui', 'sans-serif'],
      },
      borderRadius: {
        'sm': 'var(--radius-sm)',
        'md': 'var(--radius-md)',
        'lg': 'var(--radius-lg)',
        'xl': 'var(--radius-xl)',
        '2xl': 'var(--radius-2xl)',
        'full': 'var(--radius-full)',
      },
      boxShadow: {
        '2xs': 'var(--shadow-2xs)',
        'xs': 'var(--shadow-xs)',
        'sm': 'var(--shadow-sm)',
        'md': 'var(--shadow-md)',
        'lg': 'var(--shadow-lg)',
        'xl': 'var(--shadow-xl)',
        '2xl': 'var(--shadow-2xl)',
      },
    },
  },
  plugins: [],
}