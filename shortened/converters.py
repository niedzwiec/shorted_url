class Hash:
    regex = '^[a-zA-Z0-9]{10}$'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
