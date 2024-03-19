// let body = document.querySelector('body');
// body.style.backgroundColor='black';
let newEle = document.createElement("button");
newEle.style.width='200px';
newEle.innerText='click me';
newEle.style.color='red';
document.querySelector("body").append(newEle);


let p=document.createElement('p');
p.innerText='it is a try of js ';
p.setAttribute('class','p1');
document.querySelector('body').prepend(p);
let pp=document.getElementsByClassName('p1');
console.log(pp);
p.setAttribute('id','sty');
let pSty=document.getElementById('sty');
pSty.style.color='green';
pSty.style.fontSize='25px';
pSty.style.display='inline';
pSty.style.backgroundColor='black';
