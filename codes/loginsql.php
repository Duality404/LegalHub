<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "radar";
print_r($_POST);
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO login (firstname, lastname, email,username,password)
VALUES ('$_POST[fname]','$_POST[lname]','$_POST[email]','$_POST[uname]','$_POST[pass]')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
  header("location:home.html");
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>