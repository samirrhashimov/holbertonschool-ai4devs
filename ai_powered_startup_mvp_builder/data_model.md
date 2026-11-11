# Data Model - AI-Assisted Instant Feedback Collector

## Entity Relationship Summary
The system consists of 3 primary entities: `Feedback`, `Category`, and `AnalyticsSnapshot`.

---

### 1. Entity: `Feedback`
Stores individual user feedback entries submitted through the public form.

| Field Name     | Data Type | Constraints               | Description                              |
|----------------|-----------|---------------------------|------------------------------------------|
| `id`           | INTEGER   | Primary Key, Auto-Increment| Unique identifier for each entry        |
| `rating`       | INTEGER   | NOT NULL, Range 1-5       | User rating from 1 to 5 stars            |
| `comment`      | TEXT      | NOT NULL                  | Detailed textual feedback from the user  |
| `mood`         | VARCHAR   | Default 'neutral'         | Mood tag (e.g., happy, neutral, frustrated)|
| `category_id`  | INTEGER   | Foreign Key -> Category   | Linked feedback category                 |
| `created_at`   | TIMESTAMP | Default CURRENT_TIMESTAMP | Submission timestamp                     |

---

### 2. Entity: `Category`
Organizes feedback entries into predefined product modules or topics.

| Field Name     | Data Type | Constraints               | Description                              |
|----------------|-----------|---------------------------|------------------------------------------|
| `id`           | INTEGER   | Primary Key, Auto-Increment| Unique category ID                       |
| `name`         | VARCHAR   | NOT NULL, Unique          | Category name (e.g., UI/UX, Bug, Feature)|
| `description`  | TEXT      | Optional                  | Short summary of the category            |

---

### 3. Entity: `AnalyticsSnapshot`
Tracks real-time system metrics and usage limits.

| Field Name        | Data Type | Constraints               | Description                              |
|-------------------|-----------|---------------------------|------------------------------------------|
| `id`              | INTEGER   | Primary Key, Auto-Increment| Unique snapshot ID                       |
| `total_count`     | INTEGER   | Default 0                 | Total number of feedback entries (Max 100)|
| `average_score`   | FLOAT     | Default 0.0               | Current overall average satisfaction score|
| `last_updated_at` | TIMESTAMP | Default CURRENT_TIMESTAMP | Timestamp of last aggregation calculation|