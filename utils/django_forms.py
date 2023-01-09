def add_placeholder(field, place_value):
    field.widget.attrs.update({'placeholder': place_value})


def add_attr(field, attr_name, value):
    field.widget.attrs.update({attr_name: value})
