# IBM Full-Stack Developer Professional Certification Capstone Project

## Overview

This project is the capstone for the IBM Full-Stack Developer Certification. It involves developing a comprehensive web application using Django and integrating multiple microservices. The main features include user management, car dealership and review management, sentiment analysis, and continuous integration and deployment.

## Project Architecture

The project is structured into several key components:

1. **Django Application**: Serves as the main web application framework.
2. **React Frontend**: Provides a dynamic and responsive user interface.
3. **Node.js Microservices**: Manages dealerships and reviews, containerized with Docker.
4. **Sentiment Analyzer**: Analyzes review sentiments, deployed on IBM Cloud Code Engine.
5. **CI/CD Pipelines**: Ensures continuous integration and deployment of the application.

## Features

### Django Application

- **User Management**: Implemented using Django’s user authentication system.
- **Static and Dynamic Pages**: Created using Django templates and React components.
- **Car Management**: Models and views to manage car make and model data.
- **Proxy Services**: Integrates Node.js microservices for dealers and reviews.

### Node.js Microservices

- **Express Server**: Manages dealers and reviews.
- **MongoDB**: Stores dealership and review data.
- **Dockerized**: Containerized for easy deployment.

### Sentiment Analyzer

- **IBM Cloud Code Engine**: Deployed for real-time sentiment analysis of reviews.
- **Sentiment Analysis Service**: Returns positive, negative, or neutral sentiment.

### CI/CD Pipelines

- **Continuous Integration**: Automated testing and linting.
- **Continuous Deployment**: Deploys the application on Kubernetes.

## Installation and Setup

### Prerequisites

- Docker
- Kubernetes
- Node.js
- Python and Django
- React.js
- MongoDB
- IBM Cloud account

### How to Use

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/jmill29/xrwvm-fullstack_developer_capstone.git
    ```

2. **Navigate to the Database Directory:**
    ```bash
    cd xrwvm-fullstack_developer_capstone/server/database
    ```

3. **Run the Express Server with MongoDB:**
    ```bash
    docker-compose up
    ```

4. **Open a Separate Command Terminal**

5. **Navigate to the Frontend Directory:**
    ```bash
    cd /xrwvm-fullstack_developer_capstone/server/frontend
    ```

6. **Install Dependencies and Build the Frontend:**
    ```bash
    npm install
    npm run build
    ```

7. **Return to the Server Directory:**
    ```bash
    cd ../
    ```

8. **Build the Docker Image and Push to a Container Registry:**
    ```bash
    docker build -t your-docker-image .
    docker push your-docker-image
    ```

9. **Edit the `deployment.yaml` File to Reference Your Docker Image**

10. **Deploy the Application Using Kubernetes CLI:**
    ```bash
    kubectl apply -f deployment.yaml
    ```

11. **Use Port Forwarding to Run the Application:**
    ```bash
    kubectl port-forward deployment.apps/dealership 8000:8000
    ```

12. **Open the Application in Your Browser:**
    ```
    http://localhost:8000/
    ```

## Contributing

1. Fork the repository.
2. Create a feature branch.
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Commit your changes.
    ```bash
    git commit -m "Add your feature"
    ```
4. Push to the branch.
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a Pull Request.

## License

This project is licensed under the Apache License (v2.0). See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- IBM for providing the course and project template.
- Contributors and reviewers for their valuable inputs.

## Contact

For any queries or issues, please open an issue in the repository or contact the maintainer at [jacoblmiller.jlm@gmail.com].
