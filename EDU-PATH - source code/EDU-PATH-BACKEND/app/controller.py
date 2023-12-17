from operator import truediv
from re import template
from app import app, bcrypt
from flask import render_template, request, redirect, url_for, session, flash
from sqlalchemy import func
from .database import db
from datetime import date
from flask import session
from .model import *


@app.route('/')
def index():
  return 'Hello from Flask!'
