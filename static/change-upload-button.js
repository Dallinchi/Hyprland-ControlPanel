document.getElementById('file-input').addEventListener('change', function() {
  var fileName = this.value.split('\\').pop();  // Получаем имя выбранного файла
  if (fileName.length  > 9) {
    fileName = fileName.substring(0, 9) + '..';  // Обрезаем имя файла до 15 символов и добавляем ".."
  }
  document.querySelector('.btn-panel span').textContent = fileName;  // Меняем текст в теге span
});
