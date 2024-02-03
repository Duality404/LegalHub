
<link rel="stylesheet" href="./style.css">

</head>
<body>
<!-- partial:index.partial.html -->
<head>
  <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  </head>

<body>
<div id="form">
  <div class="container">
    <div class="col-lg-6 col-lg-offset-3 col-md-6 col-md-offset-3 col-md-8 col-md-offset-2">
      <div id="userform">
        <ul class="nav nav-tabs nav-justified" role="tablist">
          <li class="active"><a href="#signup"  role="tab" data-toggle="tab">Sign up</a></li>
          <li><a href="#login"  role="tab" data-toggle="tab">Log in</a></li>
        </ul>
        <div class="tab-content">
          <div class="tab-pane fade active in" id="signup">
            <h2 class="text-uppercase text-center"> Sign Up for Free</h2>
            <form id="signup" method="POST" action="loginsql.php">
              <div class="row">
                <div class="col-xs-12 col-sm-6">
                  <div class="form-group">
                    <label>First Name<span class="req">*</span> </label>
                    <input  class="form-control" type="text" id="fname" name="fname" required data-validation-required-message="Please enter your name." autocomplete="off">
                    <p class="help-block text-danger"></p>
                  </div>
                </div>
                <div class="col-xs-12 col-sm-6">
                  <div class="form-group">
                    <label> Last Name<span class="req">*</span> </label>
                    <input  class="form-control"  type="text" id="lname" name="lname" required data-validation-required-message="Please enter your name." autocomplete="off">
                    <p class="help-block text-danger"></p>
                  </div>
                </div>
              </div>
              <div class="form-group">
                <label> Your Email<span class="req">*</span> </label>
                <input  class="form-control" type="email" id="email" name="email" required data-validation-required-message="Please enter your email address." autocomplete="off">
                <p class="help-block text-danger"></p>
              </div>
              <div class="form-group">
                <label> Password<span class="req">*</span> </label>
                <input  class="form-control" type="password" id="pass" name="pass" required data-validation-required-message="Please enter your password" autocomplete="off">
                <p class="help-block text-danger"></p>
              </div>
              <div class="mrgn-30-top">
                <button type="submit" class="btn btn-larger btn-block"/>
                Sign up
                </button>
              </div>
            </form>
          </div>
          <div class="tab-pane fade in" id="login">
            <h2 class="text-uppercase text-center"> Log in</h2>
            <form id="signup" method="POST" action="index.php">
              <div class="form-group">
                <label> Your Email<span class="req">*</span> </label>
                <input  class="form-control" type="email" id="signemail" name="signemail" required data-validation-required-message="Please enter your email address." autocomplete="off">
                <p class="help-block text-danger"></p>
              </div>
              <div class="form-group">
                <label> Password<span class="req">*</span> </label>
                <input  class="form-control" type="password" id="signpass" name="signpass" required data-validation-required-message="Please enter your password" autocomplete="off">
                <p class="help-block text-danger"></p>
              </div>
              <div class="mrgn-30-top">
                <button type="submit" class="btn btn-larger btn-block"/>
                Log in
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /.container --> 
</div>
<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
</body>
<!-- partial -->
  <script  src="./script.js"></script>

</body>
</html>
<?php
    if (isset($_POST['signemail']) && isset($_POST['signpass'])) {
      // Replace these with your actual database connection details
      $servername = "localhost";
      $username = "root";
      $password = '';
      $dbname = "radar";

      // Create connection
      $conn = new mysqli($servername, $username, $password, $dbname);

      // Check connection
      if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
      }

      // Prepare and execute query
      $sql = "SELECT * FROM login WHERE email = ? ";
      $stmt = $conn->prepare($sql);
      $stmt->bind_param("s", $_POST['signemail']);
      $stmt->execute();
      $result = $stmt->get_result();

      // Check if user exists
      if ($result->num_rows === 1) {
        $user = $result->fetch_assoc();
        if (($_POST['signpass']==$user['password'])) {
          
          // Start session and store user data (replace with secure session management)
        //   session_start();
        //   $_SESSION['user_id'] = $user['id'];
        //   $_SESSION['email'] = $user['email'];
        ?>x

    <script>window.location="homeindex.html?id=$user[id]";</script>
    ?><?php
        } else {
          echo "<p>Invalid password.</p>";
        }
      } else {
        echo "<p>Invalid email.</p>";
      }

      // Close connection
      $conn->close();
    }
  ?>
