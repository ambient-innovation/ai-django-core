import requests
from django.shortcuts import _get_queryset
import httplib
from django.core.files.base import File
from django.core.files.temp import NamedTemporaryFile



def get_object_or_none(klass, *args, **kwargs):
    """
    Uses get() to return an object, or raises a Http404 exception if the object
    does not exist.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the get() query.

    Note: Like with get(), an MultipleObjectsReturned will be raised if more than one
    object is found.
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None
    
def save_image_from_url(model, url):
    r = requests.get(url)

    img_temp = NamedTemporaryFile()
    img_temp.write(r.content)
    img_temp.flush()

    model.picture.save(model.image_id+".jpg", File(img_temp), save=True)
    
    
def get_attr_lang(obj, attrname, lang):
    value_en = getattr(obj, attrname + "_en")
    if lang == "en" and value_en is not None and len(value_en) > 0:
        return value_en
    else:
        return getattr(obj, attrname + "_de")
        