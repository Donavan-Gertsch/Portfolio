var counter = 1;
window.onload = function(){

  let next = document.getElementById("next");
  next.addEventListener("click", ahead);
  let previous = document.getElementById("prev");
  previous.addEventListener("click", behind);
}

function ahead(){

  if(counter==1){
  let newnext = document.getElementById("slide-Container");
  newnext.style.backgroundImage = "url('world/2.jpg')";
    counter++;
  } else if (counter==2){
    let newnext = document.getElementById("slide-Container");
  newnext.style.backgroundImage = "url('world/3.jpg')";
    counter++;
  }
  else{
    let newnext = document.getElementById("slide-Container");
  newnext.style.backgroundImage = "url('world/1.jpg')";
    counter -= 2;
  }
}
function behind(){
  if(counter==1){
    let oldprev = document.getElementById("slide-Container");
    oldprev.style.backgroundImage = "url('world/3.jpg')";
    counter +=2;
  }else if(counter==2){
    let oldprev = document.getElementById("slide-Container");
    oldprev.style.backgroundImage = "url('world/1.jpg')";
    counter--;
  }
  else{
        let oldprev = document.getElementById("slide-Container");
    oldprev.style.backgroundImage = "url('world/2.jpg')";
    counter--;
  }
}