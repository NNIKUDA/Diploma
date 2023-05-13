from django.db import models


class NewsTag(models.Model):
    title = models.CharField(max_length=255, primary_key=True)

    class Meta:
        db_table = 'newstag'


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField()
    date = models.DateTimeField(null=False, default=None)
    tag = models.ManyToManyField(NewsTag)

    class Meta:
        db_table = 'news'


class Comment(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)  # Field renamed because it was a Python reserved word.
    news = models.ForeignKey(News, models.DO_NOTHING)
    # user_id = models.BigIntegerField()
    text = models.CharField(max_length=255)

    # todo user_id = models.ForeignKey

    class Meta:
        db_table = 'comment'
