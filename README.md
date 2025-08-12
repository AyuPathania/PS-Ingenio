# Appium Test Automation Project

This project provides a comprehensive test automation framework for testing both User and Advisor applications across multiple platforms (Android, iOS, and Web) using Appium with Python.

## Project Structure

```
Ingenio/
├── config/                     # Configuration files
│   ├── __init__.py
│   └── config.py              # Central configuration management
├── core/                       # Core Appium functionality
│   ├── __init__.py
│   └── appium_driver.py       # Centralized Appium driver with all methods
├── locators/                   # Element locators organized by user type and platform
│   ├── __init__.py
│   ├── user/                   # User app locators
│   │   ├── __init__.py
│   │   ├── android_locators.py
│   │   ├── ios_locators.py
│   │   └── web_locators.py
│   └── advisor/                # Advisor app locators
│       ├── __init__.py
│       ├── android_locators.py
│       ├── ios_locators.py
│       └── web_locators.py
├── tests/                      # Test cases organized by user type
│   ├── __init__.py
│   ├── conftest.py            # Pytest configuration and fixtures
│   ├── user/                   # User app tests
│   │   ├── __init__.py
│   │   └── test_user_login.py
│   └── advisor/                # Advisor app tests
│       ├── __init__.py
│       └── test_advisor_login.py
├── requirements.txt            # Python dependencies
├── pytest.ini                 # Pytest configuration
├── env.example                # Environment variables template
└── README.md                  # This file
```

## Features

- **Multi-platform Support**: Android, iOS, and Web testing
- **User Type Separation**: Separate locators and tests for User and Advisor applications
- **Centralized Driver**: All Appium methods available in one place
- **Organized Locators**: Platform-specific locators for each user type
- **Pytest Integration**: Modern testing framework with fixtures and markers
- **Configuration Management**: Environment-based configuration
- **Comprehensive Testing**: Login, navigation, and functionality tests

## Prerequisites

- Python 3.8+
- Appium Server
- Android SDK (for Android testing)
- Xcode (for iOS testing)
- Chrome/WebDriver (for web testing)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Ingenio
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy environment template:
```bash
cp env.example .env
```

4. Update `.env` file with your configuration

## Configuration

The project uses a centralized configuration system in `config/config.py`:

- **Appium Server**: Host, port, and capabilities
- **Platform Settings**: Android, iOS, and Web specific configurations
- **App Configurations**: Separate settings for User and Advisor apps
- **Test Settings**: Timeouts, screenshot directories, etc.

## Usage

### Running Tests

1. **All Tests**:
```bash
pytest
```

2. **Platform-specific Tests**:
```bash
pytest -m android    # Android tests only
pytest -m ios        # iOS tests only
pytest -m web        # Web tests only
```

3. **User Type Tests**:
```bash
pytest -m user       # User app tests only
pytest -m advisor    # Advisor app tests only
```

4. **Specific Test File**:
```bash
pytest tests/user/test_user_login.py
```

5. **Parallel Execution**:
```bash
pytest -n auto
```

### Test Organization

Tests are organized by:
- **User Type**: User vs Advisor
- **Platform**: Android, iOS, Web
- **Functionality**: Login, Navigation, etc.

### Locators

Locators are organized by:
- **User Type**: Separate locator classes for User and Advisor
- **Platform**: Platform-specific locator strategies
- **Functionality**: Grouped by screen/feature

## Centralized Appium Driver

The `core/appium_driver.py` provides a comprehensive set of methods:

### Element Finding
- `find_element()`: Find single element with explicit wait
- `find_elements()`: Find multiple elements
- Platform-specific text finding methods

### Interaction Methods
- `click()`: Click on elements
- `input_text()`: Input text into fields
- `clear_text()`: Clear text fields
- `swipe()`: Swipe gestures

### Wait Methods
- `wait_for_element()`: Wait for element presence
- `wait_for_element_visible()`: Wait for element visibility
- `wait_for_element_clickable()`: Wait for element to be clickable

### Utility Methods
- `take_screenshot()`: Capture screenshots
- `is_element_present()`: Check element existence
- `get_element_text()`: Get element text

## Adding New Tests

1. **Create Locators**: Add new locators to appropriate locator files
2. **Create Test Class**: Create new test class in appropriate test directory
3. **Use Fixtures**: Use provided fixtures for different platforms and user types
4. **Follow Naming**: Use descriptive test method names

Example:
```python
def test_user_profile_edit_android(self, android_user_driver):
    """Test user profile editing on Android"""
    driver = android_user_driver
    locators = UserAndroidLocators()
    
    # Test implementation
    pass
```

## Best Practices

1. **Use Fixtures**: Leverage pytest fixtures for driver management
2. **Organize Locators**: Keep locators organized by platform and user type
3. **Descriptive Names**: Use clear, descriptive test and method names
4. **Error Handling**: Implement proper error handling and assertions
5. **Screenshots**: Take screenshots on failures for debugging
6. **Parallel Execution**: Use pytest-xdist for faster test execution

## Reporting

The project generates HTML reports in the `reports/` directory:
- Test results with pass/fail status
- Execution time and details
- Screenshots on failures

## Troubleshooting

1. **Appium Server**: Ensure Appium server is running
2. **Device Connection**: Verify device/emulator connection
3. **Capabilities**: Check platform capabilities in config
4. **Dependencies**: Verify all Python packages are installed
5. **Environment**: Check environment variables and configuration

## Contributing

1. Follow the existing project structure
2. Add appropriate tests for new functionality
3. Update locators as needed
4. Maintain consistent coding style
5. Add documentation for new features

## License

[Add your license information here]
