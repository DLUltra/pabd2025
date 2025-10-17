# Modulo de conecção com o Supabase
import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Carregando as variaveis de ambiente
load_dotenv()

class SupabaseConnection:
    '''Padrão de projeto - Singleton 
    * Ganante apenas uma instancia em toda a aplicação
    '''

    _instance = None
    # type hint - garante o tipo de dado a ser atribuido a um atributo/variavel
    _client: Client = None

# new - cria uma instancia da classe
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SupabaseConnection, cls).__new__(cls)
            cls.instance._init_conenection()
        return cls._instance
    
    def _init_conenection(self):
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_KEY')

        if not supabase_url or not supabase_key:
            raise ValueError('Erro nas variaveis de ambiente!')

        self._client = create_client(supabase_url, supabase_key)
        print('Conexão com o Supabase OK!')

    @property
    def client(self) -> Client: # type hint
        return self._client