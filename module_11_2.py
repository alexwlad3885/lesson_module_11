"""Домашнее задание по теме 'Интроспекция'"""
import inspect


def module_funct(*args, **kwargs):        # проверочная функция
    pass


def introspection_info(obj):
    if not isinstance(obj, (int, float, str, tuple, list, dict, set)):
        print(f'\nимя объекта:   {obj.__name__}')
    else:
        print(f'\n')
    print(f'тип объекта:   {type(obj)}')
    print(f'аттрибуты объекта:')
    print([attr_name for attr_name in dir(obj) if not callable(getattr(obj, attr_name))])
    print(f'методы объекта:')
    print([attr_name for attr_name in dir(obj) if callable(getattr(obj, attr_name))])
    print(f'модуль, к которому объект принадлежит:  {inspect.getmodule(obj)}')
    print(f'идентификатор объекта:  {id(obj)}')


if __name__ == '__main__':

    introspection_info(module_funct)

    a = 42
    introspection_info(a)
