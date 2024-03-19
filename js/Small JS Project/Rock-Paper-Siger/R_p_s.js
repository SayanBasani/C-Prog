let buttons = document.querySelectorAll(".button_images");
// console.log(buttons);

buttons.forEach((button) => {
    // console.log(button);
    button.addEventListener('click',()=> {
        console.log(button.innerHTML)
    })
})