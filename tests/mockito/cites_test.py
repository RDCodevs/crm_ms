import unittest
from unittest.mock import patch, MagicMock, Mock

from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder

from src.config.database import Session
from src.models.cites import Cites as CiteModel
from src.schemas.cites import Cites, UpdateCite
from src.services.cites import (
    get_cite_by_id,
    get_cite_by_patient_id,
    get_cites_by_medic_id,
    create_cite,
    patch_cite,
    delete_cite,
)


def get_all_cites():
    db = Session()
    res = db.query(CiteModel).all()

    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(res))


class TestCiteFunctions(unittest.TestCase):
    @patch("src.config.database.Session")
    def test_get_all_cites(self, mock_session):
        # Crea una instancia ficticia de CiteModel para simular la respuesta de la base de datos
        cite1 = CiteModel(..., id_cite=1)
        cite2 = CiteModel(..., id_cite=2)

        # Configura el comportamiento del objeto Mock de la sesión de la base de datos
        mock_db_session = MagicMock()
        mock_db_session.query.return_value.all.return_value = [cite1, cite2]
        mock_session.return_value = mock_db_session

        # Llama a la función que deseas probar
        response = get_all_cites()

        # Verifica el resultado esperado
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder([cite1, cite2]))

    @patch("src.config.database.Session")
    def test_get_cite_by_id(self, mock_session):
        # Crea una instancia ficticia de CiteModel para simular la respuesta de la base de datos
        cite = CiteModel(..., id_cite=1)

        # Configura el comportamiento del objeto Mock de la sesión de la base de datos
        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = cite
        mock_session.return_value = mock_db_session

        # Llama a la función que deseas probar
        response = get_cite_by_id(1)

        # Verifica el resultado esperado
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(cite))

    @patch("src.config.database.Session")
    def test_get_cite_by_patient_id(self, mock_session):
        # Crea una instancia ficticia de CiteModel para simular la respuesta de la base de datos
        cite = CiteModel(..., id_cite=1)

        # Configura el comportamiento del objeto Mock de la sesión de la base de datos
        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = cite
        mock_session.return_value = mock_db_session

        # Llama a la función que deseas probar
        response = get_cite_by_patient_id(1)

        # Verifica el resultado esperado
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(cite))

    @patch("src.config.database.Session")
    def test_get_cites_by_medic_id(self, mock_session):
        # Crea una instancia ficticia de CiteModel para simular la respuesta de la base de datos
        cite1 = CiteModel(..., id_cite=1)
        cite2 = CiteModel(..., id_cite=2)

        # Configura el comportamiento del objeto Mock de la sesión de la base de datos
        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.all.return_value = [
            cite1,
            cite2,
        ]
        mock_session.return_value = mock_db_session

        # Llama a la función que deseas probar
        response = get_cites_by_medic_id(1)

        # Verifica el resultado esperado
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder([cite1, cite2]))

    @patch("src.config.database.Session")
    def test_create_cite(self, mock_session):
        # Crea una instancia ficticia de CiteModel para simular la creación de una nueva cita
        new_cite = Cites(..., id_cite=1)

        # Configura el comportamiento del objeto Mock de la sesión de la base de datos
        mock_db_session = MagicMock()
        mock_db_session.add.return_value = None
        mock_db_session.commit.return_value = None
        mock_session.return_value = mock_db_session

        # Llama a la función que deseas probar
        response = create_cite(new_cite)

        # Verifica el resultado esperado
        self.assertEqual(response, new_cite.dict())

    @patch("src.config.database.Session")
    def test_patch_cite(self, mock_session):
        # Crea una instancia ficticia de CiteModel para simular la respuesta de la base de datos
        cite = CiteModel(..., id_cite=1)

        # Configura el comportamiento del objeto Mock de la sesión de la base de datos
        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = cite
        mock_db_session.add.return_value = None
        mock_db_session.commit.return_value = None
        mock_db_session.refresh.return_value = None
        mock_session.return_value = mock_db_session

        # Crea una instancia de UpdateCite para especificar los campos que se actualizarán
        updated_cite = UpdateCite(..., id_cite=1)

        # Llama a la función que deseas probar
        response = patch_cite(updated_cite)

        # Verifica el resultado esperado
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(cite))

    @patch("src.config.database.Session")
    def test_delete_cite(self, mock_session):
        # Crea una instancia ficticia de CiteModel para simular la respuesta de la base de datos
        cite = CiteModel(..., id_cite=1)

        # Configura el comportamiento del objeto Mock de la sesión de la base de datos
        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = cite
        mock_db_session.delete.return_value = None
        mock_db_session.commit.return_value = None
        mock_session.return_value = mock_db_session

        # Llama a la función que deseas probar
        response = delete_cite(1)

        # Verifica el resultado esperado
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(cite))

if __name__ == '__main__':
    unittest.main()