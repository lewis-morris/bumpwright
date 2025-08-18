# docs/_ext/mdblock.py
from docutils.parsers.rst import Directive
from docutils.utils import new_document
from docutils import nodes

from myst_parser.parsers.docutils_ import Parser as MystParser  # MyST's docutils parser

class MarkdownBlock(Directive):
    has_content = True

    def run(self):
        md_text = "\n".join(self.content)
        # create a sub-document with the same settings as the current one
        settings = self.state.document.settings
        subdoc = new_document(self.state.document["source"], settings=settings)
        MystParser().parse(md_text, subdoc)

        container = nodes.container("", *subdoc.children,
                                    classes=["md-container"])
        if "id" in self.options:
            container["ids"].append(self.options["id"])

        return [container]

def setup(app):
    app.add_directive("markdown", MarkdownBlock)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
