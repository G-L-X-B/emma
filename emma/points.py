from emma.util.checks import check_isidentifier


class Point:
    """A point in a space of arbitrary dimensions.

    Point(point) -> copies point.

    Point(**mapping) -> a new `Point` that uses mapping to initialize
    its axes and values. Axes names must be valid python identifiers.
    Note that names 'axes' and 'dimensions' are reserved. Values must
    be `float`-convertible.

    Point(point, **mapping) -> copies point and then creates or
    overwrites axes given in the mapping.

    Axes can be accessed directly as members of a `Point` object."""

    def __init__(self, other=None, **axes):
        self.__axes = {}
        pairs = list(axes.items())
        if other is not None:
            pairs += other.__axes.items()
        for axis, value in sorted(pairs):
            check_isidentifier(axis)
            if axis in dir(self) or axis == 'dimensions' or axis == 'axes':
                raise ValueError(f"Can't name an axis '{axis}'.")
            self.__axes[axis] = float(value)

    def __repr__(self):
        return f"Point({', '.join('{}={}'.format(*x) for x in self.__axes.items())})"

    def __getattribute__(self, name: str):
        axes = super().__getattribute__('_Point__axes')
        if name == 'dimensions':
            return len(axes)
        elif name == 'axes':
            return tuple(axes.keys())
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
            axes = self.__axes
            if name not in self.axes:
                raise AttributeError()
            axes[name] = float(value)
        except (AttributeError, KeyError):
            super().__setattr__(name, value)

    def __eq__(self, other) -> bool:
        try:
            for axis1, axis2 in zip(
                    self.__axes.items(),
                    other.__axes.items(),
                    strict=True):
                if axis1 != axis2:
                    raise ValueError()
        except ValueError:
            return False
        return True

    def is_same_space(self, other) -> bool:
        return self.axes == other.axes

    def __add__(self, other):
        sums = {}
        if not self.is_same_space(other):
            raise AxesError()
        for axis in self.__axes.keys():
            sums[axis] = self.__axes[axis] + other.__axes[axis]
        return Point(**sums)

    def __sub__(self, other):
        subs = {}
        if not self.is_same_space(other):
            raise AxesError()
        for axis in self.__axes.keys():
            subs[axis] = self.__axes[axis] - other.__axes[axis]
        return Point(**subs)


class AxesError(AttributeError):
    """Raised when points have different axes."""
    pass
