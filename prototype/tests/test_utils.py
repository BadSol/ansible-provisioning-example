import pytest

from prototype.utils import generate_fdf_from_fields, PgxPrototypeDocument


def test_generate_fdf_from_fields_returning_correct_data_stream():
    test_field_list = [('field_'+str(n), 'field_value_'+str(n)) for n in range(0, 2)]

    result = generate_fdf_from_fields(test_field_list)
    expected_stream = b'%FDF-1.2\n%\xe2\xe3\xcf\xd3\r\n1 0 obj\n<</FDF<</Fields' \
                      b'[<</T(\xfe\xff\x00f\x00i\x00e\x00l\x00d\x00_' \
                      b'\x000)/V(\xfe\xff\x00f\x00i\x00e\x00l\x00d\x00' \
                      b'_\x00v\x00a\x00l\x00u\x00e\x00_\x000)/ClrF 2/ClrFf 1>>' \
                      b'<</T(\xfe\xff\x00f\x00i\x00e\x00l\x00d\x00_\x001)/V' \
                      b'(\xfe\xff\x00f\x00i\x00e\x00l\x00d\x00_\x00v\x00' \
                      b'a\x00l\x00u\x00e\x00_\x001)/ClrF 2/ClrFf 1>>]\n>>\n>' \
                      b'>\nendobj\ntrailer\n\n<<\n/Root 1 0 R\n>>\n%%EOF\n\n'

    assert(result == expected_stream)


def test_pbx_prototype_document_fail_initialization_without_arguments():
    with pytest.raises(TypeError):
        PgxPrototypeDocument()


def test_pbx_prototype_document_returning_correct_fields_when_few_fields_use_the_same_value():
    testing_values = [n for n in range(0, 5)]
    document = PgxPrototypeDocument(*testing_values)
    result = document.return_field_list()

    assert result[1][1] == 1 and result[7][1] == 1
