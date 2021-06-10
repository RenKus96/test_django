def format_list(lst):
    return '<br>'.join(lst)


def format_records(lst):
    if len(lst) == 0:
        return '(Emtpy recordset)'
    return '<br>'.join(str(elem) for elem in lst)