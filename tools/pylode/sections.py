"""Narrative sections for the generated page (SKOS-Reference-style chapters).

A sections directory holds numbered markdown files (``01-introduction.md``), each
with a minimal front-matter::

    ---
    title: Documents
    terms: Document schema:headline schema:abstract
    ---
    prose in markdown ...
    <!-- definitions -->
    prose rendered AFTER the term definitions (integrity conditions, examples, notes)

``terms`` lists the page ANCHORS of the terms the chapter owns (bare local name for
the ontology's own terms, ``prefix:LocalName`` for borrowed ones), separated by
whitespace or commas. A chapter with no terms is pure prose. Terms not assigned to
any chapter stay in the standard trailing listings (Classes, Object Properties, ...).
"""
import os
import re

import markdown

MARKER = "<!-- definitions -->"


def _render(md_text):
    return markdown.markdown(md_text, extensions=["tables", "fenced_code"])


def _slug(text):
    text = re.sub(r"^[\d.\s]+", "", text)
    return re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()


def _add_ids(html, prefix):
    """Give every prose <h3> an id and collect (id, title) for the ToC."""
    subs = []

    def repl(m):
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        sid = f"{prefix}-{_slug(title)}"
        subs.append({"id": sid, "title": title})
        return f'<h3 id="{sid}">{m.group(1)}</h3>'

    return re.sub(r"<h3>(.*?)</h3>", repl, html, flags=re.S), subs


def load_sections(sections_dir):
    sections = []
    for fname in sorted(os.listdir(sections_dir)):
        if not fname.endswith(".md"):
            continue
        text = open(os.path.join(sections_dir, fname), encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if not m:
            raise ValueError(f"{fname}: missing '---' front-matter")
        fm, body = m.groups()
        meta = {}
        for line in fm.split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        if "title" not in meta:
            raise ValueError(f"{fname}: front-matter has no 'title'")
        terms = [t for t in re.split(r"[,\s]+", meta.get("terms", "")) if t]
        before, _, after = body.partition(MARKER)
        slug = re.sub(r"^\d+-", "", fname[:-3])
        html_before, subs_before = _add_ids(_render(before), f"sec-{slug}")
        html_after, subs_after = (None, [])
        if after.strip():
            html_after, subs_after = _add_ids(_render(after), f"sec-{slug}")
        sections.append({
            "slug": slug,
            "title": meta["title"],
            "terms": terms,
            "html": html_before,
            "html_after": html_after,
            "subs_before": subs_before,
            "subs_after": subs_after,
        })
    return sections
