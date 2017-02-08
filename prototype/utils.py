from fdfgen import forge_fdf


def generate_fdf_from_fields(field_list):
    """
    Generate fdf file data from the fields list.
    fdf file is needed to populate pdf forms with values.
    :param field_list: list of field name, field value tuples
    :return: fdf file data ready for writing.
    """
    fdf = forge_fdf("", field_list, [], [], [])

    return fdf
