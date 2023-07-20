from django.core.checks import Tags, Warning, register


@register(Tags.compatibility)
def package_deprecation_warning(*args, **kwargs):
    return [Warning(
        "This package is deprecated and was superseded by Ambient Toolbox. ",
        hint="Please replace it: https://pypi.org/project/ambient-toolbox/",
        obj="ai_django_core",
        id="W001",
    )]
