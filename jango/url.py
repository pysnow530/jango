import re
from importlib import import_module


def resolve(path_info, urlconf):
    """匹配请求url，返回匹配项"""
    urlconf_module = import_module(urlconf)
    urlpatterns = urlconf_module.urlpatterns

    for pattern in urlpatterns:
        regex = pattern[0]
        re_matched = re.match(regex, path_info)

        # ['hello/', view]
        if re_matched and callable(pattern[1]):
            callback = pattern[1]
            callback_kwargs = re_matched.groupdict()
            groups = re_matched.groups()
            callback_args = groups[:len(groups) - len(callback_kwargs)]
            return callback, callback_args, callback_kwargs

        # ['api/', 'demo.urls']
        elif re_matched and isinstance(pattern[1], str):
            resolve_match = resolve(path_info[re_matched.end():], pattern[1])
            if resolve_match:
                return resolve_match

    return None
