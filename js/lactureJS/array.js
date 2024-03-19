// Array
// they are basecely a object with 'index' as 'key', as we acces object valus using key ,in this case we use index to acces it's related values
// Array is mutable

// let marks = [12,16,15,20];
// console.log(marks)
// console.log(marks.length)//to know about length
// // acces using index value
// console.log(marks[3])//20

// in js array we can store any data types of value in a array 

// let mixarr=["sayan",19,"B.I.T","C.S,T"];
// console.log(mixarr)
// // using index to acces 
// console.log(mixarr[2]);
// console.log(mixarr['2']);
// // in here we can change any position value 
// mixarr[1]=20;
// console.log(mixarr);
// console.log(mixarr[1]);


// print array one by one 

// let arr=['karan','sayan','anish','riju'];
// for(let i=0;i<arr.length;i++){
//     console.log(arr[i]);
// }


// array used functions
////// push() to add element in the back of the array

// let arr=['karan','sayan','anish','riju'];
// console.log(arr);
// arr.push("rocky");
// console.log(arr);
////// pop() it is help to pop a element from end from the array and return this value

// let popItem=arr.pop();
// console.log(popItem);
// console.log(arr);

////// toString() use convert a array in a string 

// let ans=arr.toString();
// console.log(ans);
// console.log(typeof(ans));//string

/////// concat() to add two ore more then arrays,//they add one by one in sequence 
// let boys=['karan','sayan','anish','riju'];
// let girls=['shreya','ankita','eshika','retuporna'];
// let teachers=['joyita','samol','sumon'];
// let all=boys.concat(girls,teachers);//(11) ['karan', 'sayan', 'anish', 'riju', 'shreya', 'ankita', 'eshika', 'retuporna', 'joyita', 'samol', 'sumon']
// console.log(all);

// unshift() use (like push()) to add element in the fornt 
// let boys=['karan','sayan','anish','riju'];
// console.log(boys);
// boys.unshift('sanket');//['sanket', 'karan', 'sayan', 'anish', 'riju']
// console.log(boys);
// // shift() use (like pop()) to remove from front and it return shift item
// let shiftItem=boys.shift();
// console.log(boys);
// console.log(shiftItem);

////// slice() to cut from prtecular index
////// splice() use to add , remove , replace ////if it remove of pop any items so it return them
// let boys=['sanket', 'karan', 'sayan', 'anish', 'riju'];
// boys.splice(3,2);//remove 3 etement from 2 index
// console.log(boys);
// boys.splice(2,0,'arijit','aju');//add element from 2 index
// console.log(boys);
