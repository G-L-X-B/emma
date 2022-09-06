from emma.util.checks import check_isidentifier


class Point:
    """A point in a space of arbitrary dimensions.

    Point(mapping) -> new `Point` that uses mapping to initialize its
    axes and values. Axes names must be valid python identifiers.
    Note that names 'axes' and 'dimensions' are reserved. Values must
    be `float`-convertible.

    Axes can be accessed directly as members of a `Point` object."""

    def __init__(self, **axes):
        self.__axes = {}
        for axis, value in axes.items():
            check_isidentifier(axis)
            if axis in dir(self) or axis == 'dimensions' or axis == 'axes':
                raise ValueError(f"Can't name an axis '{axis}'.")
            super().__getattribute__('_Point__axes')[axis] = float(value)

    def __repr__(self):
        axes = super().__getattribute__('_Point__axes')
        return f"Point({', '.join('{}={}'.format(*x) for x in axes.items())})"

    def __getattribute__(self, name: str):
        axes = super().__getattribute__('_Point__axes')
        if name == 'dimensions':
            return len(axes)
        elif name == 'axes':
            return {axes.keys()}
        elif name in axes.keys():
            return axes[name]
        else:
            return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == 'dimensions':
            raise AttributeError('One cannot simply change amount of dimensions in a space the point belongs to.')
        elif name == 'axes':
            raise AttributeError("'axes' member is not accessible.")
        try:
            axes = super().__getattribute__('_Point__axes')
            if name not in self.axes:
                raise AttributeError()
            axes[name] = float(value)
        except (AttributeError, KeyError):
            super().__setattr__(name, value)
