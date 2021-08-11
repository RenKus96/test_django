from copy import copy


def get_params(request):
    context = {}
    params = request.GET
    if 'page' in params:
        params = copy(params)
        del params['page']

    context['get_params'] = params.urlencode()
    return context
