<?php
$servername = "localhost";
$username = "root";
$password = "";

// 🔹 Conectar al servidor MySQL
$conn = new mysqli($servername, $username, $password);

// Verificar conexión
if ($conn->connect_error) {
  die("Error de conexión: " . $conn->connect_error);
}

// 🔹 Crear base de datos si no existe
$sql = "CREATE DATABASE IF NOT EXISTS uam_mante";
if ($conn->query($sql) === TRUE) {
  echo "✅ Base de datos 'uam_mante' lista.<br>";
} else {
  echo "❌ Error al crear la base de datos: " . $conn->error . "<br>";
}

// 🔹 Conectarse a la base de datos
$conn->select_db("uam_mante");

// 🔹 Crear tabla si no existe
$sql = "CREATE TABLE IF NOT EXISTS registros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(100) NOT NULL,
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";
if ($conn->query($sql) === TRUE) {
  echo "✅ Tabla 'registros' lista.<br>";
} else {
  echo "❌ Error al crear la tabla: " . $conn->error . "<br>";
}

$conn->close();

echo "<br>🎉 Todo listo. Ya puedes usar <b>guardar_registro.php</b> para guardar datos.";
?>
