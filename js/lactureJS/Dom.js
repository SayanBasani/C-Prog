// console.log(document);// it is print only 
// console.dir(document);// it is view the spical objects poperties and methords 

// console.log("sayan");
// window.console.log("sayan2");// same 

// using dom ue acces some poperties of html and we change them . it's class , id and other mata tags;

// // To acces attribut 
// let div = document.querySelector('#div1id');
// console.log("id is :"+div.getAttribute('id'));
// // // // to change the name of the attribute
// console.log('lets see the attribute name :'); 
// console.log(div.getAttribute('class'));
// console.log('lets change the attribute name :'); 
// console.log("lets take a view of class ")
// div.setAttribute('class','sayan');// change the name of the attribute
// console.log(div.getAttribute('class')); 



// /// //// ///// STYLE USING DOM /// // /

// let div = document.querySelector('#div1id');
// div.style.backgroundColor='blue';


// // // // // if we want to add any element (button , pera , h2 ,h1 ) so we have to creat first then we have to add 
// let h1 = document.createElement('h1');//add a h1 tag
// h1.innerText="i am sayan";
// document.querySelector('div').append(h1);//at the last of the selected element
// document.querySelector('div').prepend(h1);//at the start of the selected element
// document.querySelector('div').before(h1);//at the upper outside side of the selected element
// document.querySelector('div').after(h1);//at the end outside of the selected element

// let button = document.createElement('button');
// button.innerText='click me ';
// let pp=document.querySelector('div').prepend(button);

// // // // if we want so we can remove a element
// let pera = document.querySelector('p');
// pera.remove();


// appendchild();
// removechild();

