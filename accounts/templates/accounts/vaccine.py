<!doctype html>
<html lang="en">

<head>
  {% load static %}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <title>Aarogya Setu|Vaccination</title>
  <link rel="icon" href="https://upload.wikimedia.org/wikipedia/commons/4/41/Aarogya_Setu_App_Logo.png"
    type="image/x-icon">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <link href="{% static 'open-iconic/font/css/open-iconic-bootstrap.css' %}" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Encode+Sans+Semi+Condensed&family=Ubuntu+Condensed&display=swap"
    rel="stylesheet">
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link
    href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300&family=Roboto+Condensed:wght@300&family=Roboto:wght@100&display=swap"
    rel="stylesheet">
</head>
<style>
  body {
    font-family: 'Encode Sans Semi Condensed', sans-serif;
    font-family: 'Ubuntu Condensed', sans-serif;
    padding-left: 3px;
    font-size: 20px;
  }

  .ubuntu {
    font-family: 'Encode Sans Semi Condensed', sans-serif;
    font-family: 'Ubuntu Condensed', sans-serif;
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
  }

  .font {
    font-family: 'Noto Sans JP', sans-serif;
    font-family: 'Roboto', sans-serif;
    font-family: 'Roboto Condensed', sans-serif;
    font-size: 16px;
    padding-left: 5px;
    padding-right: 5px;
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
  <center>
    <h1 style="color: #03256c;"><u><b>ABOUT VACCINATION</b></u></h1>
  </center>
  <div class="font">
    <p><b>
        A covid‑19 Vaccine Is A Vaccine Intended To Provide Acquired Immunity Against Severe Acute Respiratory Syndrome
        CORONA VIRUS 2 (SARS‑CoV‑2), The Virus Causing CORONA VIRUS Disease 2019 (covid‑19).In Phase III Trials, Several
        covid‑19 Vaccines Have Demonstrated Efficacy As High As 95% In Preventing Symptomatic covid‑19 Infections. As Of
        April 2021, 16 Vaccines Are Authorized By At Least One National Regulatory Authority For Public Use: Two RNA
        Vaccines (Pfizer–BioNTech And Moderna), Seven Conventional Inactivated Vaccines (BBIBP-CorV, CoronaVac, Covaxin,
        WIBP-CorV, CoviVac, Minhai-Kangtai and QazVac), Five Viral Vector Vaccines (Sputnik Light, Sputnik V,
        Oxford–AstraZeneca, Convidecia, and Johnson & Johnson), And Two Protein Subunit Vaccines (EpiVacCorona and
        RBD-Dimer).In Total, As Of March 2021, 308 Vaccine Candidates Are In Various Stages Of Development, With 73 In
        Clinical Research, Including 24 In Phase I Trials, 33 In Phase I–II Trials, And 16 In Phase III Development.
      </b>
    </p>
  </div>
  <center>
    <h4 style="color: #03256c;"><u><b>TO KNOW MORE ABOUT VACCINATION,CLICK HERE</b></u></h4>
    <a href="https://www.cowin.gov.in/faq"><button class="btn btn-primary">CLICK HERE</button></a>
  </center>
  <script>
    //https://api.covid19api.com/summary

    async function getcovidApi() {
      const jsonFormatData = await fetch('https://api.covid19india.org/data.json');
      const jsFormatData = await jsonFormatData.json();

      const d = jsFormatData.tested.length - 1;
      document.getElementById("g1").innerHTML = jsFormatData.tested[d].totaldosesadministered;
      document.getElementById("g2").innerHTML = jsFormatData.tested[d].firstdoseadministered;
      document.getElementById("g3").innerHTML = jsFormatData.tested[d].seconddoseadministered;
      document.getElementById("g4").innerHTML = jsFormatData.tested[d].updatetimestamp;

    }
    getcovidApi();
  </script>
  <div align="center">
    <hr>
    <h1 style="color: red;"><b>VACCINATION STATUS</b></h1>
    <hr>
    <div class="ubuntu">
      <table class="table-responsive-sm">
        <thead>
          <tr style="background-color:#ff8303;">
            <th style="padding: 10px">TOTAL VACCINATION DOSES</th>
            <th style="padding:10px">DOSE 1 VACCINATION</th>
            <th style="padding:10px">DOSE 2 VACCINATION</th>
            <th style="padding:10px">LAST UPDATED</th>
          </tr>
        </thead>
        <tbody>

          <tr>
            <td style="padding:10px">
              <p id="g1"> </p>
            </td>
            <td style="padding:10px">
              <p id="g2"> </p>
            </td>
            <td style="padding:10px">
              <p id="g3"> </p>
            </td>
            <td style="padding:10px">
              <p id="g4"> </p>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <br>
    <a href="javascript:location.reload(true)"><button class="btn btn-primary">REFRESH PAGE</button></a>
  </div>
  <hr>
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
<footer class="text-muted">
  <div class="container text-center">
    <br>
    <p>HELPLINE NUMBER : +91-11-23978046</p>
    <p>TOLL FREE NUMBER: 1075</p>
    <h5><b>✅STAY HOME,STAY SAFE!!✅</b></h5>
  </div>
</footer>

</html>
