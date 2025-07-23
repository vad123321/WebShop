$(document).ready(() => {
    // 1 - Створюємо індикатори результатів валідації:
    let result1 = false;   // результат валідації логіна
    let result2 = false;   // результат валідації 1 пароля
    let result3 = false;   // результат валідації 2 пароля
    let result4 = false;   // результат валідації e-mail

    // 2 - Валідація поля логін:
    $('#username').blur(() => {
        let loginX = $('#username').val();
        let loginRe = /^[a-zA-Z][a-zA-Z0-9\_\-\.]{5,15}$/;
        if (loginRe.test(loginX)) {
            // Перевірка зайнятості логіна:
            $.ajax({
                url: '/accounts/ajaxreg',
                data: 'username=' + loginX,
                success: (result) => {
                    if (result.message === 'Логін - зайнятий!') {
                        $('#login-err').text('Введений логін вже існує!');
                        result1 = false;
                    } else {
                        $('#login-err').text('');
                        result1 = true;
                    }
                }
            });
        } else {
            $('#login-err').text('Помилка формату введення ...');
            result1 = false;
        }
    });
    // 3 - Валідація поля пароль:
    $('#pass1').blur(() => {
        let pass1X = $('#pass1').val();
        let passRe = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9\_\-\.]{8,}$/;
        if (passRe.test(pass1X)) {
            $('#pass1-err').text('');
            result2 = true;
        } else {
            $('#pass1-err').text('Помилка формату введення пароля ...');
            result2 = false;
        }
    });
    // 4 - Валідація поля повтор:
    $('#pass2').blur(() => {
        let pass1X = $('#pass1').val();
        let pass2X = $('#pass2').val();
        if (pass1X === pass2X) {
            $('#pass2-err').text('');
            result3 = true;
        } else {
            $('#pass2-err').text('Введені паролі не співпадають ...');
            result3 = false;
        }
    });
    // 5 - Валідація поля email:
    let emailRe = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;

    $('#email').blur(() => {
        let emailX = $('#email').val();
        if (emailRe.test(emailX)) {
            $('#email-err').text('');
            result4 = true;
        } else {
            $('#email-err').text('Некоректний email ...');
            result4 = false;
        }
    });
 
    // 6 - Підсумкова перевірка:
    $('#submit').click(() => {
        if (
            result1 === true &&
            result2 === true &&
            result3 === true &&
            result4 === true
        ) {
            $('#form1').attr('onsubmit', 'return true');
        } else {
            $('#form1').attr('onsubmit', 'return false');
            alert('Форма містить некоректні дані!\nВідправка даних заблокована!')
        }
    })
})