import unittest
from unittest.mock import patch, MagicMock
from src.config.database import Session
from src.models.medic import Medic as MedicModel
from src.schemas.medic import Medic, UpdateMedic
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder
from src.services.medic import get_all_medic, create_medic, patch_medic
#-------------------------------------------------------
def get_medic(medic_id: int):
    db = Session()
    res = db.query(MedicModel).filter(MedicModel.id_medic == medic_id).first()

    if not res:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Medic not Found"})

    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(res))

class TestMedicFunctions(unittest.TestCase):
    @patch('src.config.database.Session')
    def test_get_medic(self, mock_session):
        medic = MedicModel( ..., id_medic=1)
        
        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = medic
        mock_session.return_value = mock_db_session

        response = get_medic(1)

 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(medic))

    @patch('src.config.database.Session')
    def test_get_all_medic(self, mock_session):

        medic1 = MedicModel(..., id_medic=1)
        medic2 = MedicModel(..., id_medic=2)
        
        mock_db_session = MagicMock()
        mock_db_session.query.return_value.all.return_value = [medic1, medic2]
        mock_session.return_value = mock_db_session

        response = get_all_medic()
 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder([medic1, medic2]))

    @patch('src.config.database.Session')
    def test_create_medic(self, mock_session):

        new_medic = Medic(..., id_medic=1)
        
  
        mock_db_session = MagicMock()
        mock_db_session.add.return_value = None
        mock_db_session.commit.return_value = None
        mock_session.return_value = mock_db_session

        response = create_medic(new_medic)

        self.assertEqual(response, new_medic.dict())

    @patch('src.config.database.Session')
    def test_patch_medic(self, mock_session):

        medic = MedicModel(..., id_medic=1)
        
        mock_db_session = MagicMock()
        mock_db_session.query.return_value.filter.return_value.first.return_value = medic
        mock_db_session.add.return_value = None
        mock_db_session.commit.return_value = None
        mock_db_session.refresh.return_value = None
        mock_session.return_value = mock_db_session


        updated_medic = UpdateMedic(..., id=1)
        
        response = patch_medic(updated_medic)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, jsonable_encoder(medic))

if __name__ == '__main__':
    unittest.main()
