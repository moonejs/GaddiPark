function toggleSpotDetails(){
    const booked_model=document.querySelector('.booked-spot-model')
    const vacant_model = document.querySelector('.vacant-spot-model');
    const page_container=document.querySelector('.page-container')

    let has_spot = false;
    let is_booked = false;


    has_spot = page_container.dataset.hasSpot === "true";
    is_booked = page_container.dataset.isBooked === "true";

    if (has_spot){
        if (is_booked){
            booked_model.style.display='block'

        }else{
            vacant_model.style.display='block'
        }
    }
    
    const close_booked = document.querySelector('.booked-spot-model-close');
    const close_vacant = document.querySelector('.vacant-spot-model-close');
    
    if (close_booked) {
        close_booked.addEventListener('click', () => {
            booked_model.style.display = 'none';
        });
    }

    if (close_vacant) {
    close_vacant.addEventListener('click', () => {
        vacant_model.style.display = 'none';
    });
    }

}



document.addEventListener('DOMContentLoaded', () => {
    toggleSpotDetails()
})