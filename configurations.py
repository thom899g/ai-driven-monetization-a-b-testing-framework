class Configuration:
    def __init__(self):
        self.api_keys = {}
        self.experiment_settings = {}
    
    def get_api_key(self, service_name: str) -> str:
        """Retrieves API key for a specified service.
        
        Args:
            service_name: Name of the service.
            
        Returns:
            API key as string. Raises KeyError if not found.
        """
        return self.api_keys[service_name]
    
    def set_experiment_settings(self, settings: Dict):
        """Updates experiment configuration parameters.
        
        Args:
            settings: Dictionary with new experiment settings.
        """
        self.experiment_settings.update(settings)