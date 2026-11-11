## Entities Overview

```text
+-------------------+        1:N        +-------------------+
|      Session      |-------------------|   CapturedPhoto   |
+-------------------+                   +-------------------+
                                                  |
                                                  | 1:N
                                        +-------------------+
                                        |  DetectedSubject  |
                                        +-------------------+

```

## Entity Definitions

### 1. Session

Represents an active auto-capture shooting session.

| Attribute | Type | Description |
| --- | --- | --- |
| `id` | String (UUID) | Unique identifier for the session |
| `start_time` | Timestamp | Timestamp when the user launched the camera session |
| `end_time` | Timestamp (Nullable) | Timestamp when the session ended |
| `status` | Enum (`active`, `paused`, `completed`) | Current status of the capture session |
| `countdown_duration` | Integer | Configured countdown timer in seconds (default: 3) |
| `sensitivity_threshold` | Float | Confidence threshold for gaze detection (0.0 - 1.0) |

### 2. CapturedPhoto

Represents an individual image frame captured by the system.

| Attribute | Type | Description |
| --- | --- | --- |
| `id` | String (UUID) | Unique identifier for the photo |
| `session_id` | String (UUID) | Foreign key referencing the parent `Session` |
| `image_url` | String | Path or Blob URL of the stored high-res image |
| `captured_at` | Timestamp | Exact moment the image frame was taken |
| `ai_quality_score` | Float | Calculated AI score (0 - 100) based on smiles & open eyes |
| `is_best_shot` | Boolean | Flag indicating if this photo was evaluated as the best shot |

### 3. DetectedSubject

Represents facial analysis metrics for an individual detected in a specific photo.

| Attribute | Type | Description |
| --- | --- | --- |
| `id` | String (UUID) | Unique identifier for the detected face entry |
| `photo_id` | String (UUID) | Foreign key referencing the associated `CapturedPhoto` |
| `bounding_box` | JSON | Coordinates `{x, y, width, height}` of the face region |
| `is_looking_at_camera` | Boolean | Detection result indicating if the subject's gaze was direct |
| `smile_confidence` | Float | Confidence score (0.0 - 1.0) for smile detection |
| `blink_detected` | Boolean | Flag indicating if the subject had eyes closed |