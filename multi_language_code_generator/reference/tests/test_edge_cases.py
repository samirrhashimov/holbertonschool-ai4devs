import unittest
from photo_readiness import PhotoReadinessEngine

class TestPhotoReadinessEdgeCases(unittest.TestCase):
    def setUp(self):
        self.engine = PhotoReadinessEngine(min_threshold=0.80)

    def test_empty_faces_list(self):
        result = self.engine.analyze_frame([])
        self.assertEqual(result["totalFaces"], 0)
        self.assertEqual(result["readyFaces"], 0)
        self.assertEqual(result["frameReadinessRatio"], 0.0)
        self.assertFalse(result["shouldTriggerSnap"])

    def test_invalid_input_type(self):
        result = self.engine.analyze_frame(None)
        self.assertEqual(result["totalFaces"], 0)
        self.assertFalse(result["shouldTriggerSnap"])

    def test_out_of_bounds_score_clamping(self):
        faces = [{"faceId": 1, "eyeOpenScore": 1.50, "gazeScore": -0.20}]
        result = self.engine.analyze_frame(faces)
        self.assertEqual(result["readyFaces"], 0)
        self.assertFalse(result["shouldTriggerSnap"])

    def test_eye_open_threshold_strictness(self):
        faces = [{"faceId": 1, "eyeOpenScore": 0.79, "gazeScore": 1.0}]
        result = self.engine.analyze_frame(faces)
        self.assertEqual(result["readyFaces"], 0)
        self.assertFalse(result["shouldTriggerSnap"])

    def test_zero_threshold_with_empty_faces(self):
        engine_zero = PhotoReadinessEngine(min_threshold=0.0)
        result = engine_zero.analyze_frame([])
        self.assertFalse(result["shouldTriggerSnap"])

if __name__ == "__main__":
    unittest.main()