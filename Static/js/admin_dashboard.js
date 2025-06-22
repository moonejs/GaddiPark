function toggleParkingLotStatus() {
    add_parking_lot = document.querySelector('#add_parking_lot');
    add_parking_lot_model = document.querySelector('.add-parking-lot-model');
    page_1= document.querySelector('.page-1');
    close_add_parking_lot_model = document.querySelector('.close-add-parking-lot-model');
    
    
    add_parking_lot.addEventListener('click', ()=> {
        add_parking_lot_model.style.display = 'block';
        page_1.classList.add('blur');
    })
    
    close_add_parking_lot_model.addEventListener('click', ()=> {
        add_parking_lot_model.style.display = 'none';
        page_1.classList.remove('blur');
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

document.addEventListener('DOMContentLoaded', () => {
    toggleParkingLotStatus();
    
    const radios = document.querySelectorAll('input[name="is_24_hours"]');
    radios.forEach(radio => {
        radio.addEventListener('change', toggleTimeFields);
    });
})