"""Домашнее задание по теме 'Интроспекция'"""
import inspect


def module_funct(*args, **kwargs):        # проверочная функция
    pass


def introspection_info(obj):
    if not isinstance(obj, (int, float, str, tuple, list, dict, set)):
        name_object = obj.__name__
    else:
        name_object = 'нет'
    object_type = type(obj)
    attr_object = [attr_name for attr_name in dir(obj) if not callable(getattr(obj, attr_name))]
    object_methods = [attr_name for attr_name in dir(obj) if callable(getattr(obj, attr_name))]
    object_module = inspect.getmodule(obj)
    object_id = id(obj)
    information_about_object = (f'имя объекта: {name_object}\n'
                                f'тип объекта: {object_type}\n'
                                f'аттрибуты объекта:\n'
                                f'{attr_object}\n'
                                f'методы объекта:\n'
                                f'{object_methods}\n'
                                f'модуль, к которому объект принадлежит:  {object_module}\n'
                                f'идентификатор объекта:  {object_id}\n')
    return information_about_object


if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)

    number_info = introspection_info(module_funct)
    print(number_info)
