const url = window.location.href;

const quizBox = document.getElementById('quiz-box');

const scoreBoxText = document.querySelector('.score-box h4');


$.ajax({
    type: 'GET',
    url: `${url}data/`,
    success: function (response) {
        const data = response.data;
        const data_pk = response.data_pk;
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
                            <input class="opt" type="radio" name="${question}" id="${data_pk[question]}" value="${option}">
                            <label for="${data_pk[question]}">
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
            data[el.id] = el.value;
        else {
            if (!data[el.id])
                data[el.id] = null;
        }
    });

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function (response) {
            const results = response.results;
            const score = response.score;
            const max_score = response.max_score;
            if (response.passed === true){
                scoreBoxText.innerHTML += `<h4>You passed the quiz!</h4>`;
            }
            else {
                scoreBoxText.innerHTML += `<h4>You failed the quiz!</h4>`;
            }
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
                        const selected = response['selected'];

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
            scoreBoxText.innerHTML += `<h4>Your score is ${score}/${max_score}</h4>`;
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
