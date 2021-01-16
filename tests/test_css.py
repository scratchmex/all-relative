from all_relative import parsers

from .base_test import BaseTest


class TestCSS1(BaseTest):
    _classname = "ParseCSS"
    _ext = ".html"

    _input_template = """
{% extends 'base.html' %}
{% block title %}Test css 1{% endblock %}
{% block body %}
    <style>
        body {
            background-image: url("/some/dir/paper.gif");
            background-color: #cccccc;
        }
    </style>
{% endblock %}
    """

    _output_template = """
{% extends 'base.html' %}
{% block title %}Test css 1{% endblock %}
{% block body %}
    <style>
        body {
            background-image: url("some/dir/paper.gif");
            background-color: #cccccc;
        }
    </style>
{% endblock %}
    """


class TestCSS2(BaseTest):
    _classname = "ParseCSS"
    _ext = ".css"

    _input_template = """
body {
    background-image: url("/some/dir/paper.gif");
    background-color: #cccccc;
}
    """

    _output_template = """
body {
    background-image: url("some/dir/paper.gif");
    background-color: #cccccc;
}
    """
