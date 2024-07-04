document.addEventListener("DOMContentLoaded", () => {
    const maxAttempts = 10;
    let attemptsLeft = maxAttempts;
    let answer = generateRandomNumbers();
    
    function generateRandomNumbers() {
        let numbers = [];
        while (numbers.length < 3) {
            let num = Math.floor(Math.random() * 10);
            if (!numbers.includes(num)) {
                numbers.push(num);
            }
        }
        return numbers;
    }
    
    function resetGame() {
        attemptsLeft = maxAttempts;
        answer = generateRandomNumbers();
        document.querySelectorAll('.input-field').forEach(input => input.value = '');
        document.querySelector('.result-display').innerHTML = '';
        document.getElementById('game-result-img').src = '';
        document.querySelector('.submit-button').disabled = false;
    }
    
    function checkNumbers() {
        const inputs = document.querySelectorAll('.input-field');
        let inputValues = Array.from(inputs).map(input => input.value);
        
        if (inputValues.includes('')) {
            inputs.forEach(input => input.value = '');
            return;
        }
        
        let inputNumbers = inputValues.map(value => parseInt(value));
        let result = calculateResult(inputNumbers);
        displayResult(inputNumbers, result);
        
        attemptsLeft--;
        
        if (result.strikes === 3) {
            endGame(true);
        } else if (attemptsLeft === 0) {
            endGame(false);
        }
    }
    
    function calculateResult(inputNumbers) {
        let strikes = 0;
        let balls = 0;
        
        inputNumbers.forEach((num, index) => {
            if (num === answer[index]) {
                strikes++;
            } else if (answer.includes(num)) {
                balls++;
            }
        });
        
        return { strikes, balls };
    }
    
    function displayResult(inputNumbers, result) {
        const resultDisplay = document.querySelector('.result-display');
        let resultDiv = document.createElement('div');
        resultDiv.className = 'check-result';
        
        let leftDiv = document.createElement('div');
        leftDiv.className = 'left';
        leftDiv.textContent = inputNumbers.join(' ');
        
        let rightDiv = document.createElement('div');
        rightDiv.className = 'right';
        
        if (result.strikes === 0 && result.balls === 0) {
            let outDiv = document.createElement('div');
            outDiv.className = 'out num-result';
            outDiv.textContent = 'O';
            rightDiv.appendChild(outDiv);
        } else {
            if (result.strikes > 0) {
                rightDiv.innerHTML += `${result.strikes} <div class="strike num-result">S</div>`;
            }
            if (result.balls > 0) {
                rightDiv.innerHTML += `${result.balls} <div class="ball num-result">B</div>`;
            }
        }
        
        resultDiv.appendChild(leftDiv);
        resultDiv.appendChild(rightDiv);
        resultDisplay.appendChild(resultDiv);
    }
    
    function endGame(isWin) {
        const resultImg = document.getElementById('game-result-img');
        resultImg.src = isWin ? 'success.png' : 'fail.png';
        document.querySelector('.submit-button').disabled = true;
    }
    
    document.querySelector('.submit-button').addEventListener('click', checkNumbers);
    
    resetGame();
});