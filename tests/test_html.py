from all_relative import parsers

from .base_test import BaseTest


class TestHTML1(BaseTest):
    _classname = "ParseHTML"
    _ext = ".html"

    _input_template = """
{% extends 'base.html' %}
{% block title %}Test html 1{% endblock %}
{% block head %}
    <link href="/static/css/main.chunk.css" rel="stylesheet">
    <link rel="manifest" href="/manifest.json" />
{% endblock %}
    """

    _output_template = """
{% extends 'base.html' %}
{% block title %}Test html 1{% endblock %}
{% block head %}
    <link href="static/css/main.chunk.css" rel="stylesheet">
    <link rel="manifest" href="manifest.json" />
{% endblock %}
    """


class TestHTML2(BaseTest):
    _classname = "ParseHTML"
    _ext = ".html"

    _input_template = """
{% extends 'base.html' %}
{% block title %}Test html 2{% endblock %}
{% block body %}
    <script src="/static/js/file.chunk.js"></script>
    <script src="/static/js/main.123asd.chunk.js"></script>
{% endblock %}
    """

    _output_template = """
{% extends 'base.html' %}
{% block title %}Test html 2{% endblock %}
{% block body %}
    <script src="static/js/file.chunk.js"></script>
    <script src="static/js/main.123asd.chunk.js"></script>
{% endblock %}
    """
