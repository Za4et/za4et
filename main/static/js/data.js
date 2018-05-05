$(document).ready(function () {

    // var d = new Date();
    //
    // var day = new Array("Воскресенье", "Понедельник", "Вторник",
    //     "Среда", "Четверг", "Пятница", "Суббота");
    //
    // var month = new Array("января", "февраля", "марта", "апреля", "мая", "июня",
    //     "июля", "августа", "сентября", "октября", "ноября", "декабря");

    var oddOrEvenWeek = function () {
        var curDate = new Date(),
            dayShift = 1,
            firstDay = new Date(curDate.getFullYear(), 0, dayShift),
            startYear = new Date(firstDay.getTime()),
            daysInCurYear,
            weekDay = (firstDay.getUTCDay() === 0) ? 7 : firstDay.getUTCDay(); //week day 1-7, 1 is monday, 7 is sunday

        while (weekDay > 1) {
            firstDay = new Date(curDate.getFullYear(), 0, (++dayShift));
            weekDay = (firstDay.getUTCDay() === 0) ? 7 : firstDay.getUTCDay();
        }

        daysInCurYear = ((curDate.getTime() - startYear.getTime()) / 24 / 60 / 60 / 1000) - (7 - dayShift - 1);

        return (Math.floor(daysInCurYear / 7) % 2 === 0) ? 'Неделя: чётная' : 'Неделя: нечётная';
    };

    document.getElementById('week').innerHTML = oddOrEvenWeek();
    // document.getElementById('dateNumber').outerHTML = d.getDate();
    // document.getElementById('dateDay').innerHTML = day[d.getDay()];
    // document.getElementById('dateMonth').innerHTML = month[d.getMonth()];

});