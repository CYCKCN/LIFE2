from flask import Flask
from flask import Blueprint, request, redirect, render_template, url_for

staff = Blueprint('staff',__name__)