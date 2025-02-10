from django.db.models import (Model, CharField, DateTimeField, TextField, ForeignKey, SET_NULL)
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Note(Model):
    author = ForeignKey(User, null=True, blank=False, on_delete=SET_NULL)    #null и blank как True для того, чтобы можно было создать миграции, когда уже есть заполненная БД
    title = CharField(max_length=255)
    text = TextField(blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-updated']
