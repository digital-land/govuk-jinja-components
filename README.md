# govuk-jinja-components

GOVUK Frontend components ported to jinja to use in Flask apps.

Add this line to your requirements.txt

    -e git+https://github.com/digital-land/govuk-jinja-components#egg=govuk-jinja-components

Add the following to your Flask factory.py

    def register_templates(app):
        multi_loader = ChoiceLoader([
            app.jinja_loader,
            PrefixLoader({
                'govuk-jinja-components': PackageLoader('govuk-jinja-components')
            })
        ])
        app.jinja_loader = multi_loader
