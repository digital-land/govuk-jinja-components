import glob
import os

from setuptools import setup

components = []
directories_html = glob.glob("govuk_jinja_components/**/**/*.html", recursive=True)
directories_jinja = glob.glob("govuk_jinja_components/**/**/*.jinja", recursive=True)

for directory in directories_html:
    components.append(os.path.relpath(os.path.dirname(directory), "govuk_jinja_components") + "/*.html")

for directory in directories_jinja:
    components.append(os.path.relpath(os.path.dirname(directory), "govuk_jinja_components") + "/*.jinja")

setup(
    name="govuk-jinja-components",
    version="0.1.0",
    author="Colm Britton",
    description="GOVUK Design system components ported from Nunjucks to Jinja",
    license="MIT",
    packages=["govuk_jinja_components"],
    package_data={'govuk-jinja-components': components},
    python_requires=">=3.5",
    install_requires=[
        "jinja2",
    ],
)
