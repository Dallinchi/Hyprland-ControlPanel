
function send(url) {
    fetch('http://192.168.1.4:5566' + url, {
        method: 'GET'
    })
        .then(response => response.json())
        .then(data => { })
        .catch(error => console.error('Error:', error));
}
function updateTitle(player) {
    return fetch('http://192.168.1.4:5566/api/player/' + player + '/title', {
        method: 'GET'
    })
        .then(response => response.json())
        .then(data => {
            return data;
        })
        .catch(error => console.error('Error:', error));
}
function updateStatus(player) {
    return fetch('http://192.168.1.4:5566/api/player/' + player + '/status', {
        method: 'GET'
    })
        .then(response => response.text())
        .then(data => {
            return data;
        })
        .catch(error => console.error('Error:', error));
}

const parentElement = document.getElementById('main-panel');

// Управление через Amixer
const panelElement = document.createElement('div');
panelElement.className = 'panel';


const btnPanelElement = document.createElement('div');
btnPanelElement.className = 'btn-panel';
const spanElement = document.createElement('span');
spanElement.textContent = 'Amixer';
btnPanelElement.appendChild(spanElement);


// Кнопки громкости плеера
const btnContainerVolume = document.createElement('div');
btnContainerVolume.className = 'btn-container';

const buttonVolumeDown = document.createElement('button');
buttonVolumeDown.className = 'control-btn';
buttonVolumeDown.id = 'btn-' + 'amixer' + '-volume-down';
buttonVolumeDown.textContent = '-';
buttonVolumeDown.addEventListener("click", function () {
    send('/api/player/volume/down');
});

const buttonVolumeUp = document.createElement('button');
buttonVolumeUp.className = 'control-btn';
buttonVolumeUp.id = 'btn-' + 'amixer' + '-volume-up';
buttonVolumeUp.textContent = '+';
buttonVolumeUp.addEventListener("click", function () {
    send('/api/player/volume/up');
});

btnContainerVolume.appendChild(buttonVolumeDown)
btnContainerVolume.appendChild(buttonVolumeUp)
btnPanelElement.appendChild(btnContainerVolume);


// Прочее
panelElement.appendChild(btnPanelElement);
parentElement.appendChild(panelElement);


fetch('http://192.168.1.4:5566/api/player/players')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        data.forEach(item => {
            const panelElement = document.createElement('div');
            panelElement.className = 'panel';


            const btnPanelElement = document.createElement('div');
            btnPanelElement.className = 'btn-panel';
            const spanElement = document.createElement('span');
            // Почему такое чувство, что я делаю что-то плохое?
            // Впрочем какая разница, если это работает ^-^
            updateTitle(item)
                .then(title => {
                    spanElement.textContent = item + " - " + title;
                });
            btnPanelElement.appendChild(spanElement);

            // Кнопки Назад Плей/Пауза Вперед
            const btnContainerPlayerControl = document.createElement('div');
            btnContainerPlayerControl.className = 'btn-container';
            
            const buttonPrev = document.createElement('button');
            buttonPrev.className = 'control-btn';
            buttonPrev.id = 'btn-' + item + '-prev';
            buttonPrev.textContent = '<-';
            buttonPrev.addEventListener("click", function () {
                send('/api/player/' + item + '/previous');
                updateTitle(item)
                .then(title => {
                    spanElement.textContent = item + " - " + title;
                });
            });
            
            const buttonPlayPause = document.createElement('button');
            buttonPlayPause.className = 'control-btn';
            buttonPlayPause.id = 'btn-' + item + '-play-pause';
            buttonPlayPause.textContent = 'play | pause';
            buttonPlayPause.addEventListener("click", function () {
                send('/api/player/' + item + '/play-pause');
                updateStatus(item)
                    .then(status => {
                        status = status.replace(/"/g, '').replace(/\\n/g, '');
                        console.log(status)

                        if (status == "Playing") {
                            buttonPlayPause.innerHTML = "<i class='nf nf-fa-play'></i>";
                        } else {
                            buttonPlayPause.innerHTML = "<i class='nf nf-fa-pause'></i>";
                        }
                    });
            });
            updateStatus(item)
                .then(status => {
                    status = status.replace(/"/g, '').replace(/\\n/g, '');
                    console.log(status)

                    if (status == "Playing") {
                        buttonPlayPause.innerHTML = "<i class='nf nf-fa-pause'></i>";
                    } else {
                        buttonPlayPause.innerHTML = "<i class='nf nf-fa-play'></i>";
                    }
                });

            const buttonNext = document.createElement('button');
            buttonNext.className = 'control-btn';
            buttonNext.id = 'btn-' + item + '-next';
            buttonNext.textContent = '->';
            buttonNext.addEventListener("click", function () {
                send('/api/player/' + item + '/next');
                updateTitle(item)
                    .then(title => {
                        spanElement.textContent = item + " - " + title;
                    });
            });

            btnPanelElement.appendChild(btnContainerPlayerControl);
            btnContainerPlayerControl.appendChild(buttonPrev)
            btnContainerPlayerControl.appendChild(buttonPlayPause);
            btnContainerPlayerControl.appendChild(buttonNext)


            // Кнопки громкости плеера
            const btnContainerVolume = document.createElement('div');
            btnContainerVolume.className = 'btn-container';

            const buttonVolumeDown = document.createElement('button');
            buttonVolumeDown.className = 'control-btn';
            buttonVolumeDown.id = 'btn-' + item + '-volume-down';
            buttonVolumeDown.textContent = '-';
            buttonVolumeDown.addEventListener("click", function () {
                send('/api/player/' + item + '/volume/-0.1');
            });

            const buttonVolumeUp = document.createElement('button');
            buttonVolumeUp.className = 'control-btn';
            buttonVolumeUp.id = 'btn-' + item + '-volume-up';
            buttonVolumeUp.textContent = '+';
            buttonVolumeUp.addEventListener("click", function () {
                send('/api/player/' + item + '/volume/0.1');
            });

            btnContainerVolume.appendChild(buttonVolumeDown)
            btnContainerVolume.appendChild(buttonVolumeUp)
            btnPanelElement.appendChild(btnContainerVolume);


            // Прочее
            panelElement.appendChild(btnPanelElement);
            parentElement.appendChild(panelElement);
        });
    })
    .catch(error => console.error('Error:', error));