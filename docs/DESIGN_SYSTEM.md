# Northstar Design System

**Document Version:** 1.0  
**Date:** January 19, 2026  
**Product:** Northstar by MarketNova  
**Based On:** MarketNova Website (marketnova.net)

---

## Overview

This design system defines the visual language for the Northstar Client Portal, derived from the MarketNova corporate website. It ensures brand consistency across all client-facing interfaces.

**Tech Stack:**
- **Framework:** React with TypeScript
- **Styling:** TailwindCSS v4
- **Icons:** Lucide React, MDI Icons
- **Fonts:** Montserrat (Google Fonts)
- **Components:** shadcn/ui (customized to match theme)

---

## Color Palette

### Primary Colors (Alpha - Purple)

The primary brand color is a vibrant purple gradient scale.

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-alpha-50` | `#efe8fd` | Lightest backgrounds |
| `--color-alpha-100` | `#ded0fb` | Light hover states |
| `--color-alpha-200` | `#bea2f6` | Light accents |
| `--color-alpha-300` | `#9d73f2` | Medium accents |
| `--color-alpha-400` | `#7d44ee` | **Vibrant accent text** |
| `--color-alpha-500` | `#5c16e9` | **Primary brand color** |
| `--color-alpha-600` | `#4a11bb` | Primary buttons, focus states |
| `--color-alpha-700` | `#370d8c` | Dark accents |
| `--color-alpha-800` | `#25095d` | **Body text (light mode)** |
| `--color-alpha-900` | `#12042f` | **Title text (light mode)** |
| `--color-alpha-950` | `#0d0321` | **Dark mode background** |

### Muted Purple (Alpha Muted)

Desaturated purple for subtle backgrounds and borders.

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-alpha-muted-50` | `#f1eff6` | - |
| `--color-alpha-muted-100` | `#e3deed` | Card hover (light) |
| `--color-alpha-muted-200` | `#c7beda` | Mode button (dark) |
| `--color-alpha-muted-300` | `#ab9dc8` | - |
| `--color-alpha-muted-400` | `#8f7cb6` | - |
| `--color-alpha-muted-500` | `#745ca3` | - |
| `--color-alpha-muted-600` | `#5c4983` | Mode button (light) |
| `--color-alpha-muted-700` | `#453762` | - |
| `--color-alpha-muted-800` | `#2e2541` | - |
| `--color-alpha-muted-900` | `#171221` | Card background (dark) |
| `--color-alpha-muted-950` | `#100d17` | - |

### Faded Purple (Alpha Faded)

Neutral gray-purple for text and borders.

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-alpha-faded-50` | `#f2f1f4` | Card background (light) |
| `--color-alpha-faded-100` | `#e5e3e8` | - |
| `--color-alpha-faded-200` | `#cac7d1` | - |
| `--color-alpha-faded-300` | `#b0abba` | Borders (light), highlight secondary |
| `--color-alpha-faded-400` | `#968fa3` | - |
| `--color-alpha-faded-500` | `#7b738c` | - |
| `--color-alpha-faded-600` | `#635c70` | Button hover |
| `--color-alpha-faded-700` | `#4a4554` | - |
| `--color-alpha-faded-800` | `#312e38` | Buttons, borders (dark) |
| `--color-alpha-faded-900` | `#19171c` | - |
| `--color-alpha-faded-950` | `#111014` | - |

### Secondary Colors (Beta - Cyan/Teal)

Accent color for section headers and info icons.

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-beta-50` | `#e5fffc` | - |
| `--color-beta-100` | `#ccfffa` | - |
| `--color-beta-200` | `#99fff5` | - |
| `--color-beta-300` | `#66fff0` | - |
| `--color-beta-400` | `#33ffeb` | - |
| `--color-beta-500` | `#00ffe6` | Bright cyan |
| `--color-beta-600` | `#00ccb8` | Section header (dark) |
| `--color-beta-700` | `#00998a` | **Section header (light), info icons** |
| `--color-beta-800` | `#00665c` | - |
| `--color-beta-900` | `#00332e` | - |
| `--color-beta-950` | `#002420` | - |

### Tertiary Colors (Gamma - Coral/Orange)

