# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with the Nestle Baby & Me Uzbekistan web presentation project.

## Project Overview

This is a web presentation for Nestle Baby & Me Uzbekistan showcasing their 2025-2026 digital transformation strategy to SMM agencies. The presentation addresses the critical business challenge of low engagement rate (1.20% ER with 46K followers) and presents a comprehensive strategy built on "25 years = 3 generations of trust" positioning.

## Technical Project Details

### Project Type
- **What**: Interactive web presentation (44 slides)
- **Purpose**: Present digital transformation strategy to SMM agencies
- **Tech Stack**: Vite 5 + React 18 + TypeScript + Tailwind CSS + shadcn/ui
- **Hosting**: Vercel (static deployment)
- **Key Feature**: Full print support (all slides must be printable as PDF)

### Critical Technical Requirements

1. **Print Architecture (MOST IMPORTANT)**
   - ALL 44 slides must be rendered in DOM simultaneously
   - Visibility controlled via CSS, not routing
   - Print CSS must show all slides with page breaks
   - Each slide on separate page when printing

2. **Navigation**
   - Keyboard arrows (←/→), Space, Enter
   - Click anywhere to advance
   - URL sync for sharing (/slide/1, /slide/2)
   - Progress bar at bottom

3. **Performance**
   - First Contentful Paint < 1s
   - Bundle size < 500KB
   - Lazy load images
   - Static generation

## Project Structure

```
nstl_wepapp/
├── src/
│   ├── App.tsx             # Main component with slide management
│   ├── main.tsx            # Entry point
│   ├── index.css           # Global styles + critical print CSS
│   ├── components/
│   │   ├── slides/         # 44 slide components
│   │   │   ├── index.ts    # Export registry
│   │   │   ├── S01_Title.tsx
│   │   │   ├── S02_MainProblem.tsx
│   │   │   └── ... (all 44 slides)
│   │   ├── ui/             # shadcn/ui components
│   │   ├── SlideWrapper.tsx
│   │   ├── ImagePlaceholder.tsx
│   │   └── ProgressBar.tsx
│   ├── lib/
│   │   ├── slides.ts       # Slide metadata
│   │   ├── constants.ts    # Brand colors
│   │   └── utils.ts        # cn() helper
│   └── assets/
│       └── images/         # Presentation images
└── [config files]
```

## Content Structure (44 Slides)

### BLOCK 1: PROBLEM & CONTEXT (Slides 1-7)
1. Title: Digital Transformation Strategy 2025-2026
2. Main Problem: 1.20% ER with 46K followers
3. Problem Details: Low quality ER and LTV
4. WHO Code Red Zone: What's forbidden/allowed
5. Unique Advantage: 20 years in Uzbekistan
6. Two Mothers: Striving Researchers vs Uncompromising Pioneers
7. Competitive Landscape: Nestle's generational trust

### BLOCK 2: MARKET OVERVIEW (Slides 8-20)
8. Market Landscape: The Engagement Battlefield
9. Leaders Anatomy: Top 3 analysis
10. 5 Working Market Mechanics
11. Competitor Lessons
12. Nestle Position: From "showcase" to "advisor"
13-19. Competitor Profiles (Kabrita, Nutrilak, Agusha, Nutrilon, Nuppi, FrutoNyanya, Bebivita)
20. E-commerce insights

### BLOCK 3: STRATEGY SOLUTION (Slides 21-30)
21. Strategic Advantage: 25 years = 3 generations
22. Unique RTB: "We don't sell product, we transfer trust"
23. Big Idea: "Circle of Trust Baby & Me"
24. Baby&Me Positioning
25. 4 Strategic Solutions
26-29. Solution Details (UGC Contest, AI Bot, Personalization, Generations Content)
30. Tone of Voice

### BLOCK 4: TACTICAL IMPLEMENTATION (Slides 31-38)
31. Content Rubrics
32. Instagram Formats (60% Reels)
33. Telegram Strategy
34. Doctors Strategy (Unbranded only)
35. Creative Examples
36. Community Management 3.0
37. Visual Transformation
38. Engagement Mechanics

### BLOCK 5: SAFETY & CONTROL (Slides 39-41)
39. UGC Safety System
40. Risk Protection
41. Compliance Process

### BLOCK 6: METRICS & RESULTS (Slides 42-44)
42. KPI Ladder (ER: 1.20% → 1.80%)
43. Quality Metrics
44. 90-Day Plan

## Design System

### Color System (Candyland Theme + Custom Brand Colors)
```css
/* Candyland Base Colors (OKLCH) */
--primary: oklch(0.8677 0.0735 7.0855);        /* Soft peach */
--secondary: oklch(0.8148 0.0819 225.7537);    /* Soft blue */
--accent: oklch(0.9680 0.2110 109.7692);       /* Bright lime */
--muted: oklch(0.8828 0.0285 98.1033);         /* Soft yellow */
--card: oklch(1.0000 0 0);                     /* Pure white */
--background: oklch(0.9809 0.0025 228.7836);   /* Soft background */

/* Custom Nestle Brand Colors (OKLCH) */
--nestle-blue: oklch(0.5234 0.1876 237.4521);
--nestle-blue-light: oklch(0.9456 0.0234 237.4521);
--nestle-blue-pastel: oklch(0.7123 0.1234 237.4521);
--nestle-blue-dark: oklch(0.3456 0.2134 237.4521);
--baby-pink: oklch(0.9567 0.0456 345.6789);
--baby-pink-deep: oklch(0.8234 0.0789 345.6789);
--baby-pink-vibrant: oklch(0.7456 0.1234 345.6789);
--success-green: oklch(0.6789 0.1876 142.3456);
--danger-red: oklch(0.6368 0.2078 25.3313);
```

