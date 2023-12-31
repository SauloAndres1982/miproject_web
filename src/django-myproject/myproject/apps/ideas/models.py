from django.db import models
from django. urls import reverse
from django.utils.translation import gettext_lazy as _

from myproject.apps.core.models import CreationModificationDateBase, MetaTagsBase, UrlBase


class Idea(CreationModificationDateBase, MetaTagsBase, UrlBase):

    title = models.CharField(_("Title"), max_length=200)
    content = models.TextField(_("Content"))

    class Meta:
        verbose_name = _("Idea")
        verbose_name_plural = _("Ideas")

    def _str__(self):
        return self.title
    
    def get_url_path(self):
        return reverse("idea_details", kwargs={
            "idea_id":str(self.pk),
        })

# Create your models here.

