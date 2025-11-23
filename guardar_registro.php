<?php
// Conexión con MySQL
$servername = "localhost";
$username = "root"; 
$password = ""; 
$dbname = "mapa_uam_mante"; // debe coincidir con el que pusiste en setup_db.php

$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
  die("Error de conexión: " . $conn->connect_error);
}

// Recibir los datos del formulario
$nombre = $_POST['nombre'];
$correo = $_POST['correo'];
$tipo_usuario = $_POST['tipo_usuario'];

// Insertar en la base de datos
$sql = "INSERT INTO registros (nombre, correo, tipo_usuario)
        VALUES ('$nombre', '$correo', '$tipo_usuario')";

if ($conn->query($sql) === TRUE) {
  echo "✅ Registro guardado correctamente.";
} else {
  echo "❌ Error: " . $conn->error;
}

$conn->close();
?>
