try:
    import simplejson as __json__
except:
    #default to basic json library
    import json as __json__

import os
import codecs
import uuid
import random
import hashlib
import time
import datetime
import dateutil.parser
from datetime import date
import base64 as __b64__
from os.path import expanduser
from decimal import Decimal
from wrapper import Wrapper


def extract_ip_address(request):
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    except:
        return None


def wrap(**kwd):
    return Wrapper.create(**kwd)


def curry(f, *a, **kw):
    def curried(*more_a, **more_kw):
        return f(*(a + more_a), **dict(kw, **more_kw))
    return curried


def rename(tbl, current_name, new_name):
    """Rename a property in a dictionary"""
    try:
        tbl[new_name] = tbl[current_name]
        tbl.pop(current_name)
    except KeyError:
        pass

def json(obj, indent=None, sort_keys=True, pretty=False):
    """Convert the object instance into a json blob."""
    assert obj is not None, "The input parameter is null!"

    try:
        if indent:
            return __json__.dumps(obj, check_circular=False, sort_keys=sort_keys, indent=indent)
        else:
            if pretty is True:
                return __json__.dumps(obj, check_circular=False, sort_keys=sort_keys, indent=2)
            return __json__.dumps(obj, check_circular=False, sort_keys=sort_keys)
    except Exception, ex:
        def fixer(o):
            if isinstance(o, dict) is True:
                for key in o:
                    val = o[key]
                    if hasattr(val, '__call__'):
                        o[key] = "function()"
                        continue
                    if isinstance(val, datetime.datetime):
                        val = val.strftime("%Y-%m-%d %H:%M:%S")
                        o[key] = val
                    elif isinstance(val, datetime.date):
                        val = val.strftime("%Y-%m-%d")
                        o[key] = val
                    elif isinstance(val, (dict, list)):
                        o[key] = fixer(val)
                    elif isinstance(val, Decimal):
                        val = float(str(val))
                        o[key] = val
            elif isinstance(o, list) is True:
                for x, val in enumerate(o):
                    if hasattr(val, '__call__'):
                        o[x] = "function()"
                        continue
                    if isinstance(val, datetime.datetime):
                        val = val.strftime("%Y-%m-%d %H:%M:%S")
                        o[x] = val
                    elif isinstance(val, datetime.date):
                        val = val.strftime("%Y-%m-%d")
                        o[x] = val
                    elif isinstance(val, Decimal):
                        val = float(str(val))
                        o[x] = val
                    elif isinstance(val, dict):
                        val = fixer(val)
                        o[x] = val
                    elif isinstance(val, list):
                        val = fixer(val)
                        o[x] = val
            return o

        def deep_copy(o):
            if isinstance(o, list):
                copy = []
                for x, val in enumerate(o):
                    if isinstance(val, (list, dict)) is True:
                        val = deep_copy(val)
                        copy.append(val)
                return copy
            elif isinstance(o, dict):
                copy = {}
                for key in o:
                    val = o[key]
                    copy[key] = val
                    if isinstance(val, (list, dict)) is True:
                        val = deep_copy(val)
                        copy[key] = val
                return copy
            return o

        try:
            copy = deep_copy(obj)
            fixer(copy)
            if indent:
                return __json__.dumps(copy, check_circular=False, sort_keys=sort_keys, indent=indent)
            else:
                if pretty is True:
                    return __json__.dumps(copy, check_circular=False, sort_keys=sort_keys, indent=2)
                return __json__.dumps(copy, check_circular=False, sort_keys=sort_keys)
        except Exception, e:
            print e.message

        message = "Unable to encode the object to json-> %s" % ex.message
        raise Exception(message)


def unjson(data, silent=False):
    """Convert the json blob into an object instance."""
    assert data is not None, "The input parameter is null!"

    if silent is True:
        try:
            txt = data.strip()
            pfx, sfx = txt[0], txt[len(txt) - 1]
            if pfx == "[" and sfx == "]" or pfx == "{" and sfx == "}":
                try:
                    return __json__.loads(data, strict=False)
                except:
                    return None
            return None
        except:
            return None

    try:
        return __json__.loads(data, strict=False)
    except Exception, ex:
        message = "Unable to decode the json object-> %s" % ex.message
        raise Exception(message)



def timestamp():
    """Return a datetime instance representing the current date/time"""
    dt = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return dt


def now():
    """Return a datetime instance"""
    return datetime.datetime.utcnow()


def parse_date(txt):
    """Parse the date string"""
    if isinstance(txt, int):
        txt = time.ctime(txt)
        txt = txt.split("-")[0]

    try:
        return dateutil.parser.parse(txt)
    except Exception, ex:
        if isinstance(txt, (datetime.datetime, datetime.date)):
            return txt
        raise Exception("Invalid date format-> '%s' could not be parsed.\n%s" % (txt, ex.message))


def format_date(dt, *fmt):
    """Parse the date string"""
    fmt = "" if len(fmt) == 0 else fmt[0]

    try:
        dt = dateutil.parser.parse(dt)
    except:
        pass

    try:
        return dt.strftime(fmt)
    except Exception, ex:
        raise Exception("Invalid date format-> '%s' could not be parsed.\n%s" % (str(dt), ex.message))




