let button = document.querySelector("#envButt_both");
let button1 = document.querySelector("#envButt1");
let button2 = document.querySelector("#envButt2");
let button_para = document.querySelector("#envName");
let dis_body = document.getElementsByTagName("body")[0];
var v = 0;

// simple version using 2 button change color of diplay
button2.addEventListener("click",() => {
    dis_body.style.backgroundColor="blue";
});
button1.addEventListener("click",() =>{
    dis_body.style.backgroundColor='red';
});

// using a single button change display color dark or light 
button.addEventListener("click",() => {
    if(v==0){
    dis_body.style.backgroundColor="black";
    button_para.innerHTML="Dark"
    v = 1;
    }else if (v == 1){
        dis_body.style.backgroundColor="white";
        button_para.innerHTML="Light"
        v = 0;
    }
});