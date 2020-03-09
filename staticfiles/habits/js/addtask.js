// let addtaskinput = "off";
// function toggleaddtask() {
//     if (addtaskinput == "off") {
//         document.getElementById('addtaskinput').classList.remove('is-hidden');
//         document.getElementById('addtaskbutton').classList.add('is-hidden');
//         return addtaskinput = "showing";
//     } else {
//         document.getElementById('addtaskinput').classList.add('is-hidden');
//         document.getElementById('addtaskbutton').classList.remove('is-hidden');
//         return addtaskinput = "off";
//     };
// };


const addTaskButton = document.getElementById('addtaskbutton');
const addTaskInput = document.getElementById('addtaskinput');
const cancel = document.getElementById('cancel')

// Adds an event listener to the add task button, toggles what you see 
addTaskButton.addEventListener('click', function hideAdd() {
    addTaskInput.classList.toggle('is-hidden');
    addTaskButton.classList.toggle('is-hidden');
});

cancel.addEventListener('click', function () {
    document.getElementById('id_title').value = '';
    addTaskButton.click();
});