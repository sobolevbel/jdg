"""Генерирует FAQPage JSON-LD для страниц FAQ из заголовков h3/h4 и их содержимого."""

import json
import re

FAQ_PAGES = {"faq.md", "faq.en.md"}
HEADING = re.compile(r"<h([34])[^>]*>(.*?)</h\1>", re.S)
TAG = re.compile(r"<[^>]+>")
MAX_ANSWER = 1500


def _text(html: str) -> str:
    text = TAG.sub(" ", html)
    text = text.replace("&para;", " ").replace("¶", " ")
    return re.sub(r"\s+", " ", text).strip()


def on_page_content(html, page, config, files):
    if page.file.src_uri not in FAQ_PAGES:
        return html
    qa = []
    parts = HEADING.split(html)
    # parts = [до первого заголовка, уровень, текст заголовка, тело, уровень, ...]
    for i in range(1, len(parts) - 2, 3):
        question = _text(parts[i + 1])
        body = parts[i + 2]
        # тело вопроса заканчивается на следующем h2 (начало новой секции)
        body = re.split(r"<h2[^>]*>", body)[0]
        answer = _text(body)
        if question and answer:
            qa.append(
                {
                    "@type": "Question",
                    "name": question,
                    "acceptedAnswer": {"@type": "Answer", "text": answer[:MAX_ANSWER]},
                }
            )
    if qa:
        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": qa,
        }
        page._faq_schema = (
            '<script type="application/ld+json">'
            + json.dumps(schema, ensure_ascii=False)
            + "</script>"
        )
    return html


def on_post_page(output, page, config):
    schema = getattr(page, "_faq_schema", None)
    if schema:
        return output.replace("</head>", schema + "</head>", 1)
    return output
