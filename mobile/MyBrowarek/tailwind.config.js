/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./App.tsx", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        'yellow': {
          '100': '#EFC84F',
          '90': '#F1CE61',
          '80': '#F2D372',
          '70': '#F4D984',
          '60': '#F5DE95',
          '50': '#F6E3A6',
          '40': '#F9E9B9',
          '30': '#FBEFCB',
          '20': '#FCF4DC',
          '10': '#FEFAEE',

        },
        'cream': {
          '100': '#F9F4E2',
          '90': '#FAF6E5',
          '80': '#FAF6E8',
          '70': '#FBF8EB',
          '60': '#FBF8EE',
          '50': '#FBF9F0',
          '40': '#FDFBF3',
          '30': '#FEFCF7',
          '20': '#FEFDF9',
          '10': '#FFFEFD',
        },
        'red':{
          '100': '#E45F36',
          '90': '#E76F4B',
          '80': '#E97F5E',
          '70': '#ED8F73',
          '60': '#EF9F86',
          '50': '#F1AE9A',
          '40': '#F4BFAF',
          '30': '#F7CFC3',
          '20': '#FADFD7',
          '10': '#FDEFEB',
        },
        'porto':{
          '100': '#330B0B',
          '90': '#482424',
          '80': '#5C3C3C',
          '70': '#715555',
          '60': '#856D6D',
          '50': '#988484',
          '40': '#AD9D9D',
          '30': '#C2B6B6',
          '20': '#D6CECE',
          '10': '#EBE7E7',
        }

      }
    },
  },
  plugins: [],
}

