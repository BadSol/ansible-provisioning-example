from fdfgen import forge_fdf
from django.core.files import File
from django.conf import settings


def generate_fdf_from_fields(field_list):
    """
    Generate fdf file data from the fields list.
    fdf file is needed to populate pdf forms with values.
    :param field_list: list of field name, field value tuples
    :return: fdf file data ready for writing.
    """
    fdf = forge_fdf("", field_list, [], [], [])

    return fdf


def save_file_to_media(file_data, file_name):  # todo: test this method
    """
    Saves fdf files to media folder
    :param file_data:
    :return:
    """
    # print(settings.MEDIA_ROOT)
    with open('{media_root}/ftf_files/{file_name}.fdf'.format(media_root=settings.MEDIA_ROOT, file_name=file_name),
              'wb') as f:
        fbf_file = File(f)
        fbf_file.write(file_data)
