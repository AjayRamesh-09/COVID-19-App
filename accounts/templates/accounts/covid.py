<!DOCTYPE html>
<html lang="en">

<head>
    {% load static%}
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Aarogya Setu|covid-19 Checker</title>
    <link rel="icon" href="https://upload.wikimedia.org/wikipedia/commons/4/41/Aarogya_Setu_App_Logo.png"
        type="image/x-icon">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link href="{% static 'open-iconic/font/css/open-iconic-bootstrap.css' %}" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link
        href="https://fonts.googleapis.com/css2?family=Encode+Sans+Semi+Condensed&family=Ubuntu+Condensed&display=swap"
        rel="stylesheet">
</head>
<style>
    body {
        font-family: 'Encode Sans Semi Condensed', sans-serif;
        font-family: 'Ubuntu Condensed', sans-serif;
        padding-left: 10px;
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
        bottom: -20px;
        left: 0;
        width: 100%;
    }

    .guide {
        width: 200px;
        border: 1px solid whitesmoke;
        box-shadow: blanchedalmond;
        padding: 50px;
        margin: 20px;
        border: 1px solid;
        padding: 10px;
        background-color: orange;


    }

    .container {
        width: 300px;
    }

    .guideform {
        width: 800px;
        border: 1px solid whitesmoke;
        box-shadow: blanchedalmond;
        padding: 50px;
        margin: 20px;
        border: 1px solid;
        padding: 10px;
        background-color: #da723c;

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
                    <a class="nav-item nav-link" href="{% url 'signup' %}">SIGN-UP/LOGIN</a>
                    {% endif %}
                </div>
        </nav>
    </header>
    <center>
        <div style="color:red;">
            <h1><u><b>covid-19 CHECKER</b></u></h1><br>
        </div>
        <div style="color:#03256c;">
            <h4><b><u>PLEASE FILL IN YOUR RESPONSE TO RECEIVE THE REPORT</u></b></h4>
        </div>

        <form action="{% url 'result' %}">
            {% csrf_token %}
            <div>
                <div class="form-group col-md-4">
                    <label for="inputState"><b>COUGH</b></label>
                    <div class="container">
                        <select id="inputState" class="form-control bg-white text-dark" name="cough">
                            <option selected>CHOOSE</option>
                            <option>YES</option>
                            <option>NO</option>
                        </select>
                    </div>
                    <br>
                </div>
                <div class="form-group col-md-4">
                    <label for="inputState"><b>FEVER</b></label>
                    <div class="container">
                        <select id="inputState" class="form-control bg-white text-dark" name="fever">
                            <option selected>CHOOSE</option>
                            <option>YES</option>
                            <option>NO</option>
                        </select>
                    </div>
                    <br>
                </div>

                <div class="form-group col-md-4">
                    <label for="inputState"><b>SORE THROAT</b></label>
                    <div class="container">
                        <select id="inputState" class="form-control bg-white text-dark" name="sore">
                            <option selected>CHOOSE</option>
                            <option>YES</option>
                            <option>NO</option>
                        </select>
                    </div>
                    <br>
                </div>

                <div class="form-group col-md-4">
                    <label for="inputState"><b>SHORTNESS OF BREATH</b></label>
                    <div class="container">
                        <select id="inputState" class="form-control bg-white text-dark" name="short">
                            <option selected>CHOOSE</option>
                            <option>YES</option>
                            <option>NO</option>
                        </select>
                    </div>
                    <br>
                </div>

                <div class="form-group col-md-4">
                    <label for="inputState"><b>HEADACHE</b></label>
                    <div class="container">
                        <select id="inputState" class="form-control bg-white text-dark" name="head">
                            <option selected>CHOOSE</option>
                            <option>YES</option>
                            <option>NO</option>
                        </select>
                    </div>
                    <br>
                </div>
            </div>

            <div style="color:#03256c;">
                <h4><b><u>TO RECIEVE A COPY OF THE RESULT,PLEASE ENTER THE PHONE NUMBER</u></b></h4>
            </div>
            <div class="form-group col-md-4">
                <label for="inputState"><b>PHONE NUMBER</b></label>
                <div class="container">
                    <input type="text" id="inputState" class="form-control bg-white text-dark" name="number">
                </div>
            </div>
            <input class="btn btn-primary" type="submit" value="CHECK NOW" />
            <br>
        </form>
    </center>
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
<hr>
<footer class="text-muted">
    <div class="container text-center">
        <p>TOLL FREE NUMBER: 1075</p>
        <h5><b>✅STAY HOME,STAY SAFE!!✅</b></h5>
    </div>
</footer>

</html>
