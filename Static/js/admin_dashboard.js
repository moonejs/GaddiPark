function toggleParkingLotStatus() {
    add_parking_lot = document.querySelector('#add_parking_lot');
    add_parking_lot_model = document.querySelector('.add-parking-lot-modal');
    
    close_add_parking_lot_model = document.querySelectorAll('.close-add-parking-lot-modal');
    
    
    add_parking_lot.addEventListener('click', ()=> {
        
        add_parking_lot_model.style.display = 'block';

    })
    
    close_add_parking_lot_model.forEach(close =>{
        close.addEventListener('click', () => {
            add_parking_lot_model.style.display = 'none';
        })
    })
}

function toggleTimeFields() {
  const is24 = document.querySelector('input[name="is_24_hours"]:checked').value;
  const timeFields = document.querySelectorAll('#time-field');
    timeFields.forEach(field => {
        if (is24 === '1') {
        field.style.display = 'none';
        } else {
        field.style.display = 'block';
        }
    });
}


function toggleEditLot() {

    const close_edit_lot_model=document.querySelector('.close-edit-lot-model')
    const edit_lots_cards = document.querySelectorAll('.edit-lot');
   

    const edit_parking_lot = document.querySelector('.edit-parking-lot-modal');
   

    edit_lots_cards.forEach(card => {
        card.addEventListener('click', () => {
            
            edit_parking_lot.style.display = 'block';
            
        });
    });
    if (close_edit_lot_model) {
        close_edit_lot_model.addEventListener('click', () => {
            edit_parking_lot.style.display = 'none';
    });}


}










document.addEventListener('DOMContentLoaded', () => {
    toggleParkingLotStatus();
    toggleEditLot();
    const radios = document.querySelectorAll('input[name="is_24_hours"]');
    radios.forEach(radio => {
        radio.addEventListener('change', toggleTimeFields);
    });
})