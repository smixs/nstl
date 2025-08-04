# Slide Design Guide for Nestle Baby & Me Presentation

## 🎨 Core Design Principles

### 1. Structure Template
Every slide MUST follow this exact structure:

```tsx
import SlideWrapper from '@/components/SlideWrapper'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
// Import icons from react-icons

export default function S##_SlideName() {
  return (
    <SlideWrapper>
      {/* Background Pattern/Image - ALWAYS z-0 */}
      <div 
        className="absolute inset-0 z-0"
        style={{
          // Background styles with low opacity
        }}
      />
      
      {/* Content Container - ALWAYS z-10 */}
      <div className="relative z-10 flex flex-col h-full">
        {/* Content here */}
      </div>
    </SlideWrapper>
  )
}
```

### 2. Background Rules

#### Pattern Types:
1. **Gradient Background** (S02_MainProblem)
   ```tsx
   style={{
     backgroundImage: 'linear-gradient(135deg, #0066CC 0%, #FFE6F0 100%)',
     opacity: 0.05
   }}
   ```

2. **Radial Gradient Pattern** (S01_Title, S05_UniqueAdvantage)
   ```tsx
   style={{
     backgroundImage: `
       radial-gradient(circle at 20% 50%, rgba(0, 102, 204, 0.1) 0%, transparent 50%),
       radial-gradient(circle at 80% 80%, rgba(255, 230, 240, 0.2) 0%, transparent 50%)
     `
   }}
   ```

3. **Geometric Pattern** (S13_Kabrita)
   ```tsx
   style={{
     backgroundImage: `
       linear-gradient(45deg, rgba(34, 197, 94, 0.03) 25%, transparent 25%),
       linear-gradient(-45deg, rgba(34, 197, 94, 0.03) 25%, transparent 25%)
     `,
     backgroundSize: '20px 20px'
   }}
   ```

4. **Image Background** (S03_ProblemDetails)
   ```tsx
   style={{
     backgroundImage: 'url(/images/background.avif)',
     backgroundSize: 'cover',
     backgroundPosition: 'center',
     opacity: 0.1
   }}
   ```

**IMPORTANT**: Background opacity MUST be between 0.03-0.1 to not interfere with content readability!

### 3. Typography Hierarchy

```tsx
// Main Title (h2)
<h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-2">
  Title Here
</h2>

// Subtitle
<p className="text-lg text-gray-600">
  Subtitle here
</p>

// Card Title
<CardTitle className="text-xl">Card Title</CardTitle>
// or for smaller cards
<CardTitle className="text-base font-semibold">Section Title</CardTitle>

// Body Text
<p className="text-sm text-gray-500">Body text</p>
```

### 4. Color System (Global CSS Variables)

**IMPORTANT**: All colors are defined as CSS variables in `/src/styles/variables.css`.

**Semantic Color Classes:**
- Primary: `bg-primary`, `text-primary`, `icon-primary`
- Secondary: `bg-secondary`, `text-secondary`, `icon-secondary`
- Success: `bg-success`, `text-success`, `icon-success`
- Warning: `bg-warning`, `text-warning`, `icon-warning`
- Info: `bg-info`, `text-info`, `icon-info`

**Icon Container Classes:**
```tsx
<div className="icon-container-primary mb-4">
  <IconName className="w-7 h-7 icon-primary" />
</div>
```

**Using CSS Variables with Tailwind:**
```tsx
// Direct variable usage
<div className="bg-[var(--color-primary)] text-[var(--color-primary-dark)]">

// Badge variants
<Badge variant="default">Primary</Badge>
<Badge variant="success">Success</Badge>
<Badge variant="destructive">Error</Badge>

// Gradients
<div className="bg-gradient-to-r from-[var(--color-primary)] to-[var(--color-secondary)]">
```

**Badge Background Classes:**
- `bg-primary-soft` - Light primary background
- `bg-secondary-soft` - Light secondary background
- `bg-success-soft` - Light success background

**Text Colors:**
- Primary: `text-[var(--color-text-primary)]`
- Secondary: `text-gray-600`
- Muted: `text-gray-500`

### 5. Icon System

**Icon Requirements:**
1. ALWAYS use icons from `react-icons` library
2. Preferred libraries in order:
   - `react-icons/hi2` (HeroIcons v2)
   - `react-icons/hi` (HeroIcons v1)
   - `react-icons/fa` (FontAwesome)

**Icon Container Pattern:**
```tsx
// Use predefined classes
<div className="icon-container-primary mb-4">
  <IconName className="w-7 h-7 icon-primary" />
</div>

// Or manual pattern with CSS variables
<div className="w-14 h-14 rounded-2xl bg-[var(--color-primary)] flex items-center justify-center shadow-md mb-4">
  <IconName className="w-7 h-7 text-[var(--color-primary-dark)]" />
</div>
```

**Small Icons in Text:**
```tsx
<div className="flex items-center space-x-2">
  <IconName className="w-4 h-4 text-gray-500" />
  <span className="text-gray-600">Label</span>
</div>
```

### 6. Card Design Pattern

