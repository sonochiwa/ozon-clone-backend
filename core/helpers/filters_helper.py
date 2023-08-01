class Filter:
    def __init__(
            self,
            fields: dict | None = None
    ):
        if not fields:
            fields = {}

        self.fields = fields

    def __str__(self):
        result = []

        for key, value in self.fields.items():
            result.append(f'{key}={value}')

        return '&'.join(result)
