let timerId;
let time = 0; 
const stopwatch = document.getElementById("stopwatch");
const lapTimes = document.getElementById("lapTimes");
let sec, millisec;
let lapRecords = []; 

function printTime() {
    time += 10; 
    stopwatch.innerText = getTimeFormatString();
}

function startClock() {
    if (!timerId) { 
        timerId = setInterval(printTime, 10); 
    }
}

function stopClock() {
    if (timerId != null) {
        clearInterval(timerId);
        timerId = null; 
        recordLapTime(); 
    }
}

function resetClock() {
    stopClock();
    stopwatch.innerText = "00:00";
    time = 0;
}

function getTimeFormatString() {
    sec = parseInt(String(time / 1000));
    millisec = parseInt(String(time % 1000) / 10); 

    return String(sec).padStart(2, '0') + ":" + String(millisec).padStart(2, '0');
}

function recordLapTime() {
    if (time > 0) { 
        lapRecords.push(getTimeFormatString());
        updateLapTimes();
    }
}

function updateLapTimes() {
    lapTimes.innerHTML = '';

    lapRecords.forEach((lap, index) => {
        const li = document.createElement('li');
        li.innerText = lap;

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.value = index;

        li.prepend(checkbox);
        lapTimes.appendChild(li);
    });
}

function deleteSelectedLaps() {
    const checkboxes = lapTimes.querySelectorAll('input[type="checkbox"]');
    const indicesToDelete = [];

    checkboxes.forEach((checkbox, index) => {
        if (checkbox.checked) {
            indicesToDelete.push(index);
        }
    });

    // 인덱스를 역순으로 삭제하여 삭제 시 인덱스 문제 방지
    indicesToDelete.reverse().forEach(index => {
        lapRecords.splice(index, 1);
    });

    updateLapTimes();
}

