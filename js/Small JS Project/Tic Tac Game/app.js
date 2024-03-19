let boxs = document.querySelectorAll(".options");
let val = 0;
let valu="";
let winperson="";

let winArrs = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6],
];


// function full_check(){
//   let res = false ; 
//   boxs.forEach((box)=>{
//     let m = document.querySelector(box).innerText;
//     console.log(`s${m}s`);
//     if(m == ''){
//       // return true;
//     }
//   })
//   return false;
// }


const checkWinner = (winPatterns , arr) => {
  for (pattern of winPatterns) {
    let cou =0;
    for(ele_pat of pattern){
      // element of user arr
      for(i of arr){
        if(ele_pat == i){
          cou++;
        }
      }
      if(cou == 3){
        return 1;
      }
    }
  }
  return 0;
};

let xArr=[];
let oArr=[];
boxs.forEach((box)=>{
    // // console.log(`sa${full_check}sa`);
    // full_check;
    
    box.addEventListener("click",()=>{
        if(val == 0){
            box.innerText="X";
            xArr.push(box.value);
            console.log(`selected by x is ${box.value}`);
            val = 1;
            console.log(xArr);
            valu = checkWinner(winArrs , xArr);
            if(valu == 1){
              alert("Winner is X");
              winperson="O";
            }
        }else if (val == 1){
            box.innerHTML="O";
            oArr.push(box.value);
            console.log(`selected by o is ${box.value}`);
            val = 0;
            console.log(oArr);
            valu = checkWinner(winArrs , oArr);
            if(valu == 1){
              alert("Winner is O");
              winperson="O";
            }
        }
        box.disabled=true;
        console.log (`win person is {${winperson}}`)
        if(winperson==="O"){
          console.log("it is complet one tern of a game ");
          restart();
        }
    });
});
const restart=()=> {
  console.log("sayan");
  boxs.forEach((box)=>{
    box.disabled=false;
    box.innerText=" ";
  })
    console.log(winArrs);
    xArr=[];
    oArr=[];
    console.log("all clear");
    console.log(winArrs);
    val=0;
    valu="";
    winperson=""
}
re= document.querySelector(".reset_bt");
re.onclick=restart;
