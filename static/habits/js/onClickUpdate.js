let status = "off";

function toggle() {
    if (status == "off") {
        document.getElementById('updateform').classList.remove('is-hidden');
        return status = "on";
    } else {
        document.getElementById('updateform').classList.add('is-hidden');
        return status = "off";
    };
};