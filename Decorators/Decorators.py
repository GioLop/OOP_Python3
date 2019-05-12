class Foo:
    @property
    def foo(self):
        return "bar"

    @foo.setter
    def foo(self, value):
        self._foo = value