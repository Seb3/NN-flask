from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import InputForm
from app.nn import predict
import numpy as np

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    data = []
    y = []
    form = InputForm()
    if form.validate_on_submit():
	    
        density = form.density.data
        elastic_module = form.elastic_module.data
        n_stronger = form.n_stronger.data
        epoxy = form.epoxy.data
        t_flash = form.t_flash.data
        surface_density = form.surface_density.data
        feed = form.feed.data
        angle = form.angle.data
        step = form.step.data
        d_strip = form.d_strip.data
        
        data = [density, elastic_module, n_stronger, epoxy, t_flash, surface_density, feed, angle, step, d_strip]
        #data = np.asarray(data).astype(np.float32)
        y=predict(data)
        
    return render_template('login.html',  title='Приложение', form=form, data=data, y=y)


