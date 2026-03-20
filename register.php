<?php 
error_reporting(E_ALL);
ini_set('display_errors', 1);

    if($_SERVER["REQUEST_METHOD"] == "POST") {
        $usuario = trim($_POST['usuario']??'');
        $email = trim($_POST['email']??'');
        $contrasenia = $_POST['contrasenia'];
        //validar
        if(empty($usuario) || empty($email) || empty($contrasenia)) {
            die("Por favor, complete todos los campos.");
        }
        $conn= new mysqli("localhost", "root", "", "pag_libros");
        if($conn->connect_error) {
            die("Conexión fallida: " . $conn->connect_error);
        }
        $password_hash = password_hash($contrasenia, PASSWORD_DEFAULT);
        $sql = "INSERT INTO usuarios (usuario, correo, contrasena) VALUES (?,?,?)";
        $stmt = $conn->prepare($sql);
        if(!$stmt) {
            die("Error en la preparación de la consulta: " . $conn->error);
        }
        $stmt->bind_param("sss", $usuario, $email, $password_hash);

        if($stmt ->execute()) {
            echo "Registro exitoso. Bienvenido, " . htmlspecialchars($usuario) . "!";
            header("Location: Html/generos.html");
            exit();
        } else {
            echo "Error: " . $stmt->error; 
        }
        $stmt->close();
        $conn->close();
    }
    else {
        die("Método no permitido.");
    }
?>