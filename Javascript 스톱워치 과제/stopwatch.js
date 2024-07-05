let timerId;
let time = 0; // 밀리초 단위로 변경
const stopwatch = document.getElementById("stopwatch");
let sec, millisec;

function printTime() {
    time += 10; // 10밀리초씩 증가
    stopwatch.innerText = getTimeFormatString();
}

function startClock() {
    printTime();
    stopClock();
    timerId = setTimeout(startClock, 10); // 10밀리초 간격으로 변경
}

function stopClock() {
    if (timerId != null) {
        clearTimeout(timerId);
    }
}

function resetClock() {
    stopClock();
    stopwatch.innerText = "00:00";
    time = 0;
}

function getTimeFormatString() {
    sec = parseInt(String(time / 1000));
    millisec = parseInt(String(time % 1000) / 10); // 밀리초를 10으로 나눠 2자리로 만듦

    return String(sec).padStart(2, '0') + ":" + String(millisec).padStart(2, '0');
}
