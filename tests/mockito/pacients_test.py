import unittest
from unittest.mock import patch, MagicMock

from src.config.database import Session
from src.models.pacients import Pacient as PacientModel
from src.schemas.pacients import Pacient, UpdatePacient
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder
from src.services.pacients import get_all_pacient, create_pacient, patch_pacient, delete_pacient
#-------------------------------------------------------
def get_pacient(pacient_id: int):
    db = Session()
    res = db.query(PacientModel).filter(PacientModel.id_pacient == pacient_id).first()

    if not res:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Pacient not Found"})

    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(res))

class TestPacientFunctions(unittest.TestCase):

    pacient = {
        "name": "Stalin",
        "lastname": "Pillajo",
        "gender": "Male",
        "weight": 17.05,
        "height": 1.72,
        "ethnicity": "Indigena",
        "allergies": "None",
        "HTA": 110, 
        "cie_code": 123456,
        "birthday": "2001-12-07",    
        "blood_type": "O+",
        "address": "Jesus del Gran Poder, Cojimies y Colambo",
        "phone": "0961800096"
    }

    @patch('src.config.database.Session')
    def test_get_pacient(self, mock_session):

        pacient = PacientModel(**self.pacient)

        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first = pacient
        mock_session.return_value = mock_db_session

        response = get_pacient(1)
      
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(pacient))

    @patch('src.config.database.Session')
    def test_get_all_pacient(self, mock_session):
  
        pacient1 = PacientModel(**self.pacient)
        pacient2 = PacientModel(**self.pacient)
        
  
        mock_db_session = MagicMock()
        mock_db_session.query.return_value.all.return_value = [pacient1, pacient2]
        mock_session.return_value = mock_db_session


        response = get_all_pacient()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder([pacient1, pacient2]))

    @patch('src.config.database.Session')
    def test_create_pacient(self, mock_session):

        new_pacient = PacientModel(**self.pacient)
        
        mock_db_session = MagicMock()
        mock_db_session.add.return_value = None
        mock_db_session.commit.return_value = None
        mock_session.return_value = mock_db_session

     
        response = create_pacient(new_pacient)
  
        self.assertEqual(response, new_pacient)

    @patch('src.config.database.Session')
    def test_patch_pacient(self, mock_session):
  
        pacient = Pacient(**self.pacient)
        

        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = pacient
        mock_db_session.add.return_value = None
        mock_db_session.commit.return_value = None
        mock_db_session.refresh.return_value = None
        mock_session.return_value = mock_db_session

        updated_pacient = UpdatePacient(**self.pacient)

        response = patch_pacient(updated_pacient)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(pacient))

    @patch('src.config.database.Session')
    def test_delete_pacient(self, mock_session):
 
        pacient = PacientModel(**self.pacient)

        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = pacient
        mock_db_session.delete.return_value = None
        mock_db_session.commit.return_value = None
        mock_session.return_value = mock_db_session

      
        response = delete_pacient(1)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(pacient))

if __name__ == '__main__':
    unittest.main()
