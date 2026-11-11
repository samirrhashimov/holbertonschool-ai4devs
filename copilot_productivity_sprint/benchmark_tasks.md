# Coding Benchmark Tasks

## Task 1 - Data Validation and Transformation Function
**Requirements**: Write a utility function `formatUserProfile` that accepts a raw user object, validates the presence of required fields, trims whitespace, formats the email to lowercase, and returns a sanitized user profile.
**Inputs**: Object `{ username: string, email: string, age?: number }`
**Outputs**: Object `{ id: string, username: string, email: string, isAdult: boolean }` or throws an Error.
**Acceptance Criteria**:
- Throws an error if `username` or `email` is missing or invalid.
- Converts email string to all lower-case characters.
- Correctly evaluates `isAdult` boolean flag based on `age >= 18`.
- Generates a unique string `id` for valid profiles.

## Task 2 - REST API CRUD Endpoint (Express.js)
**Requirements**: Implement a POST `/api/v1/photos` endpoint to register a new captured photo metadata item into an array/in-memory store.
**Inputs**: JSON body `{ title: string, imageUrl: string, eyeStatus: "open" | "closed" }`
**Outputs**: Created photo object with HTTP 201 status code, or validation error with HTTP 400.
**Acceptance Criteria**:
- Returns `201 Created` status code and JSON object including assigned `id` and timestamp on success.
- Returns `400 Bad Request` if `imageUrl` is not a valid URL or `eyeStatus` is invalid.
- Properly sets `Content-Type: application/json` header in responses.

## Task 3 - Algorithmic Array Processing (Best Face Finder)
**Requirements**: Implement a function `findBestPhotoFrame` that takes an array of frame objects (each containing facial analysis scores) and selects the frame index with the highest overall score based on open eyes and gaze alignment.
**Inputs**: Array of objects `[{ frameId: number, openEyeScore: number, gazeScore: number }]`
**Outputs**: Object `{ bestFrameId: number, maxScore: number }`
**Acceptance Criteria**:
- Combined score for each frame is calculated as `(openEyeScore * 0.6) + (gazeScore * 0.4)`.
- Returns the frame object with the highest calculated total score.
- Returns `null` if the input array is empty or missing.