## System Architecture Diagram

```text
+-----------------------------------------------------------------------+
|                             Browser (Client)                          |
|                                                                       |
|  +------------------+     +--------------------+     +-------------+  |
|  | WebRTC / Camera  | --> | MediaPipe / Vision | --> | React UI /  |  |
|  | Stream Engine    |     | Gaze Detection JS  |     | State Mgmt  |  |
|  +------------------+     +--------------------+     +-------------+  |
+--------------------------------------|--------------------------------+
                                       |
                           REST API / WebSockets
                                       v
+-----------------------------------------------------------------------+
|                            Backend Service                            |
|                                                                       |
|  +------------------+     +--------------------+     +-------------+  |
|  | Node.js / FastAPI| --> | AI Frame Evaluator | --> | File Storage|  |
|  | Controller Layer |     | (Quality Scoring)  |     | (Local/S3)  |  |
|  +------------------+     +--------------------+     +-------------+  |
+-----------------------------------------------------------------------+

```

## Tech Stack

* **Frontend**: React.js, Tailwind CSS, WebRTC API
* **Client-Side AI Engine**: MediaPipe Face Mesh / OpenCV.js for real-time edge detection of gaze and face orientation
* **Backend Service**: Node.js (Express) or Python (FastAPI) for processing image bursts and serving session data
* **AI Scoring Engine**: Lightweight OpenCV/PyTorch microservice to rate burst photos based on face sharpness, smile rating, and eye status
* **Storage**: Browser IndexedDB for temporary frame caching + Local File System / Amazon S3 for saved high-res photos

## Core Workflow & Data Flow

1. **Stream Setup**: User opens the Web UI and authorizes camera stream via WebRTC.
2. **Real-time Inference**: Client-side MediaPipe engine inspects webcam frames at ~30 FPS for face bounding boxes and eye gaze directions.
3. **Auto-Trigger**: Once all bounding boxes report `is_looking_at_camera == true` for > 1.5 seconds, a 3-second countdown initiates.
4. **Burst Capture**: At countdown expiration, the system captures a burst of 5 fast consecutive frames.
5. **AI Ranking & Rendering**: The 5 frames are passed to the AI Evaluator to calculate quality scores. The highest-scoring frame (`is_best_shot = true`) is displayed as the primary result.