from mcp.server.fastmcp import FastMCP
from typing import List, Dict


mcp = FastMCP("LeaveManagementSystem")

# In-memory store for leave applications
leave_db: List[Dict] = [
    {
        "employee_id": "EMP001",
        "from_date": "2025-05-10",
        "to_date": "2025-05-15",
        "reason": "Vacation",
        "status": "Pending"
    }
]


@mcp.tool()
def apply_leave(employee_id: str, from_date: str, to_date: str, reason: str) -> str:
    leave = {
        "employee_id": employee_id,
        "from_date": from_date,
        "to_date": to_date,
        "reason": reason,
        "status": "Pending"
    }
    leave_db.append(leave)
    return "Leave application submitted successfully."

@mcp.tool()
def view_leaves() -> List[Dict]:
    return leave_db

@mcp.tool()
def approve_leave(index: int) -> str:
    if 0 <= index < len(leave_db):
        leave_db[index]["status"] = "Approved"
        return "Leave approved."
    return "Invalid index."

@mcp.tool()
def reject_leave(index: int) -> str:
    if 0 <= index < len(leave_db):
        leave_db[index]["status"] = "Rejected"
        return "Leave rejected."
    return "Invalid index."

@mcp.resource("leaves://{employee_id}")
def get_employee_leaves(employee_id: str) -> List[Dict]:
    return [leave for leave in leave_db if leave["employee_id"] == employee_id]

@mcp.resource("greeting://{name}")
def get_greetin(name: str = "Guest"):
    return f"Hello, {name}! How can I assist you today?"
