def has_error(**kwargs):
    data = locals()
    params = data['kwargs']
    params['class'] = "input is-danger"
    return params
