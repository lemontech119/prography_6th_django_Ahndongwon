from django.db import models

# Create your models here.

class Subject(models.Model):
    id = models.AutoField(db_column="ID", primary_key=True)
    title = models.CharField(db_column="TITLE", max_length=100)
    description = models.TextField(db_column="DESCRIPTION")
    created_at = models.DateTimeField(db_column="CREATED_AT", auto_now_add=True)
    Modified_at = models.DateTimeField(db_column="MODIFIED_AT", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'subject'
        ordering = ('-created_at',)
