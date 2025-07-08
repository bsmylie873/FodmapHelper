# FODMAP Helper

A full-stack application designed to help users identify foods containing FODMAPs (Fermentable Oligosaccharides, Disaccharides, Monosaccharides, and Polyols) that may trigger IBS (Irritable Bowel Syndrome) symptoms. This tool empowers users to make informed dietary choices and manage their digestive health effectively.

## Features

- 🔍 **Food Search & Analysis**: Quickly search and identify FODMAP content in foods
- 📊 **FODMAP Level Indicators**: Clear visual indicators of FODMAP levels (Low, Medium, High)
- 🏷️ **Food Categories**: Organized categorization of foods by type and FODMAP content
- 📱 **Responsive Design**: Seamless experience across desktop and mobile devices
- 📋 **Food Lists**: Access comprehensive lists of low and high FODMAP foods

## Tech Stack

### Backend
- **Framework**: FastAPI (Python)
- **API Documentation**: Automatic Swagger/OpenAPI documentation
- **Data Validation**: Pydantic models

### Frontend
- **Framework**: React
- **State Management**: React Context/Redux
- **UI Components**: Material-UI/Tailwind
- **API Integration**: Axios
- **Routing**: React Router

### Database
- **Engine**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic

## Installation

### Prerequisites
- Python 3.8+
- Node.js 14+
- PostgreSQL 12+
- pip and npm/yarn

### Backend Setup
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/fodmap-helper.git
   cd fodmap-helper
   ```

2. Create and activate virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. Configure environment variables
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials and other settings
   ```

5. Run database migrations
   ```bash
   alembic upgrade head
   ```

### Frontend Setup
1. Install dependencies
   ```bash
   cd frontend
   npm install  # or: yarn install
   ```

2. Configure environment
   ```bash
   cp .env.example .env
   # Edit .env with your API endpoint and other settings
   ```

## Usage

### Running the Application

1. Start the backend server
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

2. Start the frontend development server
   ```bash
   cd frontend
   npm start  # or: yarn start
   ```

3. Access the application at `http://localhost:3000`

## API Overview

### Key Endpoints

```
GET /api/foods
    - List all foods with FODMAP information
    - Query parameters: category, search_term

POST /api/foods/search
    - Search foods by name or attributes
    - Body: {"query": "apple", "filters": {...}}

GET /api/foods/{food_id}
    - Get detailed information about a specific food

GET /api/foods/categories
    - Get list of all food categories
```

Full API documentation available at `/docs` when running the backend server.

## Database Schema

### Core Entities

1. **Foods**
   - ID, name, category
   - FODMAP levels (fructose, lactose, etc.)
   - Serving size information

2. **Categories**
   - ID, name
   - Description
   - Parent category (for hierarchical organization)

## Architecture Decision Records (ADRs)

This project uses Architecture Decision Records (ADRs) to document important architectural decisions. An ADR is a document that captures an important architectural decision made along with its context and consequences.

### ADR Structure
Each ADR in this project follows a standard format:
- Title
- Status (Proposed, Accepted, Deprecated, Superseded)
- Context (What is the issue that we're seeing that is motivating this decision?)
- Decision (What is the change that we're proposing and/or doing?)
- Consequences (What becomes easier or more difficult to do because of this change?)

### ADR Location
ADRs are stored in the `docs/adr` directory and are numbered sequentially. Each ADR is written in Markdown format and follows the naming convention `NNNN-title-with-dashes.md` where `NNNN` is a sequential number.

### Creating New ADRs
When creating a new ADR:
1. Create a new file in the `docs/adr` directory
2. Use the next sequential number in the sequence
3. Use the template provided in `docs/adr/template.md`
4. Submit the ADR as a pull request for review

For more information about ADRs, see the [architecture-decision-record repository](https://github.com/joelparkerhenderson/architecture-decision-record).

## Contributing

We welcome contributions to the FODMAP Helper project! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your PR:
- Follows the existing code style
- Includes appropriate tests
- Updates documentation as needed
- Describes the changes made

## License

[MIT License](LICENSE) - Feel free to use this project for personal or commercial purposes.

---

For questions or support, please [open an issue](https://github.com/yourusername/fodmap-helper/issues) on our GitHub repository. 