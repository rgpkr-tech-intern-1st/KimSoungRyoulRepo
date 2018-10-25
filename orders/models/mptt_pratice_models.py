from mptt import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Post(models.Model):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=250
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        max_length=250,
        unique=False,
        allow_unicode=True
    )
    category = TreeForeignKey(
        'Category',
        verbose_name=_('category'),
        null=True,
        blank=True,
        db_index=True,
        on_delete=models.SET_NULL,
    )


class Category(MPTTModel):
    parent = TreeForeignKey(
        'self',
        verbose_name=_('parent'),
        blank=True,
        null=True,
        related_name='children',
        db_index=True
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=128
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        max_length=250,
        unique=True,
        allow_unicode=True
    )

    class Meta:
        ordering = ['tree_id', 'lft']

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title
