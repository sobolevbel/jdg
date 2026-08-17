"""Mirror redirect stubs into the localized builds.

mkdocs-redirects writes one stub per redirect_maps entry, keyed by a docs source
path. Under mkdocs-static-i18n suffix mode the English pages live under /en/, so
a 'page.en.md' key would put its stub at /page.en/ — a URL the site never had —
aimed at /target.en/, which is never built, while the English URL that did exist,
/en/page/, gets no stub at all. So redirect_maps holds only the canonical
(Russian) pairs and this hook writes the localized copies from the same map,
keeping one source of truth. The relative target is identical in every language
tree, which is why the stub can be reused verbatim.
"""

import os

STUB = """<!doctype html>
<html lang="{lang}">
<head>
    <meta charset="utf-8">
    <title>Redirecting...</title>
    <link rel="canonical" href="{target}">
    <script>var anchor=window.location.hash.substr(1);location.href="{target}"+(anchor?"#"+anchor:"")</script>
    <meta http-equiv="refresh" content="0; url={target}">
</head>
<body>
You're being redirected to a <a href="{target}">new destination</a>.
</body>
</html>
"""


def _page_dir(src_uri: str) -> str:
    """'registration.md' -> 'registration' (mkdocs 'directory URLs' layout)."""
    return src_uri[: -len(".md")] if src_uri.endswith(".md") else src_uri


def _locales(config) -> list:
    """Non-default locales, i.e. the ones i18n builds into a subdirectory."""
    i18n = config["plugins"].get("i18n")
    if not i18n:
        return []
    return [
        lang.locale
        for lang in i18n.config.languages
        if not lang.default and lang.locale
    ]


def on_post_build(config, **kwargs):
    redirects = config["plugins"].get("redirects")
    if not redirects:
        return
    site_dir = config["site_dir"]
    for locale in _locales(config):
        for old, new in redirects.config["redirect_maps"].items():
            # '.en.md'-style keys are the broken form this hook replaces
            if _page_dir(old).endswith("." + locale):
                continue
            target = "../" + _page_dir(new) + "/"
            path = os.path.join(site_dir, locale, _page_dir(old), "index.html")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(STUB.format(lang=locale, target=target))
