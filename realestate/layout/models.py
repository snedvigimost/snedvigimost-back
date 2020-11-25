from django.db.models import CharField, Model


class Layout(Model):
    name = CharField(null=True, max_length=250)

    class Meta:
        db_table = "layout"

    def __str__(self):
        return self.name
