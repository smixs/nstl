import React from 'react'

export const BackgroundShapes: React.FC = () => {
  return (
    <div className="fixed inset-0 overflow-hidden pointer-events-none">
      {/* Large gradient orb - bottom right */}
      <div 
        className="absolute -bottom-48 -right-48 w-96 h-96 rounded-full opacity-20 animate-morph"
        style={{
          background: 'radial-gradient(circle at center, var(--nestle-blue-pastel), transparent 70%)',
          filter: 'blur(40px)',
        }}
      />
      
      {/* Medium gradient orb - top left */}
      <div 
        className="absolute -top-32 -left-32 w-64 h-64 rounded-full opacity-15 animate-float"
        style={{
          background: 'radial-gradient(circle at center, var(--baby-pink-vibrant), transparent 70%)',
          filter: 'blur(30px)',
          animationDelay: '2s',
        }}
      />
      
      {/* Small gradient orb - center right */}
      <div 
        className="absolute top-1/2 -right-16 w-48 h-48 rounded-full opacity-10 animate-float"
        style={{
          background: 'radial-gradient(circle at center, var(--success-green-light), transparent 70%)',
          filter: 'blur(25px)',
          animationDelay: '4s',
        }}
      />
      
      {/* Flowing shape - bottom left */}
      <div 
        className="absolute -bottom-32 -left-16 w-80 h-80 opacity-15 animate-morph"
        style={{
          background: 'linear-gradient(135deg, var(--baby-pink) 0%, var(--nestle-blue-light) 100%)',
          borderRadius: '40% 60% 70% 30% / 40% 50% 60% 50%',
          filter: 'blur(35px)',
          animationDelay: '1s',
        }}
      />
    </div>
  )
}

export default BackgroundShapes