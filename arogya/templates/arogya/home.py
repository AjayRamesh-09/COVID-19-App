{% extends 'base.html' %}

{% block content %}

<br>
<div class="row featurette">
    <div class="col-md-7">
        <h2 class="featurette-heading" style="color:#03256c;"><b><u>covid-19 SELF CHECKER</u></b></h2>
        <h5 class="lead" style="font-size:18px;font-weight: bold;">AN ONLINE, MOBILE-FRIENDLY TOOL WHICH ASKS FOR A SERIES OF QUESTIONS,AND BASED ON THE USER'S RESPONSE,IT PROVIDES THE RECOMMENDED ACTIONS AND RESOURCES.</h5>
        {% if user.is_authenticated %}
        {% if request.user.is_superuser %}
        <a class="nav-link" href="{% url 'login' %}"><button type="button" class="btn btn-primary btn-md">CLICK HERE
            >></button></a><br><br>
            {% else %}
            <a href="{% url 'covid' %}"><button type="button" class="btn btn-primary btn-md">CLICK HERE >></button></a><br><br>
            {% endif %}

            {% else %}
            <a href="{% url 'login' %}"><button type="button" class="btn btn-primary btn-md">CLICK HERE >></button></a><br><br>
            {% endif %}

        </div>
        <div class="col-md-5">
            <img src="https://media.giphy.com/media/U6pedZ9GkONjU2xCHl/giphy.gif" height="400" width="400" alt="" class="img-fluid"><br><br>
        </div>
    </div>

    <hr class="featurette-divider">

    <div class="row featurette">
        <div class="col-md-7 order-md-2">
            <h2 class="featurette-heading" style="color:#03256c;"><b><u>BED AVAILABILITY</u></b></h2>
            <h5 class="featurette-heading" style="font-size: 18px;"><b>TO KNOW ABOUT THE BED AVAILABILITY,CLICK ON THE LINK BELOW.</b></h5>
            <a href="https://tncovidbeds.tnega.org/"><button type="button" class="btn btn-primary btn-md">CLICK HERE
                >></button></a>
            </div>
            <div class="col-md-5 order-md-1">
                <img src="https://media.giphy.com/media/RIw6pFIuEljc94U4u2/giphy.gif" height="400" width="400" alt="" class="img-fluid">
            </div>
        </div>

    </div>



    {% endblock %}
