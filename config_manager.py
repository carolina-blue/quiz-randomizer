import yaml
import os
from typing import Dict, Any, List

class ConfigManager:
    """Manages configuration settings for the Quiz Randomizer application."""
    
    def __init__(self, config_file: str = "config.yaml"):
        self.config_file = config_file
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create with defaults if not exists."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return yaml.safe_load(f)
        return self._create_default_config()
    
    def _create_default_config(self) -> Dict[str, Any]:
        """Create default configuration."""
        default_config = {
            "gui": {
                "window_width": 600,
                "window_height": 500,
                "title": "Quiz Randomizer"
            },
            "quiz_defaults": {
                "num_quizzes": 5,
                "questions_per_quiz": 10,
                "allow_duplicates": False,
                "output_format": "docx",
                "output_directory": "quizzes"
            },
            "formatting": {
                "pdf": {
                    "title_font": "Arial",
                    "title_size": 16,
                    "body_font": "Arial",
                    "body_size": 12,
                    "feedback_size": 10,
                    "margins": {
                        "top": 20,
                        "bottom": 20,
                        "left": 20,
                        "right": 20
                    }
                },
                "docx": {
                    "title_size": 16,
                    "option_indent": 20,
                    "feedback_indent": 20
                }
            },
            "file_types": [
                {"name": "Text Files", "extensions": [".txt"]},
                {"name": "Word Documents", "extensions": [".docx"]},
                {"name": "Rich Text Format", "extensions": [".rtf"]},
                {"name": "All Files", "extensions": [".*"]}
            ],
            "recent_files": []
        }
        self.save_config(default_config)
        return default_config
    
    def save_config(self, config: Dict[str, Any] = None) -> None:
        """Save current configuration to file."""
        if config is not None:
            self.config = config
        with open(self.config_file, 'w') as f:
            yaml.dump(self.config, f, default_flow_style=False)
    
    def get_setting(self, *keys: str) -> Any:
        """Get a setting value using nested keys."""
        value = self.config
        for key in keys:
            value = value.get(key)
            if value is None:
                return None
        return value
    
    def set_setting(self, value: Any, *keys: str) -> None:
        """Set a setting value using nested keys."""
        config = self.config
        for key in keys[:-1]:
            config = config.setdefault(key, {})
        config[keys[-1]] = value
        self.save_config()
    
    def add_recent_file(self, filepath: str) -> None:
        """Add a file to recent files list."""
        recent_files = self.get_setting("recent_files")
        if filepath in recent_files:
            recent_files.remove(filepath)
        recent_files.insert(0, filepath)
        # Keep only last 5 files
        self.set_setting(recent_files[:5], "recent_files")
    
    def get_file_types(self) -> List[tuple]:
        """Get file types in format suitable for tkinter filedialog."""
        file_types = self.get_setting("file_types")
        return [(ft["name"], "*" + " *".join(ft["extensions"])) for ft in file_types] 