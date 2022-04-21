const url = window.location.href;

const quizBox = document.getElementById('quiz-box');

const scoreBoxText = document.querySelector('.score-box h4');


$.ajax({
    type: 'GET',
    url: `${url}data/`,
    success: function (response) {
        const data = response.data;
        data.forEach(el => {
            for (let [question, options] of Object.entries(el)) {
                let questionMark = '';
                if (!question.includes('?'))
                    questionMark = ' ?';
                quizBox.innerHTML +=
                    `<hr>
                    <div class="mb-2">
                        <b>${question + questionMark}</b>
                    </div>`;
                options.forEach(option => {
                    quizBox.innerHTML +=
                        `<div class="form-check">
                            <input class="opt" type="radio" name="${question}" id="${option}" value="${option}">
                            <label for="${option}">
                                ${option}
                            </label>
                        </div>`;
                });
            }
        });
    },
    error: function (error) {
        console.log(error);
    },
});
const quizForm = document.getElementById('quiz-form');
const csrfToken = document.getElementsByName('csrfmiddlewaretoken');

const sendData = () => {
    const data = {};
    const elements = [...document.getElementsByClassName('opt')];

    data['csrfmiddlewaretoken'] = csrfToken[0].value;
    elements.forEach(el => {
        if (el.checked)
            data[el.name] = el.value;
        else {
            if (!data[el.name])
                data[el.name] = null;
        }
    });
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function (response) {
            const results = response.results;
            const score = response.score;
            if (response.passed === true){
                scoreBoxText.innerHTML += `<h4>You passed the quiz!</h4>`;
            }
            else {
                scoreBoxText.innerHTML += `<h4>You failed the quiz!</h4>`;
            }
            console.log(score);
            quizForm.classList.add('d-none');
            results.forEach(res => {
                let resDiv = document.createElement('div');
                for (const [question, response] of Object.entries(res)) {
                    resDiv.innerHTML += question;
                    const cls = ['container', 'p-3', 'mb-2', 'h3'];
                    resDiv.classList.add(...cls);
                    if (response === 'not answered') {
                        resDiv.innerHTML += ' - Not answered';
                        resDiv.classList.add('bg-danger');
                    } else {
                        const answer = response['correct_option'];
                        console.log(response);
                        const selected = response['selected'];
                        console.log(answer === selected);
                        if (answer === selected) {
                            resDiv.classList.add('bg-success');
                            resDiv.innerHTML += ` - Correct answer: ${answer}`;
                        } else {
                            resDiv.classList.add('bg-danger');
                            resDiv.innerHTML += ` - Correct answer: ${answer} - Selected: ${selected}`;
                        }
                    }
                }
                const mainDiv = document.getElementById('main-div');
                mainDiv.appendChild(resDiv);
            })
            scoreBoxText.innerHTML += `<h4>Your score is ${score}</h4>`;
        },
        error: function (error) {
            console.log(error);
        },
    });
}
quizForm.addEventListener('submit', e => {
    const confirmation = confirm('Are you sure you want to submit?');
    e.preventDefault();
    if (!confirmation) {
        return;
    }

    sendData();
});