### Typography (Poppins Font System)
- Font Family: 'Poppins', 'Inter', system-ui, sans-serif
- Hero Text: clamp(2rem, 3.5vw, 3.5rem)
- Title: clamp(1.75rem, 2.5vw, 2.5rem)
- Heading: clamp(1.5rem, 2vw, 2rem)
- Subheading: clamp(1.25rem, 1.5vw, 1.5rem)
- Body Large: 1.125rem
- Body: 0.9375rem

### Icon System (Lucide React)
```bash
npm install lucide-react
```
- **Library**: Lucide React - soft, rounded SVG icons
- **Usage**: `import { IconName } from 'lucide-react'`
- **Style**: Clean, modern, consistent line style
- **Examples**: Users, Heart, Crown, Sparkles, etc.
- **Customizable**: Size, color, stroke width via props

### Key Components
- **SlideWrapper**: Container with consistent padding
- **ProgressBar**: Thin progress indicator at bottom
- **ImagePlaceholder**: Smart image component with fallback
- **NavigationHint**: First slide navigation helper

## Critical Implementation Notes

### 1. Print CSS Architecture
```css
@media print {
  /* CRITICAL: Show ALL slides when printing */
  .slide {
    display: block !important;
    page-break-after: always;
    page-break-inside: avoid;
    width: 100%;
    height: 100vh;
  }
  
  .slide:last-child {
    page-break-after: auto;
  }
  
  /* Hide navigation elements */
  .progress-bar,
  .navigation-hint,
  button {
    display: none !important;
  }
}
```

### 2. App.tsx Structure
```tsx
function App() {
  const [currentSlide, setCurrentSlide] = useState(0);
  
  // ALL slides in DOM for printing!
  return (
    <div className="presentation">
      <ProgressBar current={currentSlide} total={slides.length} />
      
      {slides.map((SlideComponent, index) => (
        <div
          key={index}
          className={cn(
            "slide",
            currentSlide === index ? "block" : "hidden"
          )}
        >
          <SlideComponent />
        </div>
      ))}
    </div>
  );
}
```

### 3. Image Placeholder Strategy
- With image: Show actual image with lazy loading
- Without image: Show placeholder "[Image: description]"
- Loading state: shadcn/ui Skeleton component

## Content Guidelines

### WHO Code Compliance (CRITICAL)
- **FORBIDDEN**: Any promotion of formulas for 0-12 months (stages 1-2)
- **ALLOWED**: Toddler milk (stages 3-4) and complementary foods only
- **SAFETY**: All UGC must pass 3-step verification including WHO Code compliance

### Strategic Messaging
- Core advantage: "25 years = 3 generations of trust"
- Not selling product, but transferring trust between generations
- Baby & Me as circle of trust where generational experience meets innovation
- "The same NAN your mother chose, but better"

### Key Business Metrics
- Current ER: 1.20% (need to reach 1.80%)
- Video content share: 35% → 60%
- Focus on saves and DM questions (not likes)
- Comment rate: maintain 78%+

## Slide Design System

**⚠️ IMPORTANT**: When creating new slides, you MUST follow the detailed design guide in `SLIDE_DESIGN_GUIDE.md`. 

This guide includes:
- Component structure templates with exact code patterns
- Background patterns (gradients, radial, geometric, images)
- Icon system using React Icons (hi2, hi, fa)
- Color scheme (blue-600, green-600, red-600, etc.)
- Typography hierarchy
- Card and Badge patterns
- Layout grids and spacing rules

## Development Checklist

- [ ] Vite project with React 18 + TypeScript
- [ ] shadcn/ui components installed
- [ ] All 44 slide components created
- [ ] **CRITICAL: Print (Ctrl+P) shows ALL 44 slides**
- [ ] **Each slide on separate page when printing**
- [ ] **All slides rendered in DOM (not just current)**
- [ ] Image placeholders working correctly
- [ ] Keyboard navigation functional
- [ ] URL syncs with current slide
- [ ] Lazy loading for images
- [ ] Production build successful
- [ ] Correct display on projector (1920x1080)
- [ ] Mobile responsive view

## Quick Start Commands

```bash
# Create project
npm create vite@latest nestle-presentation -- --template react-ts
cd nestle-presentation

# Install dependencies
npm install -D tailwindcss postcss autoprefixer
npm install react-router-dom lucide-react class-variance-authority clsx tailwind-merge

# Initialize Tailwind
npx tailwindcss init -p

# Install shadcn/ui
npx shadcn-ui@latest init
npx shadcn-ui@latest add button card progress skeleton badge separator alert
```

## Important Reminders

1. **Print Support**: This is the MOST critical feature. All slides must be in DOM and printable.
2. **Performance**: Keep bundle small, use lazy loading for images
3. **Accessibility**: Ensure keyboard navigation works perfectly
4. **Brand Compliance**: Follow Nestle brand colors and guidelines exactly
5. **WHO Code**: Never show content promoting formula for infants under 12 months