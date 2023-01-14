<?php
session_start();


if (isset($_POST['submit'])) {
    $Username = $_POST['Username'];
    $Password = $_POST['Password'];

    // Koble til database

    $conn = new mysqli("127.0.0.1", "root", "root", "testing");

    // Få bruker fra database
    $stmt = mysqli_prepare($conn, "SELECT * FROM User_Test WHERE Username=?");
    mysqli_stmt_bind_param($stmt, "s", $Username);
    mysqli_stmt_execute($stmt); // Kan forhindre SQL injector

    $result = mysqli_stmt_get_result($stmt);
    $row = mysqli_fetch_array($result);
    $hashed_password = $row['Password'];

    if (password_verify($Password, $hashed_password)) {
        $_SESSION['Username'] = $Username;
        echo "<h1>Logged in as " . $Username . "</h1>";
        echo "<a href='login.php'>Log Out</a>";
    } else {
        $_SESSION['error'] = "Invalid login credentials";
        header("location: failedLog.php");
    }
}

?>
