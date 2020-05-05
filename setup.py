from setuptools import setup

setup(
    name="govuk-jinja-components",
    version="0.0.2",
    author="Colm Britton",
    description="GOVUK Design system components ported from Nunjucks to Jinja",
    license="MIT",
    packages=["govuk_jinja_components"],
    package_data={'govuk-jinja-components': ['templates/**.*']},
    python_requires=">=3.6",
    install_requires=[
        "jinja2",
    ],
)
