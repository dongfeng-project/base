class DongFengException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class HTTPException(DongFengException):
    pass


class InvalidURL(HTTPException):
    def __init__(self, url):
        message = f"URL \"{url}\" invalid"
        super().__init__(message)


class UnsupportedHTTPMethod(HTTPException):
    def __init__(self, method: str = ""):
        message = f"HTTP method \"{method}\" not supported"
        super().__init__(message)


class IPException(DongFengException):
    pass


class InvalidIP(IPException):
    def __init__(self, ip):
        message = f"IP \"{ip}\" invalid"
        super().__init__(message)


class InvalidCIDR(IPException):
    def __init__(self, cidr):
        message = f"CIDR \"{cidr}\" invalid"
        super().__init__(message)
