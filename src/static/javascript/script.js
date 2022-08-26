//TODO if date is `SEP` then change to diff color, if `NOV` then change... etc.
const months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];

let cardMonthText = document.querySelector('.date').textContent.slice(-3);
let cardDate = document.querySelector('.date');
let card = document.querySelector('.card-1');
let cardDatesAll = document.querySelectorAll('.date');





function changeColor(s){
    let month = s.toUpperCase();
    if(month === months[8]){ //SEPTEMBER
        cardDate.classList.toggle('accent-1');
        cardDate.classList.toggle('accent-2');

        card.classList.remove('card-1');
        // console.log(card.classList);
        card.classList.add('card-2');
    }
    if(month === months[10]){ //OCTOBER

    }
    // ...etc
}

changeColor(cardMonthText);