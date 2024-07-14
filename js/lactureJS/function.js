////////// function are use to work a particular task multiple time . It is easy reinvoke in code . 
// function sum(a,b) {
//     return a+b;
// } 
// console.log(sum(3,4));

/////////// Arrow function -- in this function's syntex is different

// const arrowFunction = (a,b) => {return a+b;}
// console.log(arrowFunction(4,6));

// ////////// forEach loop
// this is use for array only . use to run a function on a array elements 
// // in this function the argument can be a value or a function

// let arr=[1,2,3,4,5]
// arr.forEach((val,inx,a)=> {
//     console.log(val);
//     console.log(inx);
//     console.log(a);
// });


////try forEach loop..
// let friend=['sayan','karan','sontu','riju','bokachoda'];
// friend.forEach((value,index,array)=>{
    //     console.log(value+' '+index);
    // })
// let count=[1,2,3,4,5,6]
// let ans=0;
// count.forEach((i)=>{
//     ans+=i;
// })
// console.log(ans);


// // Higer order function 
// which function use other functions as a paramiter or return a function as a output;


/////// //// map();
// it is used to applied a function on a array all valus . it is take a function as a argument or it can return a function as a output;
// this like forEach(); loop,work is same but it can return a diffrent array 

// let arr = [9,8,7,6,5,4,3];
// let squreOfArr=arr.map((value)=>{
//     return value**2;
// })
// console.log(squreOfArr);