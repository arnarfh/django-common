from wagtail.core import blocks as wagtail_blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock

# Extended Text Editor features
TEXT_FEATURES = ["bold", "italic", "ol", "ul", "link", "document-link", "embed"]

# Simple, basic Text Editor features
SIMPLE_TEXT_FEATURES = ["bold", "italic", "link"]


class HeadingBlock(wagtail_blocks.StructBlock):
    """
    Block for a heading.
    """

    heading = wagtail_blocks.CharBlock(label="Heading")
    heading_level = wagtail_blocks.ChoiceBlock(
        label="Heading",
        choices=[("h1", "h1"),("h2", "h2"),("h3", "h3"),("h4", "h4"),("h5", "h5")],
        default="h2",
        required=False
    )

    class Meta:
        label = "Heading"
        icon = "title"
        template = "content/blocks/heading.html"

class TextBlock(wagtail_blocks.StructBlock):
    """
    Block for general text.
    """

    text = wagtail_blocks.RichTextBlock(features=TEXT_FEATURES)
    style = wagtail_blocks.ChoiceBlock(
        label="Style",
        choices=[("text", "Text"), ("lead", "Lead"), ("quote", "Quote"), ("code", "Code")]
    )

    class Meta:
        label = "Text"
        icon = "pilcrow"
        template = "content/blocks/text.html"

class ImageBlock(wagtail_blocks.StructBlock):
    """
    Block for image, and caption.
    """

    image = ImageChooserBlock(label="Image")
    caption = wagtail_blocks.RichTextBlock(
        features=SIMPLE_TEXT_FEATURES,
        label="Caption",
        required=False
    )

    class Meta:
        label = "Image"
        icon = "image"
        template = "content/blocks/image.html"

LINK_STYLE_CHOICES = [("link", "Link"), ("button", "Button")]

class LinkBlock(wagtail_blocks.StructBlock):
    """
    Block for internal image link.
    """

    link = wagtail_blocks.PageChooserBlock(label="Page")
    text = wagtail_blocks.CharBlock(
        label="Link text",
        required=False,
        help_text="Overrides the title of the linked page",
    )
    style = wagtail_blocks.ChoiceBlock(
        label="Style",
        choices=LINK_STYLE_CHOICES,
        default="link",
        required=False
    )

    class Meta:
        label = "Internal link"
        icon = "link"
        template = "content/blocks/internal_link.html"

class ExternalLinkBlock(wagtail_blocks.StructBlock):
    """
    Block for external links.
    """

    link = wagtail_blocks.URLBlock(label="URL")
    text = wagtail_blocks.CharBlock(
        label="Link text",
        required=False
    )
    style = wagtail_blocks.ChoiceBlock(
        label="Style",
        choices=LINK_STYLE_CHOICES,
        default="link",
        required=False
    )

    class Meta:
        label = "External link"
        icon = "link"
        template = "content/blocks/external_link.html"

class ContentBlock(wagtail_blocks.StreamBlock):
    """
    Stream of all the single blocks.
    """

    heading = HeadingBlock()
    text = TextBlock()
    image = ImageBlock()
    internal_link = LinkBlock()
    external_link = ExternalLinkBlock()
    documents = wagtail_blocks.ListBlock(
        DocumentChooserBlock(),
        label="Document",
        template="content/blocks/documents.html",
        icon="doc-empty"
    )
    embed = EmbedBlock(label="Embed")
    html = wagtail_blocks.RawHTMLBlock(label="HTML")

    class Meta:
        label = "Content"
        template = "content/blocks/content.html"
