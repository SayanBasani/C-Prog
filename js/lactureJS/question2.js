// Question 6

// ///////make a html add a h2 heading add "Hello java scripts".append another text with this using js .
// let changeh2 = document.getElementsByTagName('h2');
// console.log(changeh2[0].innerText);
// changeh2[0].innerText = changeh2[0].innerText+" i am sayan";
// console.log(changeh2[0])

// //// make 3 div . add unique text on them using js

let divc = document.getElementsByClassName('con');
console.log(divc);
// divc[0].innerHTML="sayan";
// divc[1].innerHTML="basani";
// divc[2].innerHTML="i mad boy";
let count =0;
for(i of divc){
    i.innerText=`it is my first learn ${count++}`;
}