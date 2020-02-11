


// starting value , Avg life expectancy in days, days required to build a habit
// 100  / 29220 * 66
function ageInput() {
    const ageInDays = 29220;
    let ageInput = prompt("Please Enter your age");

    if (Number.isInteger(parseInt(ageInput)) && parseInt(ageInput) < 80 && parseInt(ageInput) > 16) {
        // let ans = initial / ageInDays * ageInput;
        let ans2 = Math.round(ageInDays - (ageInput * 365.25))
        // document.getElementById("tochange").innerHTML = ans + "is the percentage of days ";
        document.getElementById("tochange").innerHTML = ans2 + " days" + ": is the number of days you have remaining on average to change your life<br>click below and start today!";
    } else if (ageInput == null || ageInput == "") {
        return;
    } else if (parseInt(ageInput) >= 80) {
        document.getElementById("tochange").innerHTML = "err, wow!, I mean it's never too late to change! <br>(but is it really though?) Join Today to get started";
    } else if (parseInt(ageInput) <= 16) {
        document.getElementById("tochange").innerHTML = "well it's never too early to start, and here's some free advice. <br>Getting your homework done is a great start";
    } else {
        document.getElementById("tochange").innerHTML = "'" + ageInput + "'" + " is not a number";
    };
};