Accent for dividers and warnings.

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-gamma-50` | `#faeeeb` | - |
| `--color-gamma-100` | `#f4ded7` | - |
| `--color-gamma-200` | `#e9bcaf` | - |
| `--color-gamma-300` | `#de9b87` | - |
| `--color-gamma-400` | `#d37a5f` | - |
| `--color-gamma-500` | `#c85937` | **Divider color (dark mode)** |
| `--color-gamma-600` | `#a0472c` | - |
| `--color-gamma-700` | `#783521` | - |
| `--color-gamma-800` | `#502316` | - |
| `--color-gamma-900` | `#28120b` | - |
| `--color-gamma-950` | `#1c0c08` | - |

### Base Colors

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-white` | `#ffffff` | Light mode background, button text |
| `--color-black` | `#000000` | - |

---

## Semantic Color Tokens

### Light Mode

```css
:root {
  /* Backgrounds */
  --background-color: var(--color-white);                    /* #ffffff */
  --card-background-color: var(--color-alpha-faded-50);      /* #f2f1f4 */
  --card-background-hover-color: var(--color-alpha-muted-100); /* #e3deed */

  /* Text */
  --text-color: var(--color-alpha-800);                      /* #25095d */
  --text-title-color: var(--color-alpha-900);                /* #12042f */
  --text-nav-color: var(--color-alpha-900);                  /* #12042f */
  --text-section-color: var(--color-beta-700);               /* #00998a */
  --text-feature-color: var(--color-alpha-600);              /* #4a11bb */
  --text-vibrant-color: var(--color-alpha-400);              /* #7d44ee */
  --text-button-color: var(--color-white);                   /* #ffffff */

  /* Borders & Icons */
  --border-color: var(--color-alpha-faded-300);              /* #b0abba */
  --divider-color: var(--color-alpha-faded-300);             /* #b0abba */
  --info-icon-color: var(--color-beta-700);                  /* #00998a */

  /* Buttons */
  --button-color: var(--color-alpha-faded-800);              /* #312e38 */
  --button-hover-color: var(--color-alpha-faded-600);        /* #635c70 */
  --button-focus-color: var(--color-alpha-600);              /* #4a11bb */
  --button-focus-hover-color: var(--color-alpha-300);        /* #9d73f2 */

  /* Gradients */
  --highlight-primary-color: var(--color-alpha-500);         /* #5c16e9 */
  --highlight-secondary-color: var(--color-alpha-faded-300); /* #b0abba */
}
```

### Dark Mode

```css
:root[data-theme="dark"] {
  /* Backgrounds */
  --background-color: var(--color-alpha-950);                /* #0d0321 */
  --card-background-color: var(--color-alpha-muted-900);     /* #171221 */
  --card-background-hover-color: var(--color-alpha-800);     /* #25095d */

  /* Text */
  --text-color: var(--color-alpha-100);                      /* #ded0fb */
  --text-title-color: var(--color-white);                    /* #ffffff */
  --text-nav-color: var(--color-alpha-200);                  /* #bea2f6 */
  --text-section-color: var(--color-beta-600);               /* #00ccb8 */
  --text-feature-color: var(--color-alpha-300);              /* #9d73f2 */
  --text-vibrant-color: var(--color-alpha-400);              /* #7d44ee */
  --text-button-color: var(--color-alpha-100);               /* #ded0fb */

  /* Borders */
  --border-color: var(--color-alpha-faded-800);              /* #312e38 */
  --divider-color: var(--color-gamma-500);                   /* #c85937 */
  --info-icon-color: var(--color-beta-700);                  /* #00998a */

  /* Buttons */
  --button-color: var(--color-alpha-faded-800);              /* #312e38 */
  --button-hover-color: var(--color-alpha-faded-600);        /* #635c70 */
  --button-focus-color: var(--color-alpha-600);              /* #4a11bb */
  --button-focus-hover-color: var(--color-alpha-400);        /* #7d44ee */

  /* Gradients */
  --highlight-primary-color: var(--color-alpha-500);         /* #5c16e9 */
  --highlight-secondary-color: var(--color-alpha-600);       /* #4a11bb */
}
```

---

## Typography

### Font Family

```css
* {
  font-family: 'Montserrat', 'ui-sans-serif', 'system-ui', 'sans-serif';
}
```

