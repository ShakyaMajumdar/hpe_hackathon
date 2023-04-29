from django.db import models

# pyright: reportUnknownVariableType=false
# pyright: reportUnknownMemberType=false


class Article(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    pub_date = models.DateField()

    def __str__(self) -> str:
        return self.title
