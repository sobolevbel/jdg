from slugify import slugify_url


def slugify(text: str, separator: str):
    return slugify_url(text, separator=separator)
