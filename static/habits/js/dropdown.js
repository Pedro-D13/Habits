
let status = "off";
function dropdowntoggle() {
    if (status == "off") {
        document.getElementById('dropdown-menu').classList.remove("is-hidden");
        return status = "on";
    } else {
        document.getElementById('dropdown-menu').classList.add("is-hidden");
        return status = "off";
    }
};
