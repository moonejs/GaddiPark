const timer=document.querySelector('#timer')
const elapsed_minutes=document.querySelector('#elapsed_minutes')
const bookingId = document.querySelector("input[name='booking_id']").value;
const localStorageKey = `startTime_${bookingId}`;
startTime=localStorage.getItem("startTime")

if (!startTime){
    startTime=Date.now()
    localStorage.setItem("startTime",startTime)

}else{
    startTime = parseInt(startTime)
}

function updateTimer(){
    now=Date.now()
    diff=now-startTime

    totalSeconds=Math.floor(diff/1000)
    minutes=Math.floor(totalSeconds/60)
    seconds= totalSeconds%60
    
    timer.textContent =`${minutes} m ${seconds} s`
    elapsed_minutes.value=minutes
}

setInterval(updateTimer,1000)

document.getElementById("release-form").addEventListener("submit", function () {
        localStorage.removeItem("startTime");
});