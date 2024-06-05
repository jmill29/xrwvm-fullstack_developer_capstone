def format_query(text):
    text_arr = text.split(' ')
    formatted_query = ''
    for el in text_arr:
        formatted_query = formatted_query + el + '%20'
    formatted_query = formatted_query.strip('%20')
    return formatted_query
