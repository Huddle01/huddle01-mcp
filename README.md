# Huddle01 MCP Server

A Model Context Protocol (MCP) server that provides seamless integration with Huddle01's video conferencing platform. This server enables AI assistants and applications to interact with Huddle01's API services through the standardized MCP interface.

## What We're Building

The Huddle01 MCP Server acts as a bridge between AI applications and Huddle01's video conferencing services. It provides:

- **Room Management**: Create, join, and manage video conference rooms
- **Meeting Controls**: Start, stop, and control meeting sessions
- **Participant Management**: Handle participant interactions and permissions
- **Real-time Communication**: Enable seamless video/audio communication features
- **Analytics & Monitoring**: Access meeting insights and usage statistics

## What We Achieve

By implementing this MCP server, we enable:

### 🤖 **AI-Powered Meeting Management**
- AI assistants can automatically create and schedule meetings
- Intelligent meeting room suggestions based on participant availability
- Automated meeting summaries and action items generation

### 🔗 **Seamless Integration**
- Standardized MCP protocol ensures compatibility with various AI platforms
- Easy integration with existing workflows and applications
- Consistent API interface across different client implementations

### 🚀 **Enhanced Productivity**
- Reduce manual meeting setup and management overhead
- Enable voice-commanded meeting controls through AI assistants
- Automate routine meeting tasks and workflows

### 🛡️ **Enterprise-Ready**
- Secure API key management and authentication
- Project-based isolation for multi-tenant environments
- Health monitoring and observability features

## Features

- **FastMCP Framework**: Built on the modern FastMCP framework for high performance
- **Async Support**: Full asynchronous operation for scalable concurrent requests
- **Health Monitoring**: Built-in health check endpoints for service monitoring
- **Environment Configuration**: Flexible configuration through environment variables
- **Type Safety**: Full type hints and Pydantic models for robust development

## Prerequisites

- Python 3.12 or higher
- UV package manager (recommended) or pip
- Huddle01 API credentials (API Key and Project ID)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd huddle01-mcp
```

### 2. Environment Setup

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit the `.env` file with your Huddle01 credentials:

```env
Huddle01_API_KEY=your_huddle01_api_key_here
Huddle01_PROJECT_ID=your_project_id_here
```

### 3. Install Dependencies

Using UV (recommended):

```bash
make install
```

Or using pip:

```bash
pip install -r requirements.txt
```

### 4. Run the Service

Start the MCP server:

```bash
make run
```

The server will start and be available for MCP client connections.

### 5. Health Check

Verify the service is running:

```bash
curl http://localhost:8000/healthz
```

Expected response:
```json
{"status": "ok"}
```

## Development

### Code Quality

Format code:
```bash
make format
```

Lint code:
```bash
make lint
```

Check code quality:
```bash
make check
```

### Project Structure

```
huddle01-mcp/
├── app/
│   ├── __init__.py
│   ├── config.py          # Environment configuration
│   ├── main.py           # Application entry point
│   └── mcp/
│       ├── __init__.py
│       ├── client.py     # Huddle01 API client
│       └── server.py     # MCP server implementation
├── makefile              # Development commands
├── pyproject.toml        # Project configuration
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Configuration

The service is configured through environment variables:

| Variable | Description | Required |
|----------|-------------|----------|
| `Huddle01_API_KEY` | Your Huddle01 API key | Yes |
| `Huddle01_PROJECT_ID` | Your Huddle01 project ID | Yes |

## Usage with MCP Clients

Once running, this server can be connected to any MCP-compatible client. The server provides tools and resources for:

- Creating and managing Huddle01 rooms
- Handling meeting participants
- Controlling meeting sessions
- Accessing meeting analytics

## API Documentation

The server exposes MCP-standard endpoints:

- **Health Check**: `GET /healthz` - Service health verification
- **MCP Protocol**: Standard MCP endpoints for tool and resource discovery

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run code quality checks: `make check`
5. Submit a pull request

## Support

For issues and questions:

- Check the [Huddle01 API Documentation](https://docs.huddle01.com)
- Review the [MCP Specification](https://modelcontextprotocol.io)
- Create an issue in this repository

## License

[Add your license information here]

---

Built with ❤️ using [FastMCP](https://github.com/jlowin/fastmcp) and [Huddle01](https://huddle01.com)