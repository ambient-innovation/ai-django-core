class PermissionModelMixin:
    """
    Abstract model class to put permissions in which don't belong to a "real" database model.
    Inspiration / Source: https://stackoverflow.com/a/37988537/1331671
    """

    class Meta:
        # No database table creation or deletion operations will be performed for this model.
        managed = False
        # Disable "add", "change", "delete" and "view" default permissions
        default_permissions = ()
