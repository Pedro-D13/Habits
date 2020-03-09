
// let status = "off";
// function dropdowntoggle() {
//     if (status == "off") {
//         document.getElementById('dropdown-menu').classList.remove("is-hidden");
//         return status = "on";
//     } else {
//         document.getElementById('dropdown-menu').classList.add("is-hidden");
//         return status = "off";
//     }
// };

const dropdowntdl = document.getElementById('dropdown-menu-tdl');
const projectslist = document.getElementById('projects-item');

projectslist.addEventListener('click', function () {
    dropdowntdl.classList.toggle('is-active');
})