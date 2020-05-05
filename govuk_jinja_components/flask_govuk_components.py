
from jinja2 import PackageLoader, PrefixLoader, ChoiceLoader


class GovukComponents():
    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        multi_loader = ChoiceLoader([
            app.jinja_loader,
            PrefixLoader({
                'govuk-jinja-components': PackageLoader('govuk_jinja_components')
            })
        ])
        app.jinja_loader = multi_loader
