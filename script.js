// Функция для проверки пароля
function checkPassword() {
    const passwordInput = document.getElementById("password-input").value;
    const errorMessage = document.getElementById("error-message");

    if (passwordInput === "mil2025") {
        // Скрываем модальное окно
        document.getElementById("password-modal").style.display = "none";
        // Показываем калькулятор
        document.querySelector(".container").style.display = "block";
    } else {
        // Показываем сообщение об ошибке
        errorMessage.style.display = "block";
    }
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    // Скрываем калькулятор до ввода пароля
    document.querySelector(".container").style.display = "none";
    // Показываем модальное окно для ввода пароля
    document.getElementById("password-modal").style.display = "flex";
});

// Остальной JavaScript код калькулятора...
