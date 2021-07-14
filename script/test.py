# -*- coding: utf-8 -*-

# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         print(name)
#         print(bases)
#         print(attrs)
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
#     def __init__(self, name, bases=None, dict=None):
#         super(ListMetaclass, self).__init__(name, bases, dict)
#
#     # def __call__(self, *args, **kwargs):
#     #     obj = self.__new__(self, *args, **kwargs)
#     #     self.__init__(obj, *args, **kwargs)
#
# class Mylist(list, metaclass=ListMetaclass):
#
#     def __init__(self, name):
#         self.name = name
#         print(type(self))
#
#     def __new__(cls, *args, **kwargs):
#         print(cls)
#         return list.__new__(cls, *args, **kwargs)
#
# mylist = Mylist("aaa")

# class Field(object):
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type
#
#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)
#
# class StringField(Field):
#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(100)')
#
# class IntegerField(Field):
#     def __init__(self, name):
#         super(IntegerField, self).__init__(name, 'bigint')
#
#
# class ModelMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         if name == 'Model':
#             return type.__new__(cls, name, bases, attrs)
#         print('Found model: %s' % name)
#         mappings = dict()
#         for k, v in attrs.items():
#             if isinstance(v, Field):
#                 print('Found mapping: %s ==> %s' % (k, v))
#                 mappings[k] = v
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__'] = mappings
#         attrs['__table__'] = name
#         return type.__new__(cls, name, bases, attrs)
#
# class Model(dict, metaclass=ModelMetaclass):
#     def __init__(self, **kw):
#         super(Model, self).__init__(**kw)
#
#     def __getattr__(self, item):
#         try:
#             return self[item]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % item)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append("?")
#             args.append(getattr(self, k, None))
#         sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
#         print(sql)
#         print('ARGS: %s' % str(args))
#
# class User(Model):
#     id = IntegerField('id')
#     name = StringField('name')
#     email = StringField('email')
#     password = StringField('password')
#
# u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# u.save()

# import asyncio
# import threading
# import time
# import requests
#
# async def hello():
#     print("hello world! (%s)" % threading.current_thread())
#     r = await asyncio.sleep(5)
#     print("hello again! (%s)" % threading.current_thread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()