**Google Fonts Import:**
```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

### Font Weights

| Weight | Value | Usage |
|--------|-------|-------|
| Regular | `400` | Body text |
| Medium | `500` | Hero titles, buttons |
| Semibold | `600` | Feature headers, CTA buttons |
| Bold | `700` | Section headers |

### Text Styles

| Style | Size | Weight | Letter Spacing | Color Token |
|-------|------|--------|----------------|-------------|
| Hero Title | `text-5xl` to `text-7xl` | 500 | `0.2rem` | `--text-title-color` |
| Hero Accent | `text-5xl` to `text-7xl` | 500 | - | `--text-vibrant-color` |
| Section Header | `text-3xl` to `text-4xl` (2.5rem) | 700 | `0.2rem` | `--text-section-color` |
| Feature Header | `text-lg` to `text-xl` (1.2rem) | 600 | `0.1rem` | `--text-feature-color` |
| Body Text | `text-base` | 400 | - | `--text-color` |
| Navigation | `text-sm` | 400 | `tracking-wide` | `--text-nav-color` |

### CSS Classes

```css
.theme-hero-title {
  color: var(--text-title-color);
  letter-spacing: 0.2rem;
  font-weight: 500;
}

.theme-hero-title-accent {
  color: var(--text-vibrant-color);
  font-weight: 500;
}

.theme-section-header {
  color: var(--text-section-color);
  font-size: 2.5rem;
  letter-spacing: 0.2rem;
  font-weight: 700;
}

.theme-feature-header {
  color: var(--text-feature-color);
  font-size: 1.2rem;
  letter-spacing: 0.1rem;
  font-weight: 600;
}
```

---

## Components

### Buttons

#### Primary Button (Focus Button)

```css
.theme-focus-button {
  background-color: var(--button-focus-color);  /* Purple #4a11bb */
  color: var(--text-button-color);
  font-weight: 500;
  border-radius: 9999px;  /* rounded-full */
  padding: 0 1.5rem;
  height: 2.75rem;  /* h-11 */
  transition: all 300ms;
}

.theme-focus-button:hover {
  background-color: var(--button-focus-hover-color);
  transform: scale(1.05);
}

.theme-focus-button:active {
  transform: scale(0.95);
}
```

**Tailwind Classes:**
```html
<button class="relative flex h-11 w-max items-center justify-center px-6 rounded-full
  bg-alpha-600 text-white font-medium
  transition duration-300 hover:scale-105 hover:bg-alpha-300
  active:duration-75 active:scale-95">
  Learn more
</button>
```

#### Secondary Button

```css
.theme-button {
  background-color: var(--button-color);  /* Dark gray #312e38 */
  color: var(--text-button-color);
  font-weight: 500;
  border-radius: 9999px;
  padding: 0 1.5rem;
  height: 2.75rem;
}

.theme-button:hover {
  background-color: var(--button-hover-color);
}
```

### Cards

```css
.theme-card {
  background-color: var(--card-background-color);
  border-color: var(--border-color);
  border-radius: 1.5rem;  /* rounded-3xl */
  transition: all 200ms;
}

.theme-card:hover {
  background-color: var(--card-background-hover-color);
  z-index: 1;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);  /* shadow-2xl */
}
```

**Card Layout Pattern:**
```html
<div class="group relative transition hover:z-[1] hover:shadow-2xl h-full theme-card">
  <div class="relative space-y-8 py-12 p-8 h-full flex flex-col">
    <img src="..." class="w-20 mb-4 mx-auto" alt="..." />
    <div class="space-y-2 flex-grow">
      <h5 class="text-xl theme-feature-header transition group-hover:text-secondary">
        Title
      </h5>
      <p>Description text...</p>
    </div>
  </div>
</div>
```

### Navigation

```css
/* Fixed header with border */
nav {
  position: fixed;
  top: 0;
  z-index: 10;
  width: 100%;
  border-bottom: 1px solid var(--border-color);
  background-color: var(--background-color);
}

/* Navigation links */
.theme-nav-text {
  color: var(--text-nav-color);
}

/* Mobile menu dropdown */
.theme-nav-dropdown {
  background-color: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  padding: 2rem;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}
```

### Gradients

```css
/* Primary gradient (purple) */
.theme-gradient-primary {
  opacity: 0.64;
  background: linear-gradient(135deg,
    var(--background-color),
    var(--highlight-primary-color));
}

/* Secondary gradient */
.theme-gradient-secondary {
  opacity: 0.64;
  background: linear-gradient(0deg,
    var(--background-color),
    var(--highlight-secondary-color));
}
```

**Background Blur Effect:**
```html
<div class="absolute inset-0 h-max w-full m-auto grid grid-cols-2 -space-x-52">
  <div class="blur-[106px] h-56 bg-gradient-to-br from-background to-alpha-500 opacity-64"></div>
  <div class="blur-[106px] h-32 bg-gradient-to-r from-background to-alpha-faded-300 opacity-64"></div>
