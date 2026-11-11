# High-Level Architecture - AI-Assisted Instant Feedback Collector

## 1. System Overview
The **AI-Assisted Instant Feedback Collector** is built using a lightweight serverless architecture deployed on **Val Town / Townie AI**. The system connects a responsive React/Tailwind frontend with an HTTP Val backend API, utilizing SQLite for persistent data storage.

---

## 2. Architecture Diagram

```mermaid
graph TD
    %% User Layer
    subgraph Client ["Client Layer (Browser)"]
        UI_Submit["Feedback Submission Form"]
        UI_Dash["Admin Analytics Dashboard"]
        UI_Search["Real-Time Filter & Search"]
    end

    %% API Layer
    subgraph Backend ["Serverless API Layer (Val Town / Townie AI)"]
        HTTP_Val["HTTP Val Endpoint (Express / Hono)"]
        Validator["Input Validator & Entry Limit Checker"]
        Exporter["CSV Export Handler"]
    end

    %% Data Layer
    subgraph Storage ["Data Layer"]
        DB[(SQLite Storage)]
    end

    %% Flow Connections
    UI_Submit -->|HTTP POST /api/feedback| HTTP_Val
    UI_Dash -->|HTTP GET /api/feedback| HTTP_Val
    UI_Dash -->|HTTP GET /api/export| Exporter
    UI_Search -->|HTTP GET /api/search| HTTP_Val

    HTTP_Val --> Validator
    Validator -->|Write / Insert| DB
    HTTP_Val -->|Read Query| DB
    Exporter -->|Query & Generate CSV| DB