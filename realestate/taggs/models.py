from django.db.models import CharField, Model


class Tag(Model):
    title = CharField(null=True, max_length=250)

    class Meta:
        db_table = "Tag"

    def __str__(self):
        return self.title

