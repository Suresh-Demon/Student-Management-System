  setTimeout(function() {
        let alert = document.getElementById('alert-box');
        if (alert) {
            alert.classList.remove('show');
            alert.classList.add('hide');
        }
    }, 3000);