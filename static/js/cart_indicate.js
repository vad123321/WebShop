$(document).ready(() =>{

    console.log('cart_indicate.js -> Start');

    let userId = $('#user-id').val();
    console.log('userId: ', userId);

    $.ajax({
        url: '/orders/ajax_cart_indicate',
        data: `uid=${userId}`,
        success: (response) => {
            $('#count').text(response.count);
            $('#_count').text(`Товарів у кошику: ${response.count}`);
            $('#_count').text(`Вартість: ${response.amount}`);
        }
    })
})