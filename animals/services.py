from django.conf import settings
from pymongo import MongoClient
import logging

logger = logging.getLogger('animals')

class DatabaseConnection:
    """Classe para gerenciar conexão MongoDB"""
    _client = None
    _database = None
    
    @classmethod
    def get_database(cls):
        if cls._database is None:
            try:
                mongo_config = settings.MONGODB
                cls._client = MongoClient(
                    host=mongo_config['HOST'],
                    port=mongo_config['PORT'],
                    username=mongo_config['USERNAME'],
                    password=mongo_config['PASSWORD'],
                    authSource="admin",
                    serverSelectionTimeoutMS=5000,
                )
                # Testa a conexão
                cls._client.admin.command('ping')
                cls._database = cls._client[mongo_config['DATABASE']]
                logger.info("Conexão MongoDB estabelecida")
            except Exception as e:
                logger.error(f"Erro ao conectar MongoDB: {e}")
                raise
        return cls._database

class AnimalService:
    """Serviço para operações com animais"""
    
    def __init__(self):
        self.db = DatabaseConnection.get_database()
        self.collection = self.db.animal_tb
    
    def get_all_animals(self):
        """Busca todos os animais"""
        try:
            cursor = self.collection.find()
            animals = [
                {
                    "id": animal["id"],
                    "name": animal["name"],
                    "type": animal["type"]
                }
                for animal in cursor
            ]
            logger.info(f"Buscados {len(animals)} animais")
            return animals
        except Exception as e:
            logger.error(f"Erro ao buscar animais: {e}")
            raise
    
    def get_animals_by_type(self, animal_type):
        """Busca animais por tipo"""
        try:
            cursor = self.collection.find({"type": animal_type})
            animals = [
                {
                    "id": animal["id"],
                    "name": animal["name"],
                    "type": animal["type"]
                }
                for animal in cursor
            ]
            logger.info(f"Buscados {len(animals)} animais do tipo {animal_type}")
            return animals
        except Exception as e:
            logger.error(f"Erro ao buscar animais do tipo {animal_type}: {e}")
            raise