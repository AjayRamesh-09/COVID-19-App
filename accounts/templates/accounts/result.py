<!DOCTYPE html>
<html lang="en">

<head>
    {% load static%}
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Aarogya Setu|Result</title>
    <link rel="icon" href="https://upload.wikimedia.org/wikipedia/commons/4/41/Aarogya_Setu_App_Logo.png"
        type="image/x-icon">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link href="{% static 'open-iconic/font/css/open-iconic-bootstrap.css' %}" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link
        href="https://fonts.googleapis.com/css2?family=Encode+Sans+Semi+Condensed&family=Ubuntu+Condensed&display=swap"
        rel="stylesheet">
    <!-- Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" rel="stylesheet" />
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" rel="stylesheet" />
    <!-- MDB -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.5.0/mdb.min.css" rel="stylesheet" />
    <!-- MDB -->
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.5.0/mdb.min.js"></script>
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
    }

    .ad_footer_block {
        background-color: #005792;
        display: block;
    }

    .postion {
        position: absolute;
        bottom: -16px;
        left: 0;
        width: 100%;
    }
    #footer {
            position: fixed;
            padding: 10px 10px 0px 10px;
            bottom: 0;
            width: 100%;
            /* Height of the footer*/ 
            height:100px;
            background: grey;
        }
</style>

<body>
    <header>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="{% url 'home' %}">
                <img src="https://www.aarogyasetu.gov.in/wp-content/themes/setu/assets/images/aarogya_logo.png"
                    height=60 width=220 class="d-inline-block alighn-top" />
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
                aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav ml-auto">
                    <a class="nav-item nav-link" href="{% url 'statistics' %}">covid-19 STATISTICS</a>
                    <a class="nav-item nav-link" href="{% url 'vaccine' %}">VACCINATION</a>
                    <a class="nav-item nav-link" href="{% url 'covid' %}">covid-19 CHECKER</a>
                    {% if user.is_authenticated %}
                    <a class="nav-item nav-link" href="javascript:{document.getElementById('logout').submit()}"
                        onclick="">LOGOUT</a>
                    <form id="logout" method="POST" action="{% url 'logout' %}">
                        {% csrf_token %}
                        <input type="hidden" />
                    </form>
                    {% else %}
                    <a class="nav-item nav-link" href="{% url 'signup' %}">SIGN UP</a>
                    <a class="nav-item nav-link" href="{% url 'login' %}">LOGIN</a>
                    {% endif %}
                </div>
        </nav>
    </header>
    <center>
        <br>
        <h2 style="color:#03256c"><u><b>covid-19 PREDICTION</b></u></h2>
        <hr>
        <h5 style="color: #bb371a;padding-right: 2px;padding-left: 2px;"><b>{{ans}}</b></h5>
    </center>
    <hr>
</body>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
    integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
    crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
    integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
    crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
    integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
    crossorigin="anonymous"></script>
<footer class="bg-primary text-center text-white" id="footer">
    <!-- Grid container -->
    <div class="container p-4 pb-0">
        <!-- Section: Social media -->
        <section class="mb-4">
            <!-- Facebook -->
            <a href="https://www.facebook.com/AarogyaSetu/" class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                    class="fab fa-facebook-f"></i></a>

            <!-- Twitter -->
            <a href="https://twitter.com/SetuAarogya?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i class="fab fa-twitter"></i></a>

            <!-- Google -->
            <a href="https://www.mygov.in/aarogya-setu-app/" class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i class="fab fa-google"></i></a>
    
        </section>
        <!-- Section: Social media -->
    </div>

</footer>

</html>