def stringify(o, pretty=False):
    """Convert the specified object to a string. If the input object
     is a list type convert each object in the list to a string and return."""
    if o is None:
        return ""
    elif isinstance(o, basestring):
        return o
    if isinstance(o, datetime):
        return o.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(o, date):
        return o.strftime("%Y-%m-%d")

    try:
        if isinstance(o, list):
            if len(o) == 0:
                return "[]"

            if isinstance(o[0], (int, basestring, long, float)) is True:
                if isinstance(o[0], int) is True:
                    try:
                        return ",".join([str(k) for k in o])
                    except:
                        return ",".join([str(k) for k in o if k is not None])
                if isinstance(o[0], basestring) is True:
                    return "\n".join(o)

                try:
                    try:
                        if pretty is True:
                            return "[%s]" % ",".join([str(k) for k in o])
                        return ",".join([str(k) for k in o])
                    except:
                        if pretty is True:
                            return "[%s]" % ",".join([str(k) for k in o if k is not None])
                        return ",".join([str(k) for k in o if k is not None])

                except:
                    if pretty is True:
                        return "[%s]" % ",".join([str(k) for k in o if k is not None])
                    return ",".join([str(k) for k in o if k is not None])

            if pretty is True:
                return json(o, indent=3)
            return json(o)

        if isinstance(o, dict):
            if pretty is True:
                return json(o, indent=3)
            return json(o)
        elif hasattr(o, "__dict__"):
            if pretty is True:
                return json(o.__dict__, indent=3)
            return json(o.__dict__)

        return str(o)
    except Exception, ex:
        raise Exception(
            "Unable to stringify the object! %s" % ex.message
        )


def guid(*size):
    size = 32 if len(size) == 0 else size[0]
    txt = hashlib.md5(str(uuid.uuid4())).hexdigest()
    cnt = len(txt)

    while size > cnt:
        txt = "%s%s" % (txt, hashlib.md5(str(uuid.uuid4())).hexdigest())
        cnt = len(txt)

    if cnt > size:
        txt = txt[0:size]

    return txt


def to_ascii(txt):
    if txt is None or not isinstance(txt, basestring):
        return txt
    try:
        return str(txt).encode("ascii", "ignore")
    except Exception, ex:
        raise ex


def to_unicode(txt, encoding="utf-8"):
    try:
        return unicode(txt, encoding)
    except Exception, ex:
        if txt is None:
            return None
        elif isinstance(txt, unicode):
            return txt
        try:
            return unicode(txt, "Latin-1")
        except Exception, e:
            raise Exception("Unable to convert to unicode: %s" % e.message)


def fix_str(txt):
    if txt is not None and isinstance(txt, basestring) is True:
        txt = to_unicode(txt, encoding="Latin-1").encode("utf-8")
    return txt


def base64(data):
    data = __b64__.encodestring(data)
    while data.find("\n") > -1:
        data = data.replace("\n", "")
    return data


def unbase64(data):
    data = __b64__.decodestring(data)
    return data


def unroll(lst):
    if lst is None:
        return []
    def list_or_tuple(x):
        return isinstance(x, (list, tuple))
    def flatten(seq, to_expand=list_or_tuple):
        for i in seq:
            if to_expand(i):
                for sub in flatten(i, to_expand):
                    yield sub
            else:
                yield i

    if list_or_tuple(lst) is False:
        return [lst]

    unravelled = []
    for o in flatten(lst):
        unravelled.append(o)
    return unravelled


def format_dollars(amount):
    try:
        amount = str(amount)
        if amount == "0":
            return "$0.00"
        amount = float(amount)
    except:
        return "$0.00"

    try:
        amount = '{:20,.2f}'.format(amount).strip()
        amount = "$%s" % amount
        amount = amount[0:(amount.find(".")) + 3]
    except:
        pass
    return amount


def rand(*limit, **kwd):
    """Return a random number in the given range"""
    min = 0 if not kwd else kwd.get("min", 0)
    max = 100000 if not limit else limit[0]
    rnd = random.randrange(min, max)
    return rnd


def coin_flip(bias=50):
    """Return True 50% of the time."""
    rnd = random.randrange(0, 100)
    flag = rnd <= bias
    return flag


class io:
    @staticmethod
    def path_concat(uri, relative):
        """Find the normalized relative path for the given uris"""
        path = os.path.join(uri, relative)
        path = os.path.normpath(path)
        return path

    @staticmethod
    def read_file(path, text=True, fn=None):
        if text is True:
            with codecs.open(path, "r", "utf-8") as f:
                data = f.read()
                if fn is not None:
                    data = fn(data)
                return data
        with open(path, "rb") as f:
            data = f.read()
            if fn is not None:
                data = fn(data)
            return data

    @staticmethod
    def write_file(path, data, text=False):
        if path.startswith("~"):
            relative = path[1:]
            path = expanduser("~")
            path = "%s%s" % (path, relative)

        if isinstance(data, list) is True:
            data = "\n".join(data)

        if io.exists(path) is True:
            os.remove(path)

        if text is False:
            try:
                with open(path, "wb") as f:
                    f.write(data)
                return
            except Exception, ex:
                message = "Error writing file [ {file} ] -> {message}".format(file=path, message=ex.message)
                print(message)
                raise Exception(message)

        try:
            with codecs.open(path, "w", "utf-8") as f:
                f.write(data)
        except Exception, ex:
            message = "Error writing file [ {file} ] -> {message}".format(file=path, message=ex.message)
            print(message)
            raise Exception(message)


    @staticmethod
    def exists(path):
        if not os.path.exists(path):
            return False
        return True
