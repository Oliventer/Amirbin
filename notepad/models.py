from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import random
import string


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


def get_random_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str


class Note(models.Model):
    note_id = models.CharField(unique=True, primary_key=True, max_length=100, default=get_random_string)
    created = models.DateTimeField(auto_now_add=True)
    code = models.TextField(blank=True, default=print('Hello world!'), max_length=65536)
    delete_after_viewing = models.BooleanField(default=False)
    linenos = models.BooleanField(default=False)
    style = models.CharField(choices=STYLE_CHOICES, default='native', max_length=100)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Note, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']
