class PermissionModelMixin:
    """
    Abstract model class to put permissions in which don't belong to a "real" database model.
    Take care that you have to set "Meta.default_permissions" to an empty tuple/list if you want to avoid having the
    Django default permissions created.
    Inspiration / Source: https://stackoverflow.com/a/37988537/1331671
    """

    class Meta:
        # No database table creation or deletion operations will be performed for this model.
        managed = False
