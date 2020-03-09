let edit_status = "off";
function toggle(arg) {
    if (edit_status == "off") {
        document.getElementById(arg).classList.remove('is-hidden');
        return edit_status = "on";
    } else {
        document.getElementById(arg).classList.add('is-hidden');
        return edit_status = "off";
    };
};

// const goalUpdateBtn = document.getElementById('goalupdatebtn');

// goalUpdateBtn.addEventListener('click', function () {
//     // you will need to watch the video by dev ed, for handling parent and child nodes etc

// });