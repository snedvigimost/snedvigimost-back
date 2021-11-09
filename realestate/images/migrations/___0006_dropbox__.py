from django.db import migrations

from dropbox import Dropbox
from dropbox.exceptions import ApiError
from dropbox.stone_validators import ValidationError

from realestate.images.models import Image
import environ
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()
client = Dropbox(env('DROPBOX_OAUTH2_TOKEN'))


def migrate_dropbox_path_to_url(apps, schema_editor):

    for mm in Image.objects.all():
        print(mm.id)
        try:
            file_link_metadata = client.sharing_create_shared_link_with_settings(mm.photo.name)
            downloadable_url = file_link_metadata.url.replace('dl=0', 'dl=1')
            mm.photo = downloadable_url
            mm.save()
        # for already shared files but not stored url
        except ApiError as e:
            try:
                url = e.error.get_shared_link_already_exists().get_metadata().url
                downloadable_url = url.replace('dl=0', 'dl=1')
                mm.photo = downloadable_url
                mm.save()
            except Exception:
                pass
        except ValidationError:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20200614_2019'),
    ]

    operations = [
        migrations.RunPython(migrate_dropbox_path_to_url)
    ]
