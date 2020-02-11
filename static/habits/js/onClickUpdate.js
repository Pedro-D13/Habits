let status = "off";
function toggle(arg) {
    if (status == "off") {
        document.getElementById(arg).classList.remove('is-hidden');
        return status = "on";
    } else {
        document.getElementById(arg).classList.add('is-hidden');
        return status = "off";
    };
};

