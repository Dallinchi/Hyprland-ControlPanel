   // Получаем элементы формы и индикатора прогресса
   const form = document.getElementById('uploadForm');
   const progressBar = document.getElementById('progressBar');
   const usedSpace = document.getElementById('usedSpace');
   
   // Обработчик события отправки формы
   form.addEventListener('submit', (e) => {
     e.preventDefault(); // Предотвращаем стандартное поведение формы
   
     const formData = new FormData(form);
   
     // Создаем запрос на сервер для отправки файла
     const xhr = new XMLHttpRequest();
     xhr.open('POST', '/api/upload', true);
   
     // Обновляем индикатор прогресса при изменении состояния запроса
     xhr.upload.onprogress = (e) => {
       if (e.lengthComputable) {
         const percentComplete = (e.loaded / e.total) * 100;
         progressBar.style.backgroundColor = '#4caf50';
         progressBar.style.width = percentComplete + '%';
       }
     };
   
     // Обработчик завершения запроса
     xhr.onload = () => {
       if (xhr.status === 200) {
         // Файл успешно загружен
         const response = JSON.parse(xhr.response);
         console.log(response.saved); // Выводим значение 

         console.log('Файл успешно загружен');
         progressBar.style.width = '0px';
         usedSpace.textContent = response.usedspace;
       } else {
         // Произошла ошибка при загрузке файла
         progressBar.style.backgroundColor = 'red';
         console.error('Произошла ошибка при загрузке файла');
       }
     };
   
     // Отправляем запрос на сервер
     xhr.send(formData);
   });