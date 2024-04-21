<!doctype html>
<html lang="en">

<head>
  {% load static %}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <title>Aarogya Setu</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <link href="{% static 'open-iconic/font/css/open-iconic-bootstrap.css' %}" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Encode+Sans+Semi+Condensed&family=Ubuntu+Condensed&display=swap"
    rel="stylesheet">
  <link rel="icon" href="https://upload.wikimedia.org/wikipedia/commons/4/41/Aarogya_Setu_App_Logo.png"
    type="image/x-icon">
</head>
<style>
  body {
    font-family: 'Encode Sans Semi Condensed', sans-serif;
    font-family: 'Ubuntu Condensed', sans-serif;
    font-size: 20px;
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
  }
</style>

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
          {% if user.is_authenticated %}
          <a class="nav-item nav-link" href="{% url 'covid' %}">covid-19 CHECKER</a>
          <a class="nav-item nav-link" href="javascript:{document.getElementById('logout').submit()}"
            onclick="">LOGOUT</a>
          <form id="logout" method="POST" action="{% url 'logout' %}">
            {% csrf_token %}
            <input type="hidden" />
          </form>
          {% else %}
          <a class="nav-item nav-link" href="{% url 'signup' %}">SIGN-UP/LOGIN</a>
          {% endif %}
        </div>
    </nav>
  </header>
  <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
    <ol class="carousel-indicators">
      <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
      <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
      <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
    </ol>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img class="d-block w-100"
          src="https://www.aarogyasetu.gov.in/wp-content/uploads/2021/04/mygov-10000000001946816780.jpg"
          alt="First slide">
      </div>
      <div class="carousel-item">
        <img class="d-block w-100"
          src="https://www.aarogyasetu.gov.in/wp-content/uploads/2021/04/mygov-10000000001865639792.jpg"
          alt="Second slide">
      </div>
      <div class="carousel-item">
        <img class="d-block w-100"
          src="https://www.aarogyasetu.gov.in/wp-content/uploads/2021/04/mygov-9999999992125415590.jpg"
          alt="Third slide">
      </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
  </div>
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
  <br>
  <footer class="text-muted">
    <div class="container text-center">
      <br>
      <p>HELPLINE NUMBER : +91-11-23978046</p>
      <p>TOLL FREE NUMBER: 1075</p>
      <h5><b>✅STAY HOME,STAY SAFE!!✅</b></h5>
    </div>
  </footer>
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

</html>
