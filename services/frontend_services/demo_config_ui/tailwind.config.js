/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
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
        // Alpha Muted
        'alpha-muted': {
          50: '#f1eff6',
          100: '#e3deed',
          200: '#c7beda',
          300: '#ab9dc8',
          400: '#8f7cb6',
          500: '#745ca3',
          600: '#5c4983',
          700: '#453762',
          800: '#2e2541',
          900: '#171221',
          950: '#100d17',
        },
        // Alpha Faded
        'alpha-faded': {
          50: '#f2f1f4',
          100: '#e5e3e8',
          200: '#cac7d1',
          300: '#b0abba',
          400: '#968fa3',
          500: '#7b738c',
          600: '#635c70',
          700: '#4a4554',
          800: '#312e38',
          900: '#19171c',
          950: '#111014',
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
        '4xl': '2rem',
      },
      boxShadow: {
        'glow': '0 0 20px rgba(92, 22, 233, 0.3)',
        'glow-lg': '0 0 40px rgba(92, 22, 233, 0.4)',
      },
    },
  },
  plugins: [],
}
