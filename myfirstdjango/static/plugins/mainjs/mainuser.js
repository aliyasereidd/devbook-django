
function togglePasswordVisibility() {
    const passwordInput = document.getElementById("password");
    const passwordToggle = document.querySelector(".password-toggle");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        passwordToggle.textContent = "🙈"; // رمز إخفاء
    } else {
        passwordInput.type = "password";
        passwordToggle.textContent = "👁️"; // رمز إظهار
    }
}
s
document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // منع الإرسال التلقائي

    // إعادة تعيين رسائل الخطأ
    document.getElementById("username-error").textContent = "";
    document.getElementById("password-error").textContent = "";

    // جلب القيم من الحقول
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    let isValid = true;

    if (!username) {
        document.getElementById("username-error").textContent = "الرجاء إدخال اسم المستخدم أو البريد الإلكتروني";
        isValid = false;
    }

    if (!password) {
        document.getElementById("password-error").textContent = "الرجاء إدخال كلمة المرور";
        isValid = false;
    }

    if (isValid) {
        fetch("{% url 'login' %}", {  // تأكد أن 'login' هو اسم المسار في `urls.py`
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({ username: username, password: password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = "{% url 'index' %}"; // توجيه المستخدم للصفحة الرئيسية
            } else {
                document.getElementById("password-error").textContent = "❌ اسم المستخدم أو كلمة المرور غير صحيحة";
            }
        })
        .catch(error => console.error("خطأ:", error));
    }
});

// وظيفة للحصول على CSRF Token من الكوكيز
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
