# Cross-Language Specification - Photo Readiness & Gaze Scoring Engine

## Algorithm
Parse a batch of detected face metadata objects for a photo frame and compute:
- Individual readiness score for each detected face based on eye-open confidence and gaze alignment.
- Overall frame readiness percentage (ratio of fully ready faces to total detected faces).
- Optimal auto-capture decision flag (boolean indicating whether the photo shutter should trigger).

The readiness score per face is calculated as:
`Face Score = (eye_open_score * 0.6) + (gaze_score * 0.4)`
A face is considered **Ready** if `Face Score >= 0.85` and `eye_open_score >= 0.80`.

## Inputs
- `faces`: Array of objects, where each object contains:
  - `faceId` (string/integer)
  - `eyeOpenScore` (float between 0.0 and 1.0)
  - `gazeScore` (float between 0.0 and 1.0)
- `minThreshold` (float between 0.0 and 1.0, default: 0.80) - Minimum overall frame readiness required for auto-snap.

## Outputs
- JSON / Map object with:
  - `totalFaces` (integer): Total number of detected faces.
  - `readyFaces` (integer): Number of faces meeting the readiness criteria.
  - `frameReadinessRatio` (float): Ratio between 0.0 and 1.0.
  - `shouldTriggerSnap` (boolean): `true` if `frameReadinessRatio >= minThreshold` and `totalFaces > 0`, otherwise `false`.

## Edge Cases
- **Empty face array**: Should return `totalFaces: 0`, `frameReadinessRatio: 0.0`, and `shouldTriggerSnap: false` without throwing errors.
- **Malformed entry**: Negative scores or scores > 1.0 should be clamped into valid range `[0.0, 1.0]`.
- **Zero threshold**: If `minThreshold` is set to `0.0`, `shouldTriggerSnap` should still return `false` if `totalFaces == 0`.
- **Low lighting / low confidence scores**: Should strictly evaluate readiness without assuming missing values as ready.

## Test Cases
1. **Perfect Frame**:
   - Input: `faces = [{faceId: 1, eyeOpenScore: 0.95, gazeScore: 0.90}, {faceId: 2, eyeOpenScore: 1.0, gazeScore: 0.95}]`, `minThreshold = 0.80`
   - Output: `totalFaces: 2`, `readyFaces: 2`, `frameReadinessRatio: 1.0`, `shouldTriggerSnap: true`

2. **Partial Blink Frame**:
   - Input: `faces = [{faceId: 1, eyeOpenScore: 0.95, gazeScore: 0.90}, {faceId: 2, eyeOpenScore: 0.10, gazeScore: 0.85}]`, `minThreshold = 0.80`
   - Output: `totalFaces: 2`, `readyFaces: 1`, `frameReadinessRatio: 0.5`, `shouldTriggerSnap: false`

3. **Empty Input**:
   - Input: `faces = []`, `minThreshold = 0.80`
   - Output: `totalFaces: 0`, `readyFaces: 0`, `frameReadinessRatio: 0.0`, `shouldTriggerSnap: false`

4. **Clamped Invalid Scores**:
   - Input: `faces = [{faceId: 1, eyeOpenScore: 1.50, gazeScore: -0.20}]`, `minThreshold = 0.50`
   - Output: `totalFaces: 1`, `readyFaces: 0`, `frameReadinessRatio: 0.0`, `shouldTriggerSnap: false` *(clamped to 1.0 and 0.0, score = 0.60 < 0.85)*

5. **Single Person Ready**:
   - Input: `faces = [{faceId: 1, eyeOpenScore: 0.90, gazeScore: 0.88}]`, `minThreshold = 0.80`
   - Output: `totalFaces: 1`, `readyFaces: 1`, `frameReadinessRatio: 1.0`, `shouldTriggerSnap: true`