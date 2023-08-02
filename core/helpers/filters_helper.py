class Filter:
    def __init__(self,fields: dict | None = None):
        if not fields:
            fields = {}

        self.fields = fields
