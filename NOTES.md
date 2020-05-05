# Differences between Nunjucks and Jinja

### Items

Some components use the `items` key. However, it is a Python dictionary method so can cause problems.

There are 2 ways to tackle this issue.

#### The one we use

Replace

    {% if item.item %}
        {% for item in item.items %}

With

    {% if item['items'] is not callable and item['items'] is iterable  %}
        {% for item in item['items'] %}

It checks `items` is a list to be iterated over.

#### Alternative approach

Rename `items` to something like `_items`.

Shortcoming of this approach is that the users of the component macros need to know about the name change. If they copy and paste code from the [GOV.UK design system](https://design-system.service.gov.uk/) it will break.
