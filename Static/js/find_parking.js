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
    is_ev=selected_option.getAttribute('data-is-ev')==1
}


document.addEventListener('DOMContentLoaded',()=>{
    toggleBookSpot()
})