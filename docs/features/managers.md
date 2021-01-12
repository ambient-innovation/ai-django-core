# Managers

## Per-Object Permission Levels

### Motivation

A frequent requirement for information system database records are often not publicly visible. There are
strict rules who can view what. The django permission system allows to restrict access to a whole model but in a lot of
cases the visibility needs to be determined on object level. Let's say we have this data structure:

````
# models.py
class Company(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company)

class Project(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company)
````

We have a multi-tenant system which helps organising projects for different companies. As an employee of company A I
am only allowed to see all projects belonging to company A. If we would restrict access with the django permissions
to the project model, this would not suit our purpose.

### Custom manager

To tackle this problem, this library provides an abstract class (actually, there are two of them) to help structure
these access levels in a reproducible, understandable and DRY way.

If you derive your managers from ``AbstractUserSpecificManager``, you will expose three methods: `visible_for()`,
`editable_for()` and `deletable_for()`. Each methods needs to be implemented per manager class like this:

````
# managers.py
class ProjectManager(AbstractUserSpecificManager):

    def visible_for(self, user):
        return self.get_queryset().filter(company=user.company)

    def editable_for(self, user):
        return self.get_queryset().filter(company=user.company)

    def deletable_for(self, user):
        return self.get_queryset().filter(company=user.company)
````

Now just register the custom manager within the model:

````
# models.py
class Project(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company)

    objects = ProjectManager()
````

Now you can easily use the given methods in every view, service or serializers as follows:

````
# views.py
def project_list(request):
    project_list = Project.objects.all().visible_for(request.user)
    return render(request, 'project/project_list.html', {'project_list': project_list})
````

Obviously, if you are not listing your projects but want to validate if the user is allowed to create/edit or
delete the given object, you should use the other two methods.

### Best practice

As a nice tweak, you can skip the manger and use directly a ``QuerySet`` class and use this as a manager. Therefore this
package provides the class ``AbstractUserSpecificQuerySet``.

At first, use a custom queryset class like this:

````
# managers.py
class ProjectQuerySet(AbstractUserSpecificQuerySet):

    def visible_for(self, user):
        return self.filter(company=user.company)

    def editable_for(self, user):
        return self.filter(company=user.company)

    def deletable_for(self, user):
        return self.filter(company=user.company)
````

Take care that you need to register it a little different in the model:

````
# models.py
class Project(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company)

    objects = ProjectQuerySet.as_manager()
````

Then you'll save the ``.all()`` and can directly use the exposed methods:

````
project_list = Project.objects.visible_for(request.user)
````
