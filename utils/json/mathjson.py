import json, jsonpickle
from sympy import Basic, Matrix, srepr, sympify
from basicinput import *
from mathinput import *
from jxginput import *
from serializable import Serializable

class JSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (Basic, Matrix)):
            return {"py/object": "SymPy", 'srepr': srepr(obj)}
        if isinstance(obj, Serializable):
            dic = vars(obj)
            dic["py/object"] = obj.__class__.__name__
            #for k, v in dic.items():
            #    if isinstance(v, dict):
            #        dic[k] = self.default(v)
            return {key: self.default(value) for key, value in dic.items()}
        if isinstance(obj, dict):
            return {key: self.default(value) for key, value in obj.items()}
        return jsonpickle.Pickler(unpicklable=False).flatten(obj)

class JSONDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dic):
        if not isinstance(dic, dict):
            return dic
        if "py/object" in dic:
            classname = dic.pop("py/object")
            if classname == "SymPy":
                return sympify(dic['srepr'], evaluate=False)
            return globals()[classname](**{key: self.object_hook(value) for key, value in dic.items()})
        return {key: self.object_hook(value) for key, value in dic.items()}

