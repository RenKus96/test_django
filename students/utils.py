def format_list(lst):
    return '<br>'.join(lst)


def format_records(lst):
    if len(lst) == 0:
        return '(Emtpy recordset)'
    return '<br>'.join(f'<b>{num}.</b> {elem}' for num,elem in enumerate(lst, 1))