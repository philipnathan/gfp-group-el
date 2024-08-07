/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
     "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        'custom-green': '#206900',
        'custom-Olive-Drab': '#597226',
        'custom-pastel-green': '#cadcbf',
        'custom-light-over-green': '#93bc3f',
        'custom-steel-blue' : '#4c8da8',
        'custom-Gunmetal' : '#242c34',
        'custom-soft-blue' : '#74b3d4',
        'custom-light-blue' : '#b4ccdc'
      },
      // backgroundImage:{
      //   'custom-backround': "url('/baground.png')",
      // }
    },
  },
  plugins: [],
}
