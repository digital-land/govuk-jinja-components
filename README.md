# govuk-jinja-components

GOVUK Frontend components ported to jinja to use in Flask apps.

### Install

    pip install -e git+https://github.com/digital-land/govuk-jinja-components.git#egg=govuk_jinja_components

### Using with Flask

You need to initialise the extension. We use the factory method. So in you `extensions.py`:

    from govuk_jinja_components.flask_govuk_components import GovukComponents

    govuk_components = GovukComponents()

Then in your `factory.py`:

    def register_extensions(app):
        from application.extensions import govuk_components
        govuk_components.init_app(app)

Then the components should be available to your templates, e.g.

    {% from "govuk-jinja-components/inset-text/macro.jinja" import govukInsetText -%}
