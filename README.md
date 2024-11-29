# QR Generator UI Tests

This project contains UI tests for the QR Generator application using Playwright and Pytest.

## Prerequisites

- Python 3.7+
- pip
- Docker

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running Tests

### Locally

To run the tests locally, use the following command:
```sh
pytest tests -sv --alluredir=allure-results
```

### Using Docker
To run the tests using Docker, use the following command:
```sh
docker-compose up
```

### Environment Variables
The following environment variables are used in the docker-compose.yml file:
- '**BROWSER**': The browser to use for testing (e.g., 'chromium', 'webkit', 'firefox').
- '**STAGE_ADMIN_LINK**': The admin link for the staging environment.
- '**STAGE_ADMIN_EMAIL**': The admin email for the staging environment.
- '**STAGE_ADMIN_PASSWORD**': The admin password for the staging environment.

### Test Artifacts
Test artifacts such as screenshots and videos are saved in the **artifacts** directory.

### Allure Reports
To generate and view Allure reports locally, use the following commands:
```sh
allure serve allure-results
```
### Publishing Allure Reports
Test reports publishing is done using the GitHub Actions workflow to GitHub Pages

### Github Pages
Reports are published to GitHub Pages using the following URL:
- **CHROME**: https://qr-generator-chrome.vercel.app/
- **FIREFOX**: https://qr-generator-firefox.vercel.app/
- **WEBKIT**: https://qr-generator-webkit.vercel.app/


### Fixtures
The project includes several fixtures for setting up the browser, context, and page, as well as for handling test artifacts and user deletion.

### License
This project is licensed under the MIT License.
```sh 
Make sure to replace `<repository-url>` and `<repository-directory>` with the actual URL and directory of your repository.
```