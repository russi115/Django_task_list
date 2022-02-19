(function (){

    const btnEraser = document.querySelectorAll('btnEraser')

    btnEraser.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const validate = confirm('Are you sure you want to delete this task?')
            if (!validate) {
                e.preventDefault()
            }
        })
    });
})