from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField



class InputForm(FlaskForm):
    density = FloatField('Плотность, кг/м3')
    elastic_module = FloatField('Модуль упругости, ГПа')
    n_stronger = FloatField('Количество отвердителя, м.%')
    epoxy = FloatField('Содержание эпоксидных групп,%_2')
    t_flash = FloatField('Температура вспышки, С_2')
    surface_density = FloatField('Поверхностная плотность, г/м2')
    feed = FloatField('Потребление смолы, г/м2')
    angle = FloatField('Угол нашивки, град')
    step = FloatField('Шаг нашивки')
    d_strip = FloatField('Плотность нашивки')
    submit = SubmitField('Подобрать параметр')
