<!DOCTYPE html>
<html>
    <head>
        <title>Signup</title>
        <style>
            .heado {
                background-color: lightcyan;
                padding: 50px;
                border-radius: 10%;
            }
        </style>
    </head>
    <body>
        <div class="heado">
            <h1>Please signup</h1>
            <form method="post" action="signup.php" name="loginform">
                <label for="Username">Username:</label>
                <input type="text" name="Username" id="Username" required>
                <br>
                <label for="Password">Password:</label>
                <input type="password" name="Password" id="Password" required>
                <br>
                <input type="submit" name="Submit" id="submit" required>
                <br>
                <p>Already have an account? <a href="login.php">Login</a></p>

            </form>


        </div>


    </body>
</html>

<?php




$conn = new mysqli("127.0.0.1", "root", "root", "testing");

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else {
    echo "<script>" . "console.log('Connection Successfully!')</script>"; 
    
}



if (isset($_POST['Submit'])) {
    $password = $_POST["Password"];
    $options = ["cost" => 12,];
    $hashed_password = password_hash($password, PASSWORD_DEFAULT, $options);

    $stmt = mysqli_prepare($conn, "INSERT INTO User_Test (Username, Password) VALUES (?, ?)");
    mysqli_stmt_bind_param($stmt, "ss", $_POST['Username'], $hashed_password);
    mysqli_stmt_execute($stmt);


//     if ($un == "Username" && $pw == "Password") {
//         echo "test";
//         header("location:index.html");
//         exit();
//     } else {
//         echo "Invalid Username/Password";
//     }
}



?>