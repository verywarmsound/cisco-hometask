# NestJS Application

This is a NestJS application that serves tagged content. The application reads a JSON file that represents a database of documents and tags. Each document is represented by a URI and each tag is a string. Tags can have sub-tags, which can be represented as an array of strings.

## Prerequisites

- Node.js (version 14 or later)
- npm (version 6 or later)

## Installation

1. Clone the repository:     
```bash
git clone <repository-url>
```
2. Navigate to the project directory:
```bash
cd <project-directory>
```
3. Install the dependencies:

```bash
npm install
```
## Running the Application

To run the application locally, use the following command:

```bash
npm run start
```
The application will start and listen on `http://localhost:3000`.

## API Endpoints

- `GET /taggedContent?tag=<tag>`: Returns a JSON array of documents (represented by URIs) associated with the given tag (and its sub-tags).

## Data

The data for this application is stored in a JSON file located at `src/tag/db.json`. This file represents a database of documents and tags. Each document is represented by a URI and each tag is a string. Tags can have sub-tags, which can be represented as an array of strings.

## Testing

To run the tests, use the following command:
    
```bash
npm run test
```
