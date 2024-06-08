# Chat Room Application

## Overview

This web application is a real-time chat platform where users can interact in a general chat room or create their own private rooms for more specific conversations. The default page provides a general room where all users can join and chat together. Users also have the option to create and join rooms by specifying a room name (e.g., `room2`) to have focused and private discussions.

## Features

- **General Chat Room**: A default chat room where all users can interact.

- **Private Room Creation**: Users can create and join private chat rooms by specifying a unique room name.

- **Real-Time Messaging**: Instant messaging powered by real-time technologies ensuring quick and seamless communication.

- **User-Friendly Interface**: Simple and intuitive design for easy navigation and use.

## Getting Started

### Prerequisites

- Python (version 3.7 or higher)
- Flask
- Flask-SocketIO
- Other dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chat-room-application.git
   cd chat-room-application
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Flask server:
   ```bash
   python main.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. **General Room**: Upon accessing the application, you will enter the general chat room by default. Start chatting with other users instantly.

2. **Create/Join Private Room**: To create or join a private room, append the room name to the URL. For example, to create or join `room2`, navigate to:
   ```
   http://localhost:5000/room2
   ```

## Contributing

We welcome contributions to enhance the functionality and features of the chat room application. Please feel free to fork the repository, create a new branch, and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or need further assistance, please reach out to nickaj1505@gmail.com