from django.db import models


class NewsTag(models.Model):
    title = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'newstag'
        verbose_name = 'News tag'
        verbose_name_plural = 'News tags'


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='images/blog/')
    date = models.DateField(null=True, blank=True, default=None)
    tag = models.ManyToManyField(NewsTag)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'news'
        verbose_name = 'Article'
        verbose_name_plural = 'News'


class Comment(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)  # Field renamed because it was a Python reserved word.
    news = models.ForeignKey(News, models.DO_NOTHING)
    # user_id = models.BigIntegerField()
    text = models.CharField(max_length=255)

    # todo user_id = models.ForeignKey

    class Meta:
        managed = False
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
