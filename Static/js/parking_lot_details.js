function toggleSpotDetails(){
    const booked_model=document.querySelector('.booked-spot-model')
    const vacant_model = document.querySelector('.vacant-spot-model');
    const page_1=document.querySelector('.page-1')

    let has_spot = false;
    let is_booked = false;


    has_spot = page_1.dataset.hasSpot === "true";
    is_booked = page_1.dataset.isBooked === "true";

    if (has_spot){
        if (is_booked){
            booked_model.style.display='block'
            page_1.classList.add('blur')
        }else{
            vacant_model.style.display='block'
            page_1.classList.add('blur')
        }
    }
    
    const close_booked = document.querySelector('.booked-spot-model-close');
    const close_vacant = document.querySelector('.vacant-spot-model-close');
    
    if (close_booked) {
        close_booked.addEventListener('click', () => {
            booked_model.style.display = 'none';
            page_1.classList.remove('blur');
        });
    }

    if (close_vacant) {
    close_vacant.addEventListener('click', () => {
        vacant_model.style.display = 'none';
        page_1.classList.remove('blur');
    });
    }

}



document.addEventListener('DOMContentLoaded', () => {
    toggleSpotDetails()
})