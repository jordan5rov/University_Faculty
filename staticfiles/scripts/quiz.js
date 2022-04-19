const url = window.location.href;

const quizBox = document.getElementById('quiz-box');

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response){
        console.log(response);
        const data = response.data;
        data.forEach(el =>{
           for (let [question, options] of Object.entries(el)){
               if (!question.includes('?'))
                   question += ' ?';
               quizBox.innerHTML +=
                   `<hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>`;
               options.forEach(option =>{
                   quizBox.innerHTML +=
                       `<div class="form-check">
                            <input class="ans form-check-input" type="radio" name="${question}" id="${option}" value="${option}">
                            <label class="form-check-label" for="${option}">
                                ${option}
                            </label>
                        </div>`;
               });
           }
        });
    },
    error: function (error){
        console.log(error);
    },
});
