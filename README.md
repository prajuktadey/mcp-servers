# mcp-servers

## HR-Leave-Management-System

This project is built using **MCP (Model Context Protocol)** and provides a server with tools and resources for managing employee leave requests. It allows HR admins and employees to interact with a leave management system through tools and resources, such as applying for leave, viewing leave records, and approving/rejecting leave requests.

### 2. **Install Required Dependencies**
Ensure you have **Python 3.7+** installed. Then, install the required dependencies.
```bash
pip install uv
uv init leave-management
```

### 3. **Install the Server in Claude Desktop**
Run the following command in your project directory:
```bash
uv run mcp install main.py
```

### Explanation:
1. **Installing the server**: The command `uv run mcp install main.py` is used to install your server in Claude Desktop. 
2. **Restarting Claude Desktop**: If there are any running instances of Claude Desktop, you need to close them and restart to apply changes made by the server installation.

