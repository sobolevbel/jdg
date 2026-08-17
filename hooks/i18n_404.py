"""Keep the site's 404 page in the default language.

MkDocs writes 404.html at the top of site_dir on every build, and
mkdocs-static-i18n runs one build per language into that same site_dir, so the
last language to build (English) overwrites the page — a Russian reader who
mistypes a URL gets an English 404 with an English nav. This hook stashes the
default language's 404 and puts it back after the localized builds, and files
each localized copy under its own tree. GitHub Pages only ever serves the root
404.html, so the localized copies are there for correctness, not for it.
"""

import os

_default = {}


def on_post_build(config, **kwargs):
    site_dir = config["site_dir"]
    root = os.path.join(site_dir, "404.html")
    if not os.path.exists(root):
        return
    i18n = config["plugins"].get("i18n")
    if not i18n:
        return
    default_locale = next(
        (lang.locale for lang in i18n.config.languages if lang.default), None
    )
    locale = config["theme"]["language"]

    if locale == default_locale:
        with open(root, encoding="utf-8") as fh:
            _default["html"] = fh.read()
        return

    with open(root, encoding="utf-8") as fh:
        localized = fh.read()
    path = os.path.join(site_dir, locale, "404.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(localized)

    # Never leave the site without a root 404: only restore what we captured.
    if _default.get("html"):
        with open(root, "w", encoding="utf-8") as fh:
            fh.write(_default["html"])
