// question 1
//  print 1 to 100 all even numbers

// let i = 0;
// while (i <= 100) {
//     if (i % 2 == 0) {
//         console.log(i);
//     }
//     i++;
// }


//question 2
//make a gasing game

// let val=25;
// let inp=prompt("enter your think :- ");
// while(val != inp){
//     inp=prompt("enter your think :- ");
// }
// console.log("you are right");
// alert("you are right");

// // // // // // // // 3 lectur Qu

// make a user name to take a prompt from user make a use name in this name it have to present start with @ then full name and last its length like @sayanbasani11

// let name=prompt("enter your name : -");
// let lenOfName=name.length;
// let username = `@${name}${lenOfName}`;
// console.log(username);
// alert(username);

// Question 3 loop and array

// calculate the avg of a marks of array 
// let marks = [14,46,78,38,90];
// let total=0,avg;
// let i;
// for(i=0;i<marks.length;i++){
//     total=total+marks[i];
// }
// console.log(`Averag number of this class is ${total/i}`);

// decres all values 10% 

// let price = [100,200,250,300,400];
// console.log(price);
// let discount=10;
// for(let i in price){
//     price[i]=price[i]-(price[i]*discount/100);
// }
// console.log(price);

// Question 4 using arr

// let compani = ['boombarg','microsoft','uber','google','ibm','netflix'];
// //remove first compani from array
// compani.shift();
// console.log(compani);
// //remove uber add ola from it's place 
// compani.splice(1,1,'ola');
// console.log(compani);
// //add amazon at the end 
// compani.push('amazon');
// console.log(compani)


//////////// Question 5
////// find number of vowle in a string using function
// function v(a){
//     let cou=0;
//     for(char of a){
//         if(char == 'a'|| char=='e'||char=='i'||char=='o'||char=='u'){
//             cou++;
//             console.log(char);
//         }
//     }
//     return cou;
// }
// let inp=prompt("enter any thing : ");
// let ans=v(inp);
// console.log(ans);

// write a arrow to find number of vowle in a string 
// const arrowLenString=(str) => {
//     let count=0;
//     for(char of str){
//         if(char == 'a'|| char=='e'||char=='i'||char=='o'||char=='u')
//         {count++;}
//     }
//     return count;
// };
// console.log(arrowLenString("sayan"))

// ////////Qusetion 5
// // find a array all value's squre using forEach loop

// let arr=[1,2,3,4,5];
// arr.forEach((a,b,c)=>{
//     console.log(a**2);
// });

// // find students number who got upto 90+

// let result = [60,59,95,98,89,90,99];
// let cartOfClear = result.filter((value)=>{
//     return value>=90;
// })
// console.log(cartOfClear);

// // make a array acording user prompt and store its index value 
//use reduce methord to calculate sum of this array
// let prom = prompt("enter number : ");
// let arr = [];
// for(let i=0;i<prom;i++){
//     arr[i]=i+1;
// }
// console.log(arr);
// let sumOfArray = arr.reduce((pre,car)=>{
//     return pre+car;
// })
// let productOfArray = arr.reduce((pre,car)=>{
//     return pre*car;
// })
// console.log(sumOfArray);
// console.log(productOfArray);