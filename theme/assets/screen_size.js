// Detecta el ancho de la pantalla y lo expone globalmente
function getScreenWidth() {
  return window.innerWidth;
}

// Aseg�rate de que est� disponible globalmente
window.getScreenWidth = getScreenWidth;
