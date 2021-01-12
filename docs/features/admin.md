# Django Admin

## ReadOnlyAdmin

If you want to make a model in the django Admin 100% read-only, you can derive your admin class from ``ReadOnlyAdmin``.
This will ensure that nobody can modify or delete the records of this class in any way.

Either you can register it like this:
````
admin.site.register(MyModel, ReadOnlyAdmin)
````

Or like this, if you want to customise it further:
````
@admin.register(MyModel)
class MyModelAdmin(ReadOnlyAdmin):
    ...
````

## EditableOnlyAdmin

If you want to make a model in the django Admin editable, but not create- or deletable, you can simply derive your
admin class from ``EditableOnlyAdmin``. This will ensure that nobody can modify or delete the records of this class
in any way.

Either you can register it like this:
````
admin.site.register(MyModel, EditableOnlyAdmin)
````

Or like this, if you want to customise it further:
````
@admin.register(MyModel)
class MyModelAdmin(EditableOnlyAdmin):
    ...
````

## ReadOnlyTabularInline

If you want to make a model ``MyModel`` 100% read-only, but the model is embedded in its parent, `MyParentModel`,
you can derive from the ``ReadOnlyTabularInline``. This will ensure that all instances of ``MyModel`` will not be
editable in any way.

````
from django.contrib import admin

class MyModelInline(ReadonlyTabularInline):
    model = MyModel
    ...

@admin.register(MyParentModel)
class MyParentModelAdmin(admin.ModelAdmin):
    inlines = [MyModelInline]
    ...
````
