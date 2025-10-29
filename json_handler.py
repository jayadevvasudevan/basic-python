"""
JSON Data Handler
Demonstrates working with JSON data in Python including:
- Reading and writing JSON files
- Parsing JSON strings
- Nested JSON manipulation
- Data validation
- Converting between Python objects and JSON
"""

import json
from typing import Dict, List, Any
from pathlib import Path
from datetime import datetime


class JSONHandler:
    """Class to handle various JSON operations."""
    
    @staticmethod
    def read_json_file(filepath: str) -> Dict[str, Any]:
        """
        Read and parse a JSON file.
        
        Args:
            filepath: Path to the JSON file
        
        Returns:
            Parsed JSON data as dictionary
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format - {e}")
            return {}
    
    @staticmethod
    def write_json_file(filepath: str, data: Dict[str, Any], indent: int = 2):
        """
        Write data to a JSON file.
        
        Args:
            filepath: Path to save the JSON file
            data: Dictionary to save as JSON
            indent: Number of spaces for indentation (default: 2)
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=indent, ensure_ascii=False)
            print(f"Data successfully written to '{filepath}'")
        except Exception as e:
            print(f"Error writing to file: {e}")
    
    @staticmethod
    def parse_json_string(json_string: str) -> Dict[str, Any]:
        """
        Parse a JSON string.
        
        Args:
            json_string: JSON formatted string
        
        Returns:
            Parsed data as dictionary
        """
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON string: {e}")
            return {}
    
    @staticmethod
    def to_json_string(data: Dict[str, Any], pretty: bool = True) -> str:
        """
        Convert dictionary to JSON string.
        
        Args:
            data: Dictionary to convert
            pretty: Whether to format with indentation
        
        Returns:
            JSON formatted string
        """
        if pretty:
            return json.dumps(data, indent=2, ensure_ascii=False)
        return json.dumps(data, ensure_ascii=False)
    
    @staticmethod
    def get_nested_value(data: Dict[str, Any], path: str, default=None) -> Any:
        """
        Safely get a nested value from JSON using dot notation.
        
        Args:
            data: Dictionary to search
            path: Dot-separated path (e.g., "user.address.city")
            default: Default value if path not found
        
        Returns:
            Value at the path or default
        """
        keys = path.split('.')
        current = data
        
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        
        return current
    
    @staticmethod
    def set_nested_value(data: Dict[str, Any], path: str, value: Any):
        """
        Set a nested value in JSON using dot notation.
        
        Args:
            data: Dictionary to modify
            path: Dot-separated path (e.g., "user.address.city")
            value: Value to set
        """
        keys = path.split('.')
        current = data
        
        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]
        
        current[keys[-1]] = value
    
    @staticmethod
    def merge_json(base: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deep merge two JSON objects.
        
        Args:
            base: Base dictionary
            updates: Dictionary with updates
        
        Returns:
            Merged dictionary
        """
        result = base.copy()
        
        for key, value in updates.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = JSONHandler.merge_json(result[key], value)
            else:
                result[key] = value
        
        return result


# Example usage and demonstrations
def demonstrate_json_operations():
    """Demonstrate various JSON operations."""
    
    print("=" * 70)
    print("JSON Data Handler - Demonstrations")
    print("=" * 70)
    
    # 1. Create sample data
    print("\n1. Creating Sample Data:")
    print("-" * 70)
    
    user_data = {
        "users": [
            {
                "id": 1,
                "name": "Alice Johnson",
                "email": "alice@example.com",
                "age": 28,
                "address": {
                    "street": "123 Main St",
                    "city": "New York",
                    "country": "USA"
                },
                "skills": ["Python", "JavaScript", "SQL"]
            },
            {
                "id": 2,
                "name": "Bob Smith",
                "email": "bob@example.com",
                "age": 35,
                "address": {
                    "street": "456 Oak Ave",
                    "city": "San Francisco",
                    "country": "USA"
                },
                "skills": ["Java", "C++", "Docker"]
            }
        ],
        "metadata": {
            "version": "1.0",
            "created_at": datetime.now().isoformat(),
            "total_users": 2
        }
    }
    
    print(json.dumps(user_data, indent=2))
    
    # 2. Convert to JSON string
    print("\n2. Converting to JSON String:")
    print("-" * 70)
    
    json_string = JSONHandler.to_json_string(user_data, pretty=True)
    print(json_string[:200] + "...")
    
    # 3. Parse JSON string
    print("\n3. Parsing JSON String:")
    print("-" * 70)
    
    parsed_data = JSONHandler.parse_json_string(json_string)
    print(f"Parsed {len(parsed_data['users'])} users")
    
    # 4. Access nested values
    print("\n4. Accessing Nested Values:")
    print("-" * 70)
    
    city = JSONHandler.get_nested_value(user_data, "users.0.address.city")
    print(f"First user's city: {city}")
    
    version = JSONHandler.get_nested_value(user_data, "metadata.version")
    print(f"Data version: {version}")
    
    # 5. Set nested values
    print("\n5. Setting Nested Values:")
    print("-" * 70)
    
    JSONHandler.set_nested_value(user_data, "users.0.address.zipcode", "10001")
    print(f"Added zipcode: {user_data['users'][0]['address']['zipcode']}")
    
    # 6. Merge JSON objects
    print("\n6. Merging JSON Objects:")
    print("-" * 70)
    
    updates = {
        "users": [
            {
                "id": 1,
                "phone": "+1-555-0123",
                "address": {
                    "zipcode": "10002"
                }
            }
        ],
        "metadata": {
            "updated_at": datetime.now().isoformat()
        }
    }
    
    merged = JSONHandler.merge_json(user_data, updates)
    print(json.dumps(merged["users"][0], indent=2))
    
    # 7. Filter and transform data
    print("\n7. Filtering and Transforming Data:")
    print("-" * 70)
    
    # Extract only names and emails
    user_summary = [
        {"name": user["name"], "email": user["email"]}
        for user in user_data["users"]
    ]
    print(json.dumps(user_summary, indent=2))
    
    # 8. Validate data
    print("\n8. Data Validation:")
    print("-" * 70)
    
    def validate_user(user: Dict[str, Any]) -> bool:
        """Validate user data structure."""
        required_fields = ["id", "name", "email", "age"]
        return all(field in user for field in required_fields)
    
    for user in user_data["users"]:
        is_valid = validate_user(user)
        print(f"User {user['name']}: {'✓ Valid' if is_valid else '✗ Invalid'}")
    
    # 9. Working with file operations (example only - not actually writing)
    print("\n9. File Operations (Example):")
    print("-" * 70)
    print("To save to file: JSONHandler.write_json_file('users.json', user_data)")
    print("To load from file: data = JSONHandler.read_json_file('users.json')")
    
    # 10. Pretty print JSON
    print("\n10. Pretty Print Comparison:")
    print("-" * 70)
    
    compact = JSONHandler.to_json_string({"name": "Alice", "age": 28}, pretty=False)
    print(f"Compact: {compact}")
    
    pretty = JSONHandler.to_json_string({"name": "Alice", "age": 28}, pretty=True)
    print(f"Pretty:\n{pretty}")


if __name__ == "__main__":
    demonstrate_json_operations()
