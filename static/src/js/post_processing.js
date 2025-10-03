document.getElementById('pay_btn').addEventListener('click', function() {
    var codForm = document.querySelector('form[action*="/payment/status"]');
    if (codForm) {
        codForm.submit();
    }
});