</div>
```

### Icons

```css
.theme-info-icon {
  color: var(--info-icon-color);  /* Teal #00998a */
  width: 1.5rem;
  height: 1.5rem;
}
```

**Icon Usage Pattern:**
```html
<div class="flex gap-4 items-start">
  <Icon name="mdi:rocket-launch" class="w-6 h-6 ml-2 mr-2 theme-info-icon" />
  <div class="w-5/6">
    <h3 class="text-lg theme-feature-header">Feature Title</h3>
    <p class="pb-4">Feature description...</p>
  </div>
</div>
```

---

## Layout

### Container

```css
.container {
  max-width: 1280px;  /* xl breakpoint */
  margin: 0 auto;
  padding: 0 1rem;
}

@media (min-width: 640px) {
  .container { padding: 0 1.5rem; }
}

@media (min-width: 1024px) {
  .container { padding: 0 2rem; }
}
```

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `space-4` | `1rem` | Small gaps |
| `space-6` | `1.5rem` | Medium gaps |
| `space-8` | `2rem` | Section padding |
| `space-12` | `3rem` | Large gaps |
| `space-16` | `4rem` | Section margins |
| `space-20` | `5rem` | Major section margins |
| `space-36` | `9rem` | Hero top padding |

### Grid Patterns

**Feature Grid (4 columns):**
```html
<div class="grid divide-x divide-y border rounded-3xl
  sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-4 overflow-hidden">
  <!-- Cards -->
</div>
```

**Two Column Layout:**
```html
<div class="space-y-4 justify-between md:flex flex-row-reverse
  md:gap-6 md:space-y-0 lg:gap-12 lg:items-center">
  <div class="md:5/12 lg:w-1/2"><!-- Image --></div>
  <div class="md:7/12 lg:w-1/2"><!-- Content --></div>
</div>
```

---

## Responsive Breakpoints

| Breakpoint | Min Width | Usage |
|------------|-----------|-------|
| `sm` | `640px` | Mobile landscape |
| `md` | `768px` | Tablet |
| `lg` | `1024px` | Desktop |
| `xl` | `1280px` | Large desktop |

---

## Animations & Transitions

### Standard Transitions

```css
/* Default transition */
.transition {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

/* Duration variants */
.duration-300 { transition-duration: 300ms; }
.duration-500 { transition-duration: 500ms; }

/* Active state (quick snap back) */
.active\:duration-75:active { transition-duration: 75ms; }
```

### Hover Effects

```css
/* Scale on hover */
.hover\:scale-105:hover { transform: scale(1.05); }
.active\:scale-95:active { transform: scale(0.95); }

/* Shadow on hover */
.hover\:shadow-2xl:hover {
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}
```

### Mobile Menu Animation

```css
/* Menu slide in */
#navlinks {
  visibility: hidden;
  opacity: 0;
  transform: translateY(0.25rem) scale(0.9);
  transition: all 0.3s ease;
}

#nav[data-state="active"] #navlinks {
  visibility: visible;
  opacity: 1;
  transform: translateY(0) scale(1);
}

/* Background overlay */
#navLayer {
  transform: scaleY(0);
  transform-origin: bottom;
  transition: transform 0.5s ease;
}

#nav[data-state="active"] #navLayer {
  transform: scaleY(1);
  transform-origin: top;
}
```

---

## Dark Mode Implementation

### Theme Toggle

```typescript
// Toggle theme
function toggleTheme() {
  const html = document.documentElement;
  const currentTheme = html.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  
  html.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
}

// Initialize on page load
function initTheme() {
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (savedTheme) {
    document.documentElement.setAttribute('data-theme', savedTheme);
  } else if (prefersDark) {
    document.documentElement.setAttribute('data-theme', 'dark');
  }
}
```

### CSS Structure

```css
/* Light mode (default) */
:root {
  color-scheme: light;
  /* Light mode variables */
}

/* Dark mode */
:root[data-theme="dark"] {
  color-scheme: dark;
  /* Dark mode variables */
}

