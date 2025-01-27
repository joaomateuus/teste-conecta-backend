class GoogleAPIError(Exception):
    def __init__(self, status_code, message, details=None):
        self.status_code = status_code
        self.message = message
        self.details = details
        super().__init__(self.message)
    
    def __str__(self):
        return f"Google API Error (Status Code: {self.status_code}): {self.message} - Details: {self.details}"
    
    @classmethod
    def from_api_response(cls, response):
        """Método de classe para criar uma instância de GoogleAPIError a partir de uma resposta da API"""
        status_code = response.status_code
        try:
            error_data = response.json()
            message = error_data.get('error', {}).get('message', 'Unknown error')
            details = error_data.get('error', {}).get('details', 'No additional details')
        except ValueError:  # Se a resposta não for JSON ou estiver malformada
            message = 'Malformed response from Google API'
            details = str(response.text)
        
        return cls(status_code, message, details)