"""
Regular Expressions (Regex) Guide
Comprehensive examples of pattern matching and text processing with regex.
Covers common use cases: validation, extraction, substitution, and more.
"""

import re
from typing import List, Tuple, Optional, Dict


class RegexPatterns:
    """Collection of commonly used regex patterns."""
    
    # Email validation
    EMAIL = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Phone number (US format)
    PHONE_US = r'^\+?1?\s*\(?(\d{3})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})$'
    
    # URL validation
    URL = r'^https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)$'
    
    # IP Address (IPv4)
    IP_ADDRESS = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    
    # Date (YYYY-MM-DD)
    DATE_ISO = r'^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])$'
    
    # Credit Card (basic validation)
    CREDIT_CARD = r'^(?:\d{4}[\s-]?){3}\d{4}$'
    
    # Password (8+ chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char)
    PASSWORD_STRONG = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    # Username (alphanumeric, underscore, 3-16 chars)
    USERNAME = r'^[a-zA-Z0-9_]{3,16}$'
    
    # Hexadecimal color code
    HEX_COLOR = r'^#?([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    
    # HTML tag
    HTML_TAG = r'<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)'


class RegexUtility:
    """Utility class for common regex operations."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate email address format.
        
        Args:
            email: Email address to validate
        
        Returns:
            True if valid, False otherwise
        """
        return bool(re.match(RegexPatterns.EMAIL, email))
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        Validate US phone number format.
        
        Args:
            phone: Phone number to validate
        
        Returns:
            True if valid, False otherwise
        """
        return bool(re.match(RegexPatterns.PHONE_US, phone))
    
    @staticmethod
    def extract_emails(text: str) -> List[str]:
        """
        Extract all email addresses from text.
        
        Args:
            text: Text to search
        
        Returns:
            List of email addresses found
        """
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_urls(text: str) -> List[str]:
        """
        Extract all URLs from text.
        
        Args:
            text: Text to search
        
        Returns:
            List of URLs found
        """
        pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_phone_numbers(text: str) -> List[str]:
        """
        Extract phone numbers from text.
        
        Args:
            text: Text to search
        
        Returns:
            List of phone numbers found
        """
        # More flexible pattern for extraction
        pattern = r'\+?1?\s*\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_dates(text: str) -> List[str]:
        """
        Extract dates in various formats from text.
        
        Args:
            text: Text to search
        
        Returns:
            List of dates found
        """
        patterns = [
            r'\d{4}-\d{2}-\d{2}',  # YYYY-MM-DD
            r'\d{2}/\d{2}/\d{4}',  # MM/DD/YYYY
            r'\d{2}-\d{2}-\d{4}',  # MM-DD-YYYY
        ]
        
        dates = []
        for pattern in patterns:
            dates.extend(re.findall(pattern, text))
        
        return dates
    
    @staticmethod
    def mask_credit_card(text: str) -> str:
        """
        Mask credit card numbers in text.
        
        Args:
            text: Text containing credit card numbers
        
        Returns:
            Text with masked credit card numbers
        """
        pattern = r'\b(\d{4})[\s-]?(\d{4})[\s-]?(\d{4})[\s-]?(\d{4})\b'
        return re.sub(pattern, r'****-****-****-\4', text)
    
    @staticmethod
    def remove_html_tags(text: str) -> str:
        """
        Remove all HTML tags from text.
        
        Args:
            text: HTML text
        
        Returns:
            Text without HTML tags
        """
        pattern = r'<[^>]+>'
        return re.sub(pattern, '', text)
    
    @staticmethod
    def clean_whitespace(text: str) -> str:
        """
        Replace multiple whitespace with single space and trim.
        
        Args:
            text: Text to clean
        
        Returns:
            Cleaned text
        """
        # Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text)
        # Trim leading and trailing whitespace
        return text.strip()
    
    @staticmethod
    def camel_to_snake(text: str) -> str:
        """
        Convert camelCase to snake_case.
        
        Args:
            text: CamelCase text
        
        Returns:
            snake_case text
        """
        # Insert underscore before uppercase letters
        text = re.sub(r'(?<!^)(?=[A-Z])', '_', text)
        return text.lower()
    
    @staticmethod
    def snake_to_camel(text: str) -> str:
        """
        Convert snake_case to camelCase.
        
        Args:
            text: snake_case text
        
        Returns:
            camelCase text
        """
        components = text.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
    
    @staticmethod
    def find_and_replace(text: str, pattern: str, replacement: str, 
                         case_insensitive: bool = False) -> str:
        """
        Find and replace text using regex.
        
        Args:
            text: Text to search
            pattern: Regex pattern to find
            replacement: Replacement string
            case_insensitive: Whether to ignore case
        
        Returns:
            Text with replacements
        """
        flags = re.IGNORECASE if case_insensitive else 0
        return re.sub(pattern, replacement, text, flags=flags)
    
    @staticmethod
    def extract_hashtags(text: str) -> List[str]:
        """
        Extract hashtags from text (like in social media).
        
        Args:
            text: Text to search
        
        Returns:
            List of hashtags found
        """
        pattern = r'#\w+'
        return re.findall(pattern, text)
    
    @staticmethod
    def extract_mentions(text: str) -> List[str]:
        """
        Extract @mentions from text.
        
        Args:
            text: Text to search
        
        Returns:
            List of mentions found
        """
        pattern = r'@\w+'
        return re.findall(pattern, text)
    
    @staticmethod
    def split_by_delimiter(text: str, delimiter_pattern: str = r'[,;]') -> List[str]:
        """
        Split text by regex pattern delimiter.
        
        Args:
            text: Text to split
            delimiter_pattern: Regex pattern for delimiter
        
        Returns:
            List of split parts
        """
        parts = re.split(delimiter_pattern, text)
        return [part.strip() for part in parts if part.strip()]


# Demonstration functions
def demonstrate_validation():
    """Demonstrate validation patterns."""
    print("=" * 70)
    print("1. VALIDATION PATTERNS")
    print("=" * 70)
    
    # Email validation
    emails = [
        "user@example.com",
        "invalid.email@",
        "test.user+tag@domain.co.uk",
        "not-an-email"
    ]
    
    print("\nEmail Validation:")
    for email in emails:
        is_valid = RegexUtility.validate_email(email)
        print(f"  {email:30} → {'✓ Valid' if is_valid else '✗ Invalid'}")
    
    # Phone validation
    phones = [
        "(555) 123-4567",
        "555-123-4567",
        "5551234567",
        "+1 (555) 123-4567",
        "123-456"
    ]
    
    print("\nPhone Number Validation:")
    for phone in phones:
        is_valid = RegexUtility.validate_phone(phone)
        print(f"  {phone:25} → {'✓ Valid' if is_valid else '✗ Invalid'}")


def demonstrate_extraction():
    """Demonstrate extraction patterns."""
    print("\n" + "=" * 70)
    print("2. EXTRACTION PATTERNS")
    print("=" * 70)
    
    sample_text = """
    Contact us at support@example.com or sales@company.org.
    Visit our website: https://www.example.com and https://docs.example.com/api
    Call us: (555) 123-4567 or 555-987-6543
    Important dates: 2024-01-15, 03/20/2024, and 12-31-2024
    Follow us: @company #python #coding #tech
    """
    
    print("\nSample Text:")
    print(sample_text)
    
    print("\nExtracted Emails:")
    emails = RegexUtility.extract_emails(sample_text)
    for email in emails:
        print(f"  • {email}")
    
    print("\nExtracted URLs:")
    urls = RegexUtility.extract_urls(sample_text)
    for url in urls:
        print(f"  • {url}")
    
    print("\nExtracted Phone Numbers:")
    phones = RegexUtility.extract_phone_numbers(sample_text)
    for phone in phones:
        print(f"  • {phone}")
    
    print("\nExtracted Dates:")
    dates = RegexUtility.extract_dates(sample_text)
    for date in dates:
        print(f"  • {date}")
    
    print("\nExtracted Hashtags:")
    hashtags = RegexUtility.extract_hashtags(sample_text)
    for tag in hashtags:
        print(f"  • {tag}")
    
    print("\nExtracted Mentions:")
    mentions = RegexUtility.extract_mentions(sample_text)
    for mention in mentions:
        print(f"  • {mention}")


def demonstrate_substitution():
    """Demonstrate substitution patterns."""
    print("\n" + "=" * 70)
    print("3. SUBSTITUTION PATTERNS")
    print("=" * 70)
    
    # Mask credit card
    text_with_cc = "Card number: 1234-5678-9012-3456"
    masked = RegexUtility.mask_credit_card(text_with_cc)
    print(f"\nCredit Card Masking:")
    print(f"  Original: {text_with_cc}")
    print(f"  Masked:   {masked}")
    
    # Remove HTML tags
    html_text = "<p>This is <b>bold</b> and <i>italic</i> text.</p>"
    clean_text = RegexUtility.remove_html_tags(html_text)
    print(f"\nHTML Tag Removal:")
    print(f"  Original: {html_text}")
    print(f"  Cleaned:  {clean_text}")
    
    # Clean whitespace
    messy_text = "  Too    many    spaces   here  "
    clean = RegexUtility.clean_whitespace(messy_text)
    print(f"\nWhitespace Cleaning:")
    print(f"  Original: '{messy_text}'")
    print(f"  Cleaned:  '{clean}'")
    
    # Case conversion
    camel = "myVariableName"
    snake = RegexUtility.camel_to_snake(camel)
    back_to_camel = RegexUtility.snake_to_camel(snake)
    print(f"\nCase Conversion:")
    print(f"  Camel: {camel}")
    print(f"  Snake: {snake}")
    print(f"  Back:  {back_to_camel}")


def demonstrate_advanced_patterns():
    """Demonstrate advanced regex patterns."""
    print("\n" + "=" * 70)
    print("4. ADVANCED PATTERNS")
    print("=" * 70)
    
    # Lookahead and lookbehind
    text = "Price: $100 and €50"
    
    # Find numbers preceded by $
    dollar_amounts = re.findall(r'(?<=\$)\d+', text)
    print(f"\nDollar amounts: {dollar_amounts}")
    
    # Find numbers preceded by €
    euro_amounts = re.findall(r'(?<=€)\d+', text)
    print(f"Euro amounts: {euro_amounts}")
    
    # Named groups
    pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
    date_text = "Date: 2024-03-15"
    match = re.search(pattern, date_text)
    
    if match:
        print(f"\nNamed Groups from '{date_text}':")
        print(f"  Year:  {match.group('year')}")
        print(f"  Month: {match.group('month')}")
        print(f"  Day:   {match.group('day')}")
    
    # Split by multiple delimiters
    csv_like = "apple, banana; orange, grape; kiwi"
    items = RegexUtility.split_by_delimiter(csv_like)
    print(f"\nSplit '{csv_like}':")
    print(f"  Items: {items}")


if __name__ == "__main__":
    demonstrate_validation()
    demonstrate_extraction()
    demonstrate_substitution()
    demonstrate_advanced_patterns()
