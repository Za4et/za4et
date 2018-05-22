$(document).ready(function () {

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

});