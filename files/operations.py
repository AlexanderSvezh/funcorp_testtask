from flask import abort


def action(obj, calc):
    if not obj:
        abort(404)
    arg1, arg2 = obj['x'], obj['y']
    if "sum" in calc:
        res = int(arg1)+int(arg2)
    elif "sub" in calc:
        res = int(arg1)-int(arg2)
    elif "mul" in calc:
        res = int(arg1)*int(arg2)
    elif "div" in calc:
        res = int(arg1)*int(arg2)
    else:
        raise Exception('fail calc')
    return res