/* System preference fallback */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;
    /* Dark mode variables */
  }
}
```

---

## TailwindCSS Configuration

### tailwind.config.js

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        // Primary (Alpha - Purple)
        alpha: {
          50: '#efe8fd',
          100: '#ded0fb',
          200: '#bea2f6',
          300: '#9d73f2',
          400: '#7d44ee',
          500: '#5c16e9',
          600: '#4a11bb',
          700: '#370d8c',
          800: '#25095d',
          900: '#12042f',
          950: '#0d0321',
        },
        // Secondary (Beta - Cyan)
        beta: {
          50: '#e5fffc',
          100: '#ccfffa',
          200: '#99fff5',
          300: '#66fff0',
          400: '#33ffeb',
          500: '#00ffe6',
          600: '#00ccb8',
          700: '#00998a',
          800: '#00665c',
          900: '#00332e',
          950: '#002420',
        },
        // Tertiary (Gamma - Coral)
        gamma: {
          50: '#faeeeb',
          100: '#f4ded7',
          200: '#e9bcaf',
          300: '#de9b87',
          400: '#d37a5f',
          500: '#c85937',
          600: '#a0472c',
          700: '#783521',
          800: '#502316',
          900: '#28120b',
          950: '#1c0c08',
        },
      },
      fontFamily: {
        sans: ['Montserrat', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      letterSpacing: {
        'section': '0.2rem',
        'feature': '0.1rem',
      },
      borderRadius: {
        '3xl': '1.5rem',
      },
    },
  },
  plugins: [],
}
```

---

## Component Library (shadcn/ui Customization)

When using shadcn/ui, apply these theme overrides:

### Button

```typescript
// components/ui/button.tsx
const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-full font-medium transition duration-300 hover:scale-105 active:scale-95 active:duration-75",
  {
    variants: {
      variant: {
        default: "bg-alpha-600 text-white hover:bg-alpha-300",
        secondary: "bg-alpha-faded-800 text-white hover:bg-alpha-faded-600",
        outline: "border border-alpha-faded-300 bg-transparent hover:bg-alpha-faded-50",
        ghost: "hover:bg-alpha-faded-50",
      },
      size: {
        default: "h-11 px-6",
        sm: "h-9 px-4",
        lg: "h-12 px-8",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)
```

### Card

```typescript
// components/ui/card.tsx
const Card = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(
  ({ className, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(
        "rounded-3xl bg-alpha-faded-50 dark:bg-alpha-muted-900 border border-alpha-faded-300 dark:border-alpha-faded-800 transition hover:bg-alpha-muted-100 dark:hover:bg-alpha-800 hover:shadow-2xl",
        className
      )}
      {...props}
    />
  )
)
```

---

## Usage Examples

### Hero Section

```tsx
<section className="relative pt-36 mb-20">
  <Container>
    <div className="lg:w-4/5 text-center mx-auto">
      <h1 className="text-5xl md:text-6xl xl:text-7xl font-medium tracking-[0.2rem] text-alpha-900 dark:text-white">
        Analytics at <br />
        <span className="text-alpha-400">lightspeed.</span>
      </h1>
      <p className="mt-8 text-alpha-800 dark:text-alpha-100">
        Best-in-class enterprise analytics for your industry in months, not years.
      </p>
      <div className="mt-16 flex flex-wrap justify-center gap-6">
        <Button>Learn more</Button>
        <Button variant="secondary">Value chain intro</Button>
      </div>
    </div>
  </Container>
</section>
```

### Feature Card Grid

```tsx
<div className="grid divide-x divide-y border border-alpha-faded-300 dark:border-alpha-faded-800 rounded-3xl overflow-hidden sm:grid-cols-2 lg:grid-cols-4">
  {features.map((feature) => (
    <Card key={feature.id} className="group">
      <div className="space-y-8 py-12 p-8 h-full flex flex-col">
        <img src={feature.icon} className="w-20 mx-auto" alt="" />
        <div className="space-y-2 flex-grow">
          <h5 className="text-xl font-semibold tracking-[0.1rem] text-alpha-600 dark:text-alpha-300">
            {feature.title}
          </h5>
          <p className="text-alpha-800 dark:text-alpha-100">
            {feature.description}
          </p>
        </div>
      </div>
    </Card>
  ))}
</div>
```

### Section Header

```tsx
<h2 className="text-3xl md:text-4xl font-bold tracking-[0.2rem] text-beta-700 dark:text-beta-600 mb-4">
  Grand vision for enterprise analytics
</h2>
```

---

## File Structure

```
src/
├── styles/
│   ├── globals.css          # CSS variables, base styles
│   └── tailwind.css         # Tailwind imports
├── components/
│   ├── ui/                   # shadcn/ui components (customized)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   └── ...
│   ├── layout/
│   │   ├── Container.tsx
│   │   ├── Header.tsx
│   │   └── Footer.tsx
│   └── theme/
│       ├── ThemeProvider.tsx
│       └── ThemeToggle.tsx
└── lib/
    └── utils.ts              # cn() helper
```

---

*Design System maintained by MarketNova Product Team*
