"""Base class for MCP implementations."""


class BaseMCP:
    """
    Base class for Model Context Protocol tools.
    
    All MCP implementations should inherit from this class and implement
    the required abstract methods.
    """
    
    def __init__(self, credentials_path=None):
        """
        Initialize the MCP with optional credentials.
        
        Args:
            credentials_path (str, optional): Path to credentials file
        """
        self.credentials_path = credentials_path
        self.authenticated = False
        self.client = None
    
    def authenticate(self):
        """
        Authenticate with the external service.
        
        This method should handle OAuth flows, API key validation,
        or other authentication mechanisms.
        
        Returns:
            bool: True if authentication successful, False otherwise
            
        Raises:
            NotImplementedError: Must be implemented by subclass
        """
        raise NotImplementedError(
            "Subclasses must implement authenticate() method"
        )
    
    def execute(self, action, params):
        """
        Execute an MCP action.
        
        This is a generic method for executing service-specific actions.
        Subclasses should implement specific methods for their actions
        and use this as a fallback or router.
        
        Args:
            action (str): The action to perform
            params (dict): Parameters for the action
            
        Returns:
            dict: Result of the action
            
        Raises:
            NotImplementedError: Must be implemented by subclass
        """
        raise NotImplementedError(
            "Subclasses must implement execute() method"
        )
    
    def is_authenticated(self):
        """
        Check if the MCP is currently authenticated.
        
        Returns:
            bool: True if authenticated, False otherwise
        """
        return self.authenticated
    
    def _ensure_authenticated(self):
        """
        Ensure the MCP is authenticated before performing operations.
        
        Raises:
            RuntimeError: If not authenticated
        """
        if not self.authenticated:
            raise RuntimeError(
                f"{self.__class__.__name__} is not authenticated. "
                "Call authenticate() first."
            )
