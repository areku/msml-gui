__author__ = 'weigl'

from jinja2 import Environment, PackageLoader
from functools import partial


def render_template(tpl_name, **kwargs):
    return jinja_env.get_template(tpl_name).render(**kwargs)


jinja_env = Environment(loader=PackageLoader("msmlgui.help"))


tpl_operator_help = partial(render_template, "operator_help.html")
tpl_task_shape = partial(render_template, "task_shape.html")
tpl_scene_shape = partial(render_template, "scene_shape.html")
tpl_scene_help = partial(render_template, "scene_help.html")
tpl_attribute_help =  partial(render_template, "attribute_help.html")
tpl_variable_help = partial(render_template, "var_help.html")
tpl_variable_shape = partial(render_template, "var_shape.html")