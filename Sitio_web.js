 function login() {
      const usuario = document.getElementById("usuario").value;
      const clave = document.getElementById("clave").value;
      const mensaje = document.getElementById("mensaje");

      if (usuario === "Admin" && clave === "ISC2025") {
        mensaje.style.color = "green";
        mensaje.textContent = "Inicio de sesión exitoso ✅";
      } else {
        mensaje.style.color = "red";
        mensaje.textContent = "Usuario o contraseña incorrectos ❌";
      }
    }