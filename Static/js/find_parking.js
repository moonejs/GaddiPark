function toggleBookSpot(){
    book_spot_btn=document.querySelectorAll('.book-spot-btn')
    book_spot_model=document.querySelector('.book-spot-model')

    page_1=document.querySelector('.page-1')

    book_spot_btn.forEach(spot => {
        close_model=document.querySelector('.close-book-spot-model')
        spot.addEventListener('click',()=>{
            book_spot_model.style.display='block'
            page_1.classList.add('blur')
        })      
        close_model.addEventListener('click',()=>{
            book_spot_model.style.display='none'
            page_1.classList.remove('blur')
        })
    });
}

function handleVehicleChange(){
    vehicle_select=document.querySelector('#vehicle')
    selected_option=vehicle_select.options[vehicle_select.selectedIndex];
    is_ev=selected_option.getAttribute('data-is-ev')=='True'
    parking_options=document.querySelector('#parking-options')
    
    
    if (is_ev){
        parking_options.style.display='block'
        document.getElementById('regular').checked=true
        
        
    }else{
        parking_options.style.display='none'
        
    }
    updateRates()
    
}
function updateRates(){
    duration=document.querySelector('#duration')
    selected_duration=duration.options[duration.selectedIndex]
    time = parseInt(selected_duration.getAttribute('value'), 10)

    ev_charging_rate=document.querySelector('#ev-charging-rate')
    ev_rate=parseFloat(ev_charging_rate.getAttribute('data-ev-rate'))
    regular_rate_id=document.querySelector('#regular-rate')
    regular_rate=parseFloat(regular_rate_id.getAttribute('data-rate'))
    selected_parking_type=document.querySelector('input[name="parking_type"]:checked')

    estimate_cost=document.querySelector('#estimate_cost')
    hidden_estimate_cost = document.querySelector('#hidden_estimate_cost');

    if (selected_parking_type && selected_parking_type.value ==='ev_charging'){
        ev_charging_rate.style.display='block'
        estimate_cost.value=`Estimate Cost ₹ ${time*ev_rate + time*regular_rate}`
        hidden_estimate_cost.value = time * ev_rate + time * regular_rate;
        
    }else{
        ev_charging_rate.style.display='none'
        console.log(time*regular_rate);
        estimate_cost.value=`Estimate Cost ₹ ${time*regular_rate}`
        hidden_estimate_cost.value = time * regular_rate;
        
    }
        
}


document.addEventListener('DOMContentLoaded',()=>{
    toggleBookSpot()
    toggleConfirmBookingModel()
})