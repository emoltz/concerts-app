//TODO if date is `SEP` then change to diff color, if `NOV` then change... etc.
const months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];

//ELEMENTS
let cardDate = document.querySelector('.date');
let card = document.querySelector('.card-1');
let cardDatesAll = document.querySelectorAll('.date');
const allCards = document.querySelectorAll('.card');

//BASED ON MONTH
function changeColor(s) {
    let month = s.toUpperCase();
    if (month === months[8]) { //SEPTEMBER
        cardDate.classList.toggle('accent-1');
        cardDate.classList.toggle('accent-2');

        card.classList.remove('card-1');
        // console.log(card.classList);
        card.classList.add('card-2');
    }
    if (month === months[10]) { //OCTOBER

    }
    // ...etc
}

let currentColor = null;
let currentAccentColor = null;
let cardColors = [
    'card-color-1',
    'card-color-2',
    'card-color-3',
];

let accentColors = [
    'accent-1',
    'accent-2',
    'accent-3',
]
//PAIRS OF THREE
let j = 0;

function changeColorPairs() {
    for (let i = 0; i < allCards.length; i++) {
        if (i % 3 === 0) {
            currentColor = cardColors[j];
            currentAccentColor = accentColors[j];
            j++;
            if (j === 3) {
                j = 0;
            }

        }
        allCards[i].classList.toggle(currentColor); //switch colors
        if (!allCards[i].classList.contains(cardColors[0])) { //if it's the original, add it back
            allCards[i].classList.toggle(cardColors[0]);
        }

        cardDatesAll[i].classList.toggle(currentAccentColor);
        if(!cardDatesAll[i].classList.contains(accentColors[0])){
            cardDatesAll[i].classList.toggle(accentColors[0]);
        }

    }
}

changeColorPairs()