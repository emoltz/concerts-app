//TODO if date is `SEP` then change to diff color, if `NOV` then change... etc.
const months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];

let cardMonth = document.querySelector('.date').textContent.slice(-3);
let cardDatesAll = document.querySelectorAll('.date');





function changeColor(s){
    let month = s.toUpperCase();
    if(month === months[8]){
        console.log("working")
    }
}

changeColor(cardMonth);