"""Configuration management for the Research and Preparation Agent."""

import os
import yaml
from typing import Dict, Any, Optional


class ConfigManager:
    """Manages configuration for the Research and Preparation Agent."""

    def __init__(self, config_path: Optional[str] = None):
        """Initialize the configuration manager.
        
        Args:
            config_path: Path to the configuration file. If None, uses default.
        """
        self.config_path = config_path or os.path.join(
            os.path.expanduser("~"), ".research_prep_agent", "config.yaml"
        )
        self.config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file.
        
        Returns:
            Dictionary containing configuration values.
        """
        if not os.path.exists(self.config_path):
            return self._create_default_config()
            
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)
            
    def _create_default_config(self) -> Dict[str, Any]:
        """Create a default configuration.
        
        Returns:
            Dictionary containing default configuration values.
        """
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        
        default_config = {
            "user_profile": {
                "name": "Sam",
                "email": "samstar2809@gmail.com",
                "phone": "9715665066",
                "location": "Chennai, TamilNadu",
                "education": [
                    {
                        "degree": "Bachelor's Degree",
                        "field": "Computer Science",
                        "institution": "SRM University",
                        "year": 2020
                    }
                ],
                "skills": [
                    "Python", "Data Analysis", "Machine Learning"
                ],
                "experience": [
                    {
                        "title": "Software Developer",
                        "company": "Zoho",
                        "start_date": "2020-01",
                        "end_date": "2023-01",
                        "description": "Developed and maintained applications..."
                    }
                ]
            },
            "job_search": {
                "keywords": ["software developer", "python developer"],
                "locations": ["Remote", "New York, NY"],
                "exclude_keywords": ["senior", "lead"],
                "job_boards": ["linkedin", "indeed"],
                "refresh_interval_hours": 24
            },
            "credentials": {
                "linkedin": {
                    "username": "",
                    "password": ""
                },
                "indeed": {
                    "api_key": ""
                },
                "openai": {
                    "api_key": ""
                }
            },
            "output": {
                "resume_template": "modern",
                "cover_letter_template": "professional",
                "output_directory": "~/Documents/JobApplications"
            }
        }
        
        # Save default config
        with open(self.config_path, "w") as f:
            yaml.dump(default_config, f, default_flow_style=False)
            
        return default_config
        
    def get_config(self) -> Dict[str, Any]:
        """Get the full configuration.
        
        Returns:
            Dictionary containing configuration values.
        """
        return self.config
        
    def get_user_profile(self) -> Dict[str, Any]:
        """Get the user profile configuration.
        
        Returns:
            Dictionary containing user profile.
        """
        return self.config.get("user_profile", {})
        
    def get_job_search_config(self) -> Dict[str, Any]:
        """Get the job search configuration.
        
        Returns:
            Dictionary containing job search settings.
        """
        return self.config.get("job_search", {})
        
    def get_credentials(self, service: str) -> Dict[str, str]:
        """Get credentials for a specific service.
        
        Args:
            service: Name of the service (e.g., "linkedin", "indeed").
            
        Returns:
            Dictionary containing credentials for the service.
        """
        return self.config.get("credentials", {}).get(service, {})
        
    def update_config(self, config: Dict[str, Any]) -> None:
        """Update the configuration.
        
        Args:
            config: Dictionary containing new configuration values.
        """
        self.config.update(config)
        self._save_config()
        
    def _save_config(self) -> None:
        """Save the configuration to file."""
        with open(self.config_path, "w") as f:
            yaml.dump(self.config, f, default_flow_style=False)


# Create a singleton instance
config_manager = ConfigManager()