**Standard Card:**
```tsx
<Card className="hover:shadow-md transition-all duration-300">
  <CardHeader className="pb-4">
    {/* Icon container */}
    <div className="w-14 h-14 rounded-2xl bg-[color]-600 flex items-center justify-center shadow-md mb-4">
      <IconName className="w-7 h-7 text-white" />
    </div>
    <CardTitle className="text-xl">Title</CardTitle>
  </CardHeader>
  <CardContent className="space-y-3">
    {/* Content */}
  </CardContent>
</Card>
```

**Metric Display Pattern:**
```tsx
<div className="flex items-center justify-between">
  <span className="text-gray-600">Label</span>
  <Badge className="bg-[color]-100 text-[color]-700">Value</Badge>
</div>
```

### 7. Layout Patterns

**Three Column Grid:**
```tsx
<div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto">
  {/* Cards */}
</div>
```

**Two Column Grid:**
```tsx
<div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
  {/* Cards */}
</div>
```

**Bottom Conclusion Box:**
```tsx
<div className="mt-auto pt-8">
  <div className="bg-gray-50 rounded-2xl px-8 py-6 shadow-sm max-w-4xl mx-auto">
    <p className="text-center text-base font-medium text-gray-900">
      Conclusion text
    </p>
  </div>
</div>
```

### 8. Animation Classes

Available animations (already defined in CSS):
- `animate-fadeIn`
- `animate-slideUp`
- `animate-slideLeft`
- `animate-slideRight`
- `animation-delay-200`
- `animation-delay-400`
- `animation-delay-600`

### 9. Common Icon Mappings

- **Users/Audience**: `HiUsers`, `HiUserGroup`
- **Charts/Metrics**: `HiChartBar`, `FaChartLine`, `HiTrendingDown`
- **Calendar/Time**: `HiCalendar`, `HiClock`
- **Communication**: `HiChatAlt2`, `FaRegCommentDots`
- **Success/Failure**: `HiCheckCircle`, `HiXCircle`
- **Heart/Love**: `HiHeart`
- **Crown/Premium**: `FaCrown`

### 10. Slide Creation Checklist

- [ ] Import all necessary components and icons
- [ ] Add background pattern/image with low opacity (0.03-0.1)
- [ ] Use z-0 for background, z-10 for content
- [ ] Follow typography hierarchy
- [ ] Use consistent color scheme
- [ ] Add icons in colored containers for visual appeal
- [ ] Use hover:shadow-md for interactive cards
- [ ] Apply proper spacing (space-y-4/6/8)
- [ ] Add Badge components for metrics
- [ ] Include bottom conclusion box if needed
- [ ] Test that all icons are properly imported

### 11. Special Patterns

**Progress Bar Visualization:**
```tsx
<div className="relative h-16 bg-gray-50 rounded-xl overflow-hidden shadow-inner">
  <div 
    className="absolute bottom-0 left-0 bg-[color]-600 transition-all duration-1000 ease-out"
    style={{ height: '100%', width: '[percentage]%' }}
  >
    <span className="absolute right-2 top-1/2 transform -translate-y-1/2 text-white font-bold text-xs">
      [percentage]%
    </span>
  </div>
</div>
```

**List with Icons:**
```tsx
<div className="flex items-start space-x-2">
  <span className="text-[color]-600">•</span>
  <p className="text-sm">List item text</p>
</div>
```

### 12. DO NOT:

- ❌ Use emojis in titles or important text (only in conclusion boxes)
- ❌ Use CSS variables for colors (use Tailwind classes)
- ❌ Use shadow-lg (use shadow-md instead)
- ❌ Use complex glass effects or backdrop filters
- ❌ Use opacity higher than 0.1 for backgrounds
- ❌ Forget to add z-index to background and content
- ❌ Mix different icon libraries in the same component

### 13. Example Slide Template

```tsx
import SlideWrapper from '@/components/SlideWrapper'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { HiChartBar, HiUsers } from 'react-icons/hi2'

export default function S##_TemplateName() {
  return (
    <SlideWrapper>
      {/* Background */}
      <div 
        className="absolute inset-0 z-0"
        style={{
          backgroundImage: 'linear-gradient(135deg, #0066CC 0%, #FFE6F0 100%)',
          opacity: 0.05
        }}
      />
      
      <div className="relative z-10 flex flex-col h-full">
        {/* Header */}
        <div className="text-center mb-8">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-2">
            Slide Title
          </h2>
          <p className="text-lg text-gray-600">
            Subtitle description
          </p>
        </div>

        {/* Content Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto">
          <Card className="hover:shadow-md transition-all duration-300">
            <CardHeader className="pb-4">
              <div className="icon-container-primary mb-4">
                <HiUsers className="w-7 h-7 icon-primary" />
              </div>
              <CardTitle className="text-xl">Card Title</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-gray-600">Metric</span>
                <Badge variant="default">Value</Badge>
              </div>
              <p className="text-sm text-gray-500 pt-2">
                Description text
              </p>
            </CardContent>
          </Card>
        </div>

        {/* Bottom Conclusion */}
        <div className="mt-auto pt-8">
          <div className="bg-gray-50 rounded-2xl px-8 py-6 shadow-sm max-w-4xl mx-auto">
            <p className="text-center text-base font-medium text-gray-900">
              📊 Key takeaway or conclusion
            </p>
          </div>
        </div>
      </div>
    </SlideWrapper>
  )
}
```

## Remember: Consistency is Key! 🎯

Every slide should feel like part of the same presentation. Follow these rules strictly to maintain visual harmony and professional appearance.