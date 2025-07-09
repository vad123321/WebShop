$(document).ready(() => {
    // Check:
    console.log('cart.js -> Start');

    // Key Event:
    $('#gallery').on('click', '.add-to-cart-btn', (event) => {
        // 1
        console.log('add-btn -> Click');

        // 2
        let userId = $('#user-id').val();
        console.log('userId: ', userId);

        // 3
        if (userId == 'None') {
            alert('Для використання кошику Ви повинні авторизуватись');
        } else {
            //4
            // let productId = $(event.target).prev().val();
            let productId = $(event.target).closest('.add-to-cart').find('.product-id').val();
            console.log('productId: ', productId);

            //5
            // let productPrice = parseFloat($(event.target).parent().prev().find('h4').text());
            let productPrice = parseFloat($(event.target).closest('.add-to-cart').find('.product-price').val());
            console.log('productPrice: ', productPrice);

            // !!! AJAX - ЗАПИТ ДО СЕРВЕРА НА ЗБЕРЕЖЕННЯ ТОВАРУ У БД (ТАБЛИЦЯ КОШИКА):
            $.ajax({
                url: '/orders/ajax_cart',
                data: `uid=${userId}&pid=${productId}&price=${productPrice}`,
                success: (result) => {
                    console.log('AJAX -> OK');
                    console.log(result.message);
                    console.log('Check data:');
                    // ->
                    console.log('uid', result.uid);
                    console.log('pid', result.pid);
                    console.log('price', result.price);
                    // ->
                    $('#count').text(result.count);
                    $('#_count').text(`Товарів у кошику: ${result.count} шт`);
                    $('#_amount').text(`Вартість: ${result.amount} грн`);
                }
            });
        }
    });
});
