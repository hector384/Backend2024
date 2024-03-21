from .check import check


def get_csrftoken_by_request(info):
    token = info.context.META.get("HTTPS_CSRFTOKEN")
    if token is None:
        token = info.context.META.get("HTTP_CSRFTOKEN")
    if check.check_csrftoken(token):
        return token
