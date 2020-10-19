import pytest
from hueb.apps.hueb20.models.document import Document


@pytest.fixture
def documents():
    document_1 = Document()
    document_1.title = "Document 1"
    document_1.save()
    document_2 = Document()
    document_2.title = "Document 2"
    document_2.save()

    return (document_1, document_2)


@pytest.mark.django_db
def test_no_translations(documents):
    assert documents[0].translations.exists() == False
    assert documents[1].translations.exists() == False


@pytest.mark.django_db
def test_translations(documents):
    documents[0].translations.add(documents[1])
    documents[0].save()
    assert documents[0].translations.first() == documents[1]
    assert documents[1].originals.first() == documents[0]
