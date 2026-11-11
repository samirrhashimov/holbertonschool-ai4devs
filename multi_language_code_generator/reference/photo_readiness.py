class PhotoReadinessEngine:
    def __init__(self, min_threshold: float = 0.80):
        self.min_threshold = max(0.0, min(1.0, min_threshold))

    def _clamp(self, value: float) -> float:
        return max(0.0, min(1.0, value))

    def calculate_face_score(self, eye_open_score: float, gaze_score: float) -> float:
        eye_open = self._clamp(eye_open_score)
        gaze = self._clamp(gaze_score)
        return (eye_open * 0.6) + (gaze * 0.4)

    def is_face_ready(self, eye_open_score: float, gaze_score: float) -> bool:
        eye_open = self._clamp(eye_open_score)
        score = self.calculate_face_score(eye_open_score, gaze_score)
        return score >= 0.85 and eye_open >= 0.80

    def analyze_frame(self, faces: list) -> dict:
        if not faces or not isinstance(faces, list):
            return {
                "totalFaces": 0,
                "readyFaces": 0,
                "frameReadinessRatio": 0.0,
                "shouldTriggerSnap": False
            }

        total_faces = len(faces)
        ready_faces = 0

        for face in faces:
            eye_open = face.get("eyeOpenScore", 0.0)
            gaze = face.get("gazeScore", 0.0)
            if self.is_face_ready(eye_open, gaze):
                ready_faces += 1

        ratio = round(ready_faces / total_faces, 2)
        should_snap = (ratio >= self.min_threshold) and (total_faces > 0)

        return {
            "totalFaces": total_faces,
            "readyFaces": ready_faces,
            "frameReadinessRatio": ratio,
            "shouldTriggerSnap": should_snap
        }