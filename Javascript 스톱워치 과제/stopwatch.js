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
    lapRecords = []; /
    updateLapTimes();
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
    lapRecords.forEach(lap => {
        const li = document.createElement('li');
        li.innerText = lap;
        lapTimes.appendChild(li);
    });
}
