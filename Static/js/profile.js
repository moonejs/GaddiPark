input=document.querySelectorAll('input')
edit_btn=document.querySelector('#edit_btn')
updt_btn=document.querySelector('#update_btn')
pas_div=document.querySelectorAll('.password')

edit_btn.addEventListener('click', ()=>{
    pas_div.forEach(e => {
        e.style.display='block'
    });
    input.forEach(e => {
        e.disabled = false;
    });
    updt_btn.style.display = 'block';
})

