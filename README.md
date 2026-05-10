# Server Monitor Demo Bot

A Telegram bot that simulates a simple server monitoring system.

The bot shows demo server information such as status, uptime, memory usage, disk usage, CPU metrics, and recent logs.

This project is a demo. It does not connect to a real server, does not run system commands, and does not read real files or real logs.

## Features

- Telegram bot interface
- Demo server status
- Demo uptime information
- Demo memory usage
- Demo disk usage
- Demo CPU metrics
- Demo log entries
- Clean project structure
- Environment variable configuration
- Basic logging
- Error handling
- Unit tests

## Commands

| Command | Description |
|---|---|
| `/start` | Shows the welcome message |
| `/help` | Shows the available commands |
| `/status` | Shows the demo server status |
| `/uptime` | Shows demo server uptime |
| `/memory` | Shows demo memory usage |
| `/disk` | Shows demo disk usage |
| `/cpu` | Shows demo CPU metrics |
| `/logs` | Shows recent demo logs |

## Example Output

### `/status`

```text
🖥 Server Status
━━━━━━━━━━━━━━
📍 Name: demo-server-01
🌍 Environment: DEMO
⏱ Time: 2026-05-10 19:30:00
🟢 Status: Online
💬 Message: Server is online
```

### `/memory`

```text
🧠 Memory Usage
━━━━━━━━━━━━━━
📊 Usage: 39%
✅ Free: 4.9 GB
📦 Used: 3.1 GB
🛠 Total: 8 GB
```

## Project Structure

```text
server-monitor-demo-bot/
│
├── bot/
│   ├── main.py
│   ├── config.py
│   ├── exceptions.py
│   ├── logging_config.py
│   ├── handlers.py
│   ├── formatters.py
│   │
│   ├── domain/
│   │   ├── server_status.py
│   │   ├── memory_info.py
│   │   ├── disk_info.py
│   │   ├── cpu_info.py
│   │   └── log_entry.py
│   │
│   └── services/
│       └── demo_server_service.py
│
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Technologies

- Python
- python-telegram-bot
- python-dotenv
- pytest
- Telegram Bot API

## Installation

### 1. Clone the project

```bash
git clone https://github.com/TomKrimberg/server-monitor-demo-bot
cd server-monitor-demo-bot
```

If the project is already on your computer, just open the project folder.

### 2. Create a virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a Telegram bot

1. Open Telegram.
2. Search for `@BotFather`.
3. Send `/newbot`.
4. Choose a name for the bot.
5. Choose a username that ends with `bot`.
6. Copy the bot token.

### 5. Create a `.env` file

Create a file named `.env` in the root folder of the project.

Add:

```env
BOT_TOKEN=PASTE_YOUR_TELEGRAM_BOT_TOKEN_HERE
BOT_NAME=Server Monitor Demo Bot
```

Do not upload the `.env` file to GitHub.

### 6. Run the bot

From the root folder, run:

```bash
python -m bot.main
```

If the bot starts correctly, the terminal should show something like:

```text
Starting Server Monitor Demo Bot...
Bot is now running with polling.
```

Then open Telegram and send:

```text
/start
```

## Running Tests

The project includes basic unit tests for the demo service and message formatters.

To run the tests, use:

```bash
python -m pytest
```

Expected result:

```text
15 passed
```

## Configuration

The project uses environment variables from the `.env` file.

| Variable | Description |
|---|---|
| `BOT_TOKEN` | Telegram bot token from BotFather |
| `BOT_NAME` | Bot display name |

Example:

```env
BOT_TOKEN=123456789:ABCDEF_your_token_here
BOT_NAME=Server Monitor Demo Bot
```

## Main Files

### `main.py`

The entry point of the project.

It loads the configuration, sets up logging, creates the service and handlers, registers the Telegram commands, and starts the bot.

### `config.py`

Loads values from the `.env` file and checks that the required configuration exists.

### `handlers.py`

Contains the Telegram command handlers.

Each handler receives a command, calls the demo service, formats the result, and sends a response back to the user.

### `formatters.py`

Formats the data into readable Telegram messages.

### `demo_server_service.py`

Generates demo server data.

It does not access a real server or real system information.

### `domain/`

Contains the main data classes used by the project.

| Class | Purpose |
|---|---|
| `ServerStatus` | Represents server status |
| `MemoryInfo` | Represents memory usage |
| `DiskInfo` | Represents disk usage |
| `CpuInfo` | Represents CPU metrics |
| `LogEntry` | Represents one log entry |

## Safety

This bot is safe to share because it only uses demo data.

It does not:

- connect to a real server
- read real system logs
- run shell commands
- restart services
- expose private information
- control any real machine

## Logging

The project logs important events such as bot startup, received commands, and errors.

Example:

```text
[2026-05-10 19:13:13] INFO - Starting Server Monitor Demo Bot...
[2026-05-10 19:13:14] INFO - Bot is now running with polling.
[2026-05-10 19:14:01] INFO - Command /status received
```

## Stopping the bot

To stop the bot while it is running, press:

```text
Ctrl + C
```

## Future Improvements

Possible features to add later:

- Add a `/health` summary command
- Add inline keyboard buttons
- Add user authorization
- Add more advanced tests
- Add Docker support
- Add a private real-server monitoring version

## Security Note

This project is intentionally built as a demo.

If real server monitoring is added in the future, it should include authorization, command whitelisting, safe logging, and strict access control.

## Author

Created as a Python project for practicing Telegram bot development, object-oriented programming, clean code structure, and basic software engineering.