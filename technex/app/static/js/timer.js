dateFuture1 = new Date(2012,2,16,23,59,59); 
function GetCount(ddate,iid){ 
 
 dateNow = new Date();
 amount = ddate.getTime() - dateNow.getTime();
 delete dateNow; 
  if(amount < 0){ 
  document.getElementById(iid).innerHTML="Now!"; 
 } 
 else{ 
  days=0;hours=0;mins=0;secs=0;out=""; 
 
  amount = Math.floor(amount/1000);
 
  days=Math.floor(amount/86400);
  amount=amount%86400; 
 
  hours=Math.floor(amount/3600);
  amount=amount%3600; 
 
  mins=Math.floor(amount/60);
  amount=amount%60; 
 
  secs=Math.floor(amount);
 
  if(days != 0){out += days +" "+((days==1)?"D":"D")+", ";} 
  out += (hours<=9?'0':'')+hours +" "+((hours==1)?"":"")+": "; 
  out += (mins<=9?'0':'')+mins +" "+((mins==1)?"":"")+": "; 
  out += (secs<=9?'0':'')+secs +" "+((secs==1)?"":"")+"TECHNEX 2012 COUNTDOWN"; 
  out = out.substr(0,out.length-0); 
  document.getElementById(iid).innerHTML=out; 
 
  setTimeout(function(){GetCount(ddate,iid)}, 1000); 
 } 
} 
 
window.onload=function(){ 
 GetCount(dateFuture1, 'timer'); 
 }; 
