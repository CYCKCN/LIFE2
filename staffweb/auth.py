from flask import Flask
from flask import Blueprint, request, redirect, render_template, url_for

auth = Blueprint('auth',__name__)