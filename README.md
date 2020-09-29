# govuk_jinja_components

GOVUK Frontend components ported to jinja to use in Flask apps.

### Install

    pip install -e git+https://github.com/digital-land/govuk-jinja-components.git#egg=govuk_jinja_components

Run same command to update it.

### Using with Flask

You need to initialise the extension. We use the factory method. So in you `extensions.py`:

    from govuk_jinja_components.flask_govuk_components import GovukComponents

    govuk_components = GovukComponents()

Then in your `factory.py`:

    def register_extensions(app):
        from application.extensions import govuk_components
        govuk_components.init_app(app)

Then the components should be available to your templates, e.g.

    {% from "govuk-jinja-components/components/inset-text/macro.jinja" import govukInsetText -%}

### Alternative use

Even if you are not using flask, you can still use these templates with Jinja. You can do this by registering the templates.

    import jinja2
    
    # where you are setting up jinja add this
    multi_loader = jinja2.ChoiceLoader([
        jinja2.FileSystemLoader(searchpath="<<path to your templates>>"),
        jinja2.PrefixLoader({
            'govuk-jinja-components': jinja2.PackageLoader('govuk_jinja_components')
        })
    ])
    jinja2.Environment(loader=multi_loader)

