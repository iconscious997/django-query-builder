from distutils.core import setup

setup(
    name="querybuilder",
    version="0.1.10",
    packages=[
        "querybuilder",
    ],
    url="https://github.com/wesokes/django-query-builder",
    description="Django query builder",
    install_requires=[
        "django>=1.4",
    ]
)
