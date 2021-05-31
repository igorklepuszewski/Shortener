from django.db import models
from hashlib import md5

# Create your models here.


class Link(models.Model):
    '''
        Creates short url based on long_url
        long_url -> original url
        short_url -> shotened url
    '''

    long_url = models.URLField()
    _short_hash = models.CharField(max_length=8, unique=True, blank=True)

    @property
    def short_url(self):
        return self._short_hash

    def __str__(self):
        return f'{self.long_url} -> {self._short_hash}'

    def save(self, *args, **kwargs):
        self.validate_unique()

        if not self.id:
            self._short_hash = md5(self.long_url.encode()).hexdigest()[:8]

        super().save(*args, **kwargs)
