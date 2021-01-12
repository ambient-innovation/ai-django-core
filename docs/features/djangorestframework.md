# Django REST framework extension

## Serializers

### BaseModelSerializer

This serializers extends the restframeworks ``ModelSerializer`` but ensures that the ``clean()`` method in the model
is called. By default, only django forms call the model-level clean, not the serializers.

````
# models.py
class MyModel(models.Model):
    ...

    def clean():
        # here lives the model-level validation
        ...

# serializers.py
class MyModelSerializer(ModelSerializer)
    class Meta:
        model = MyModel

    # do your stuff here!
````

Just derive your serializer from the ``BaseModelSerializer`` and you are good to go!

### CommonInfoSerializer

In addition to the ``CommonInfo`` model class which provides a neat way to set the creator and last editor of
any database object, this serializers takes care of setting those fields if a request user was found.

Furthermore it extens the ``BaseModelSerializer`` to ensure that model-level validation is called on serializer
validation.

````
# models.py
class MyOwnershipRelevantModel(CommonInfo):
    ...

# serializers.py
class MyOwnershipRelevantModelSerializer(CommonInfoSerializer)
    class Meta:
        model = MyOwnershipRelevantModel

    # do your stuff here!
````
