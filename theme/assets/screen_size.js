// Detecta el ancho de la pantalla y lo expone globalmente
function getScreenWidth() {
  return window.innerWidth;
}

// Asegúrate de que esté disponible globalmente
window.getScreenWidth = getScreenWidth;
