var x,y=100;
function functionscroll1(){
	y=100;
	clearInterval(x);
	document.getElementById("divslide1").style.zIndex="1200";
	document.getElementById("divslide2").style.zIndex="0";
	document.getElementById("divslide3").style.zIndex="0";
	document.getElementById("divslide4").style.zIndex="0";
	x=setInterval("func1()",40);
}
function func1(){
	y=y-5;
	if(y===0){
		clearInterval(x);
		document.getElementById("divslide2").style.top="100%";
		document.getElementById("divslide3").style.top="100%";
		document.getElementById("divslide4").style.top="100%";
		document.getElementById("divheader").style.backgroundColor="red";
		document.getElementById("divnav1").style.backgroundColor="black";
		document.getElementById("divnav2").style.backgroundColor="white";
		document.getElementById("divnav3").style.backgroundColor="white";
		document.getElementById("divnav4").style.backgroundColor="white";
		document.getElementById("divnav1").style.boxShadow="0px 0px 2px 2px white";
		document.getElementById("divnav2").style.boxShadow="0px 0px 0px 0px black";
		document.getElementById("divnav3").style.boxShadow="0px 0px 0px 0px black";
		document.getElementById("divnav4").style.boxShadow="0px 0px 0px 0px black";
	}
	document.getElementById("divslide1").style.top=y+"%";
}

function functionscroll2(){
	y=100;
	clearInterval(x);
	document.getElementById("divslide2").style.zIndex="1200";
	document.getElementById("divslide1").style.zIndex="0";
	document.getElementById("divslide3").style.zIndex="0";
	document.getElementById("divslide4").style.zIndex="0";
	x=setInterval("func2()",40);
}
function func2(){
	y=y-5;
	if(y===0){
	clearInterval(x);
		document.getElementById("divslide1").style.top="100%";
		document.getElementById("divslide3").style.top="100%";
		document.getElementById("divslide4").style.top="100%";
		document.getElementById("divheader").style.backgroundColor="rgba(110,100,150,0.6)";
		document.getElementById("divnav2").style.backgroundColor="black";
		document.getElementById("divnav1").style.backgroundColor="white";
		document.getElementById("divnav3").style.backgroundColor="white";
		document.getElementById("divnav4").style.backgroundColor="white";
		document.getElementById("divnav2").style.boxShadow="0px 0px 2px 2px white";
		document.getElementById("divnav1").style.boxShadow="none";
		document.getElementById("divnav3").style.boxShadow="none";
		document.getElementById("divnav4").style.boxShadow="none";
	}
	document.getElementById("divslide2").style.top=y+"%";
}

function functionscroll3(){
	y=100;
	clearInterval(x);
	document.getElementById("divslide3").style.zIndex="1200";
	document.getElementById("divslide2").style.zIndex="0";
	document.getElementById("divslide1").style.zIndex="0";
	document.getElementById("divslide4").style.zIndex="0";
	x=setInterval("func3()",40);
}
function func3(){
	y=y-5;
	if(y===0){
		clearInterval(x);
		document.getElementById("divslide2").style.top="100%";
		document.getElementById("divslide1").style.top="100%";
		document.getElementById("divslide4").style.top="100%";
		document.getElementById("divheader").style.backgroundColor="rgba(89,166,166,0.6)";
		document.getElementById("divnav3").style.backgroundColor="black";
		document.getElementById("divnav1").style.backgroundColor="white";
		document.getElementById("divnav2").style.backgroundColor="white";
		document.getElementById("divnav4").style.backgroundColor="white";
		document.getElementById("divnav3").style.boxShadow="0px 0px 2px 2px white";
		document.getElementById("divnav1").style.boxShadow="0px 0px 0px 0px white";
		document.getElementById("divnav2").style.boxShadow="0px 0px 0px 0px white";
		document.getElementById("divnav4").style.boxShadow="0px 0px 0px 0px white";
	}
	document.getElementById("divslide3").style.top=y+"%";
}

function functionscroll4(){
	y=100;
	clearInterval(x);
	document.getElementById("divslide1").style.zIndex="0";
	document.getElementById("divslide2").style.zIndex="0";
	document.getElementById("divslide3").style.zIndex="0";
	document.getElementById("divslide4").style.zIndex="1200";
	x=setInterval("func4()",40);
}
function func4(){
	y=y-5;
	if(y===0){
		clearInterval(x);
		document.getElementById("divslide2").style.top="100%";
		document.getElementById("divslide1").style.top="100%";
		document.getElementById("divslide3").style.top="100%";
		document.getElementById("divheader").style.backgroundColor="rgba(51,51,204,0.6)";
		document.getElementById("divnav3").style.backgroundColor="white";
		document.getElementById("divnav1").style.backgroundColor="white";
		document.getElementById("divnav2").style.backgroundColor="white";
		document.getElementById("divnav4").style.backgroundColor="black";
		document.getElementById("divnav3").style.boxShadow="0px 0px 0px 0px white";
		document.getElementById("divnav1").style.boxShadow="0px 0px 0px 0px white";
		document.getElementById("divnav2").style.boxShadow="0px 0px 0px 0px white";
		document.getElementById("divnav4").style.boxShadow="0px 0px 2px 2px white";
	}
	document.getElementById("divslide4").style.top=y+"%";
}


