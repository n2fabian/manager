# Model Context Protocol (MCP) Tools

This directory contains MCP tool implementations for external service integrations that enhance the Band Manager Agent capabilities.

## What are MCPs?

Model Context Protocol (MCP) tools are integrations that allow AI agents to interact with external services and APIs. They provide standardized interfaces for common operations like file storage, email, and data retrieval.

## Available MCPs

### 🔄 Implemented

Currently, all MCPs are framework/skeleton implementations. Full functionality requires API credentials and additional development.

### 📋 Planned

- **Google Drive MCP** (`google_drive_mcp.py`): Access shared storage for band documents, contracts, and press materials
- **Email MCP** (`email_mcp.py`): Send automated emails via Gmail API for venue outreach and follow-ups
- **Dropbox MCP** (`dropbox_mcp.py`): Alternative cloud storage integration

## Usage

### Prerequisites

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables**:
   Copy `.env.example` to `.env` and fill in your API credentials:
   ```bash
   cp .env.example .env
   ```

3. **Obtain API credentials**:
   - Google Drive: https://developers.google.com/drive/api/quickstart/python
   - Gmail: https://developers.google.com/gmail/api/quickstart/python

### Example: Google Drive MCP

```python
from mcps import GoogleDriveMCP

# Initialize with credentials
drive = GoogleDriveMCP('path/to/credentials.json')

# Upload a file
file_id = drive.upload_file(
    file_path='docs/templates/tech-rider.pdf',
    folder_id='band-documents'
)

# Create shareable link
share_link = drive.create_share_link(file_id)
print(f"Share this with the venue: {share_link}")

# Download a file
drive.download_file(file_id, destination='local/path.pdf')

# List files in a folder
files = drive.list_files(folder_id='band-documents')
for file in files:
    print(f"{file['name']}: {file['id']}")
```

### Example: Email MCP

```python
from mcps import EmailMCP

# Initialize with Gmail credentials
email = EmailMCP('path/to/gmail-credentials.json')

# Send an email using a template
email.send_template_email(
    template='venue-email-template',
    to='venue@example.com',
    variables={
        'venue_name': 'The Metal Tavern',
        'band_name': 'Combine Harvester',
        'available_dates': ['2026-03-15', '2026-03-22']
    },
    attachments=['tech-rider.pdf', 'epk.pdf']
)

# Schedule a follow-up
email.schedule_email(
    template='follow-up',
    to='venue@example.com',
    send_date='2026-02-26',  # 1 week from now
    variables={'venue_name': 'The Metal Tavern'}
)

# Check for responses
responses = email.get_responses(thread_id='...')
```

## Creating New MCPs

To create a new MCP tool:

1. **Inherit from BaseMCP**:
   ```python
   from mcps.base_mcp import BaseMCP
   
   class MyServiceMCP(BaseMCP):
       def __init__(self, credentials_path):
           super().__init__(credentials_path)
           # Initialize your service client
   ```

2. **Implement required methods**:
   - `authenticate()`: Handle OAuth or API key authentication
   - `execute(action, params)`: Execute service-specific actions

3. **Add documentation**:
   - Docstrings for all public methods
   - Usage examples
   - Security considerations

4. **Add to this README**:
   - Brief description
   - Example usage
   - Prerequisites

## Security Best Practices

⚠️ **Never commit credentials to Git!**

- Store all API keys and tokens in `.env` file
- `.env` is automatically excluded via `.gitignore`
- Use service accounts for automated access when possible
- Implement token refresh for OAuth flows
- Log all API operations for audit trails
- Use least-privilege access (only request necessary scopes)

## Testing

```bash
# Run MCP tests
pytest tests/test_mcps.py

# Test specific MCP
pytest tests/test_mcps.py::test_google_drive_mcp
```

## Troubleshooting

### "Invalid credentials" error

- Verify your credentials file path is correct
- Check that credentials are for the correct Google Cloud project
- Ensure you've enabled the necessary APIs in Google Cloud Console

### Rate limiting errors

- MCPs implement rate limiting by default
- If you hit limits, reduce request frequency
- Consider caching results when appropriate

### OAuth token expired

- Tokens are automatically refreshed by the OAuth flow
- If manual refresh is needed, delete `token.json` and re-authenticate

## Resources

- [Google Drive API Documentation](https://developers.google.com/drive)
- [Gmail API Documentation](https://developers.google.com/gmail)
- [OAuth 2.0 for Python](https://developers.google.com/identity/protocols/oauth2)

## Contributing

See `CONTRIBUTING.md` for guidelines on adding new MCPs or improving existing ones.

---

*Last Updated: 2026-02-19*
