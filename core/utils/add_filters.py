def add_filters(query, filters):
    for field_name in filters.fields.keys():
        query = query.where(field_name == filters.fields[field_name])

    return query
