


// starting value , Avg life expectancy in days, days required to build a habit
// 100  / 29220 * 66
function ageInput() {
    const initial = 100;
    const ageInDays = 29220;
    let ageInput = prompt("Please Enter your age");

    if (Number.isInteger(parseInt(ageInput))) {
        // let ans = initial / ageInDays * ageInput;
        let ans2 = Math.round(ageInDays - (ageInput * 365.25))
        // document.getElementById("tochange").innerHTML = ans + "is the percentage of days ";
        document.getElementById("tochange").innerHTML = ans2 + ": is the number of days you have remaining on average to change your life<br>click below and Join Today!";
    } else if (ageInput == null || ageInput == "") {
        return;
    } else {
        document.getElementById("tochange").innerHTML = "'" + ageInput + "'" + " is not a number";
    };
};

