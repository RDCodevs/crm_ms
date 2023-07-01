import unittest
from unittest.mock import patch, MagicMock

from src.config.database import Session
from src.models.cites import Cites as CiteModel
from src.schemas.cites import Cites, UpdateCite
from fastapi.responses import JSONResponse
from fastapi import status

def get_all_cites():
    db = Session()
    res = db.query(CiteModel).all()

    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(res))

class TestCiteFunctions(unittest.TestCase):
    @patch('src.config.database.Session')
    def test_get_all_cites(self, mock_session):

        cite1 = CiteModel(id_cite=1, ...)
        cite2 = CiteModel(id_cite=2, ...)
        

        mock_db_session = MagicMock()
        mock_db_session.query.return_value.all.return_value = [cite1, cite2]
        mock_session.return_value = mock_db_session


        response = get_all_cites()


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder([cite1, cite2]))

    @patch('src.config.database.Session')
    def test_get_cite_by_id(self, mock_session):
 
        cite = CiteModel(id_cite=1, ...)
        

        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = cite
        mock_session.return_value = mock_db_session


        response = get_cite_by_id(1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(cite))

    @patch('src.config.database.Session')
    def test_get_cite_by_patient_id(self, mock_session):

        cite = CiteModel(id_cite=1, ...)
        

        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = cite
        mock_session.return_value = mock_db_session

   
        response = get_cite_by_patient_id(1)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(cite))

    @patch('src.config.database.Session')
    def test_get_cites_by_medic_id(self, mock_session):

        cite1 = CiteModel(id_cite=1, ...)
        cite2 = CiteModel(id_cite=2, ...)

        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.all.return_value = [cite1, cite2]
        mock_session.return_value = mock_db_session

 
        response = get_cites_by_medic_id(1)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder([cite1, cite2]))

    @patch('src.config.database.Session')
    def test_create_cite(self, mock_session):
 
        new_cite = Cites(id_cite=1, ...)
        

        mock_db_session = MagicMock()
        mock_db_session.add.return_value = None
        mock_db_session.commit.return_value = None
        mock_session.return_value = mock_db_session

  
        response = create_cite(new_cite)

  
        self.assertEqual(response, new_cite.dict())

    @patch('src.config.database.Session')
    def test_patch_cite(self, mock_session):

        cite = CiteModel(id_cite=1, ...)

        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = cite
        mock_db_session.add.return_value = None
        mock_db_session.commit.return_value = None
        mock_db_session.refresh.return_value = None
        mock_session.return_value = mock_db_session


        updated_cite = UpdateCite(id_cite=1, ...)
        
        response = patch_cite(updated_cite)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(cite))

    @patch('src.config.database.Session')
    def test_delete_cite(self, mock_session):

        cite = CiteModel(id_cite=1, ...)
        

        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = cite
        mock_db_session.delete.return_value = None
        mock_db_session.commit.return_value = None
        mock_session.return_value = mock_db_session


        response = delete_cite(1)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(cite))

if __name__ == '__main__':
    unittest.main()