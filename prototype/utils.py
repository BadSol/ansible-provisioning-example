from fdfgen import forge_fdf
from django.core.files import File
from django.conf import settings
from subprocess import call


class PgxPrototypeDocument:
    """Prototype document model"""
    pdf_form_name = 'pdx_prototype_form_1'

    def __init__(self, subject, published_data, service_name, published_data_url_address, date):
        self.field_list = [('field_1', subject),  # todo: change field names inside template pdf
                           ('field_2', published_data),
                           ('field_3', service_name),
                           ('field_4', published_data_url_address),
                           ('field_5', date),
                           ('field_6', service_name),
                           ('field_7', published_data_url_address),
                           ('field_8', published_data)]

    def return_field_list(self):
        if self.field_list:
            return self.field_list
        else:
            return None

    def return_fdf_data(self):
        return generate_fdf_from_fields(self.field_list)

    def save_fdf_file_to_media(self, file_name):
        save_file_to_media(self.return_fdf_data(), file_name)
        return True

    def generate_and_save_pdf_to_media(self, output_name):  # todo: cut out file extension, so it wont generate .pdf.pdf
        ftf_file_name = 'temp_ftf_file'
        self.save_fdf_file_to_media(ftf_file_name)

        generate_pdf_file_with_pdftk(self.pdf_form_name, ftf_file_name, output_name)


# todo: Move those methods to new generic class


# class PdfDocumentManagement:


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
    :param file_data:
    :return:
    """
    # print(settings.MEDIA_ROOT)
    with open('{media_root}/ftf_files/{file_name}.fdf'.format(media_root=settings.MEDIA_ROOT, file_name=file_name),
              'wb') as f:
        fbf_file = File(f)
        fbf_file.write(file_data)


def generate_pdf_file_with_pdftk(pdf_form_name, ftf_file_name, output_pdf_name):  # todo: store catalog path in settings
    """
    Generate pdf file using external tool (pdftk)
    :param pdf_form_name:
    :param ftf_file_name:
    :param output_pdf_name:
    :return:
    """

    call(["pdftk",
          "./media/pdf_forms/{pdf_form_name}.pdf".format(pdf_form_name=pdf_form_name),
          "fill_form",
          "./media/ftf_files/{ftf_file_name}.fdf".format(ftf_file_name=ftf_file_name),
          "output",
         "./media/pdf_outputs/{output_pdf_name}.pdf".format(output_pdf_name=output_pdf_name),
          "flatten"])

