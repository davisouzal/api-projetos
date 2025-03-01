from rest_framework import status

class NotFoundException(Exception):
    def __init__(self, instance, status=status.HTTP_404_NOT_FOUND):
        self.status = status
        self.message = f"{instance} não encontrado"
        super().__init__(self.message)

class ValidationException(Exception):
    def __init__(self, instance, errors, status=status.HTTP_400_BAD_REQUEST):
        self.status = status
        self.errors = errors
        self.message = f"Erro ao validar {instance}"
        super().__init__(self.message)

class DatabaseException(Exception):
    def __init__(self, message="Erro no banco de dados", status=status.HTTP_500_INTERNAL_SERVER_ERROR):
        self.status = status
        self.message = message
        super().__init__(self.message)
