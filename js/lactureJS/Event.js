//  Using event ue can do many thing like onClick , mouseHover
// we can do it in html call in line 
// Or we can do this in specal js file 
// let button = document.querySelector('#button');
// console.log(button);
// button.onclick=()=>{
//     console.log("sayan");
//     // alert("clicked");
// }
// let div=document.querySelector('#div1');
// div.onmousehover=(k)=>{
//     console.log("sayan");
// }

// //// after making indevisual function
// let button = document.querySelector('#button');
// console.log(button);
// function onmouseover1(){
//     console.log("mouse over this div");
// }
// div.onmouseover=onmouseover1;

// //// with out making function
// div.onmouseover=()=>{
//     console.log("mouse over this div");
// }


// ////// event object                        // in event object ue can only make one event at time like only one function is work if other line we decleared another event in same element it will overwright
// //it use to know about the event ditels
// let div = document.querySelector('#div1');
// console.log(button);
// function hover(evt){
//     console.log(evt);
//     console.log(evt.type);//show the event type
//     console.log(evt.toElement);//use to show in which element it working
// }
// div.onmouseover=hover;

// there is more usefull is event listener
// addEventListener                              //it is same like event object and work is same but we can do multiple event using this 
// let div=document.querySelector('#div1');
// function hovAbout(evt){
//     console.log(evt);//to get about event (event object)
// }
// function hovHello(){
//     console.log("hello");//to get about event (event object)
// }
// function hovByy(){
//     console.log("byyy");
// }
// div.addEventListener("mouseover",hovAbout);
// div.addEventListener("mouseover",hovHello);
// div.addEventListener("mouseover",hovByy);


// /////// here we have a option to remove event listener
// div.removeEventListener("mouseover",hovAbout);

