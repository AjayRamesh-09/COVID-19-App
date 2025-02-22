<!doctype html>
<html lang="en">

<head>
  {% load static %}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <title>Aarogya Setu|Login</title>
  <link rel="icon" href="https://upload.wikimedia.org/wikipedia/commons/4/41/Aarogya_Setu_App_Logo.png"
    type="image/x-icon">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <link href="{% static 'open-iconic/font/css/open-iconic-bootstrap.css' %}" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Encode+Sans+Semi+Condensed&family=Ubuntu+Condensed&display=swap"
    rel="stylesheet">
</head>
<style>
  body {
    font-family: 'Encode Sans Semi Condensed', sans-serif;
    font-family: 'Ubuntu Condensed', sans-serif;
    font-size: 20px;
  }

  .form {
    padding-left: 20px;
  }

  #design {
    background-color: black;
    border: none;
    color: white;
    padding: 8px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 12px;
    font-family: 'Ubuntu', sans-serif;
    border-radius: 25px;
  }


  .ad_footer_block {
    background-color: #005792;
  }

  .postion {
    position: absolute;
    bottom: 0px;
    left: 0;
    width: 100%;
  }

  /* Style all input fields */
  input {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 6px;
    margin-bottom: 16px;
  }

  /* Style the submit button */
  input[type=submit] {
    background-color: #04AA6D;
    color: white;
  }

  /* The message box is shown when the user clicks on the password field */
  #message {
    display: none;
    background: #f1f1f1;
    color: #000;
    position: relative;
    padding: 20px;
    margin-top: 10px;
  }

  #message p {
    padding: 10px 35px;
    font-size: 18px;
  }

  /* Add a green text color and a checkmark when the requirements are right */
  .valid {
    color: green;
  }

  .valid:before {
    position: relative;
    left: -35px;
    content: "✔";
  }

  /* Add a red text color and an "x" when the requirements are wrong */
  .invalid {
    color: red;
  }

  .invalid:before {
    position: relative;
    left: -35px;
    content: "✖";
  }

  .container {
    width: 320px;
  }

  .con {
    width: 170px;
  }
</style>
<script>
  function myFunction() {
    var x = document.getElementById("psw");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }
</script>

<body>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="{% url 'home' %}">
        <img src="https://www.aarogyasetu.gov.in/wp-content/themes/setu/assets/images/aarogya_logo.png" height=60
          width=220 class="d-inline-block alighn-top" />
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav ml-auto">
          <a class="nav-item nav-link" href="{% url 'statistics' %}">covid-19 STATISTICS</a>
          <a class="nav-item nav-link" href="{% url 'vaccine' %}">VACCINATION</a>
          <a class="nav-item nav-link" href="{% url 'signup' %}">SIGN-UP/LOGIN</a>
        </div>
    </nav>
  </header>
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
    integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
    crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
    integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
    crossorigin="anonymous"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
    integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
    crossorigin="anonymous"></script>
</body>
<br>
<div class="form">
  {% block content %}
  {% if error %}
  <center>
    <h5 style="color:#fa1e0e;border-radius: 20px;
    padding: 10px 10px;
    margin: 10px auto;
    background-color:#eec4c4;
    width:40%;"><b>{{ error }}</b></h5>
  </center>
  {% endif %}
  <br>
  <center>
    <h4 style="color: #03256c;"><b><u>LOGIN FOR STATUS CHECK</u></b></h4>

    <div class="container">
      <form method="POST" action="{% url 'login' %}">
        {% csrf_token %}
        <label for="usrname">USERNAME</label>
        <input class="bg-white text-dark" type="text" id="usrname" name="username" required>

        <label for="psw">PASSWORD</label>
        <input class="bg-white text-dark" type="password" id="psw" name="password"
          pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
          title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"
          required>
        <div class="con">
          <input type="button" class="btn btn-warning" onclick="myFunction()" value="SHOW PASSWORD">
        </div>
        <button type="submit" class="btn btn-primary">LOGIN</button>
      </form>
    </div>
    <br>
    <div class="text-center">
      <h7><b>NOT REGISTERED YET<br><a href="{% url 'signup' %}">CLICK HERE</a></b></h7>
    </div>
  </center>

</div>
<hr>
<center>
  <div>
    <footer class="text-muted">
      <div class="container text-center">
        <p>TOLL FREE NUMBER: 1075</p>
        <h5><b>✅STAY HOME,STAY SAFE!!✅</b></h5>
      </div>
    </footer>
</center>
</div>
{% endblock %}
