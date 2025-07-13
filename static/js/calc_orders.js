function doCalculate() {
    console.log('doCalculate() -> Call')

    // 1
    let checkedCells = $('.check:checked');
    let totalPrice = 0.0;
    let selIdList = '';

    // 2
    for (let cell of checkedCells) {
        let parentRow = $(cell).parent().parent();
        totalPrice += parseFloat($(parentRow).find('td.price-cell').text());
        selIdList += $(parentRow).find('td.id-cell').text() + ',';
    }
    selIdList += totalPrice;

    // 3
    console.log(`totalPrice: ${totalPrice}`);
    console.log(`selIdList: ${selIdList}`);
    $('#total').text(`${totalPrice.toFixed(2)} usd`)
    $('#bill-btn').attr('href', `/orders/bill/${selIdList}`);
}


$(document).ready(() => {
    // 1
    console.log('calc_orders.js -> Start');
    doCalculate();

    // 2
    $('.check').click(() => {
        console.log('input.check -> Click');
        doCalculate();
    });

    // Видалення товару з кошика
    $('.del-btn').click(function() {
        let parentRow = $(this).closest('tr');
        let orderId = parentRow.find('input[type="hidden"]').val();

        $.ajax({
            url: '/orders/delete_order',
            type: 'POST',
            data: { id: orderId },
            headers: { 'X-CSRFToken': getCookie('csrftoken') },
            success: function(response) {
                if (response.success) {
                    parentRow.remove();
                    doCalculate();
                }
            }
        });
    });

    // Функція для отримання CSRF-токена
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
})
