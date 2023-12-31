from ckeditor_uploader.fields import RichTextUploadingField
from io import BytesIO
from PIL import Image
from django.core.files import File
import datetime
from django.urls import reverse
from django.db import models
from apps.accounts.models import User
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from treebeard.mp_tree import MP_Node
from apps.core.managers import PublishedManager
from apps.core.models import PublishStatusChoice, BaseModel
from utils.utils import jalali_converter
from taggit.managers import TaggableManager
# from colorfield.fields import ColorField


class Rate(BaseModel):
    rate = models.PositiveBigIntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        db_table = 'rates'
        indexes = [
            models.Index(fields=['content_type', 'object_id'])
        ]


class Post(BaseModel):
    objects = models.Manager()
    published = PublishedManager()

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}, related_name='posts', verbose_name=_('نویسنده'))
    title = models.CharField(_('عنوان'), max_length=150, db_index=True)
    slug = models.SlugField(
        unique=True, verbose_name=_('اسلاگ'), allow_unicode=True, default=None)
    body = RichTextUploadingField(_('متن مقاله'))
    thumbnail = models.ImageField(
        upload_to="posts/%Y/%m/%d")
    published_status = models.CharField(
        max_length=1, choices=PublishStatusChoice.choices, default='d', verbose_name=_('وضعیت انتشار'))
    category = models.ForeignKey(
        'BlogCategory', verbose_name=_('دسته بندی'), on_delete=models.CASCADE, )
    # tags = models.ManyToManyField("Tag", verbose_name=_('برچسب ها'), related_name='posts')

    # tags = TaggableManager()

    likes = models.PositiveBigIntegerField(default=0)
    dislikes = models.PositiveBigIntegerField(default=0)
    rates = GenericRelation(Rate)

    class Meta:
        db_table = 'posts'
        ordering = ['-created_at']
        verbose_name = _("مقاله")
        verbose_name_plural = _("مقاله ها")

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail",  args=[str(self.slug)])

    def posts_was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

    def jcreated_at(self):
        return jalali_converter(self.created_at)

    def category_published(self):
        return self.category.filter(status=True)

    def thumbnail_tag(self):
        return format_html("<img width=100 src='{}' />".format(self.thumbnail.url))

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Comment(BaseModel):
    user = models.ForeignKey(User, related_name='users',
                             on_delete=models.CASCADE, verbose_name=_('کاربر'))
    article = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name=_('نظر'))
    is_approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'comments'
        # ordering = ['-created_at']
        verbose_name = _("نظر")
        verbose_name_plural = _("نظرات")

    def __str__(self) -> str:
        return self.comment


class CommentReply(BaseModel):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField(verbose_name=_('نظر'))


class BlogCategory(MP_Node):
    parent = models.ForeignKey(
        'self', verbose_name=_('دسته بندی والد'), blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True,
                            db_index=True, verbose_name=_('عنوان'))
    slug = models.SlugField(max_length=255, unique=True,
                            verbose_name=_('اسلاگ'), allow_unicode=True)
    description = models.TextField(
        blank=True, null=True, max_length=2048, verbose_name=_('توضیحات'))
    is_active = models.BooleanField(
        default=True, verbose_name=_('دسته بندی فعال باشد?'))
    # image = models.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog_categories'
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("blog_category_detail",  args=[str(self.slug)])


class RecyclePost(Post):

    deleted = models.Manager()

    class Meta:
        proxy = True


class Vote(BaseModel):
    class VoteChoice(models.TextChoices):
        like = 'l', _('like')
        dislike = 'd', _('dislike')

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='votes')
    vote = models.CharField(max_length=12, choices=VoteChoice.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'votes'
        verbose_name = _('Vote')
        verbose_name_plural = _("Votes")


class Attachment(BaseModel):
    file = models.FileField(_('file'), upload_to='')
    # attachmentable = GenericForeignKey()


class NewsletterSubscriber(BaseModel):
    email = models.EmailField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.email
