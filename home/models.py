from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from home.blocks import FullWidthImageSectionBlock, FullWidthSectionBlock


class StaticPage(Page):
    body = StreamField([
        ('full_width_image', FullWidthImageSectionBlock()),
        ('full_width_section', FullWidthSectionBlock()),
        ('raw_html', blocks.RawHTMLBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class HomePage(Page):
    body = StreamField([
        ('full_width_image', FullWidthImageSectionBlock()),
        ('full_width_section', FullWidthSectionBlock()),
        ('raw_html', blocks.RawHTMLBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
