---
config:
      theme: redux
---
```mermaid
flowchart TD;
    A["User Service Start"]
    
    A --> B["Receive API Request"]
    
    B --> C{"Request Type?"}
    
    C -->|Login/Register| D["Authenticate User (JWT/OAuth)"]
    C -->|Profile Update| E["Update User Details in DB"]
    C -->|Fetch Profile| F["Retrieve User Info"]
    C -->|Ride History| G["Fetch User Ride Data"]

    D --> H{"Valid Credentials?"}
    H -->|Yes| I["Generate JWT Token"]
    H -->|No| J["Return Authentication Error"]
    
    I --> K["Return Token & User Info"]

    E --> L["Validate New Profile Data"]
    L -->|Valid| M["Update DB (PostgreSQL)"]
    L -->|Invalid| N["Return Validation Error"]
    
    F --> O["Fetch Data from PostgreSQL"]
    O --> P["Return User Profile"]

    G --> Q["Fetch Ride Data from DB"]
    Q --> R["Return Ride History"]

    K & M & P & R --> S["Send API Response"]
    
    S --> T["End Request"]
