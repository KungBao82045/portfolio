<!DOCTYPE html>
<html>
    <head>
        <title>Login</title>
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
            <h1>Please login</h1>
            <form method="post" action="logged.php">
            <label for="Username">Username:</label>
            <input type="text" name="Username" required>
            <br>
            <label for="Password">Password:</label>
            <input type="Password" name="Password" required>
            <p style="color: red;">Invalid username or password</p>
            <input type="submit" name="submit" value="Login">
            <p>Dont have an account? <a href="signup.php">signup</a></p>
            </form>
        </div>

    </body>
</html>
