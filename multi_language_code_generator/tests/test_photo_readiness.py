import unittest
from photo_readiness import PhotoReadinessEngine

class TestPhotoReadinessEngine(unittest.TestCase):
    def setUp(self):
        self.engine = PhotoReadinessEngine(min_threshold=0.80)

    def test_perfect_frame(self):
        faces = [
            {"faceId": 1, "eyeOpenScore": 0.95, "gazeScore": 0.90},
            {"faceId": 2, "eyeOpenScore": 1.0, "gazeScore": 0.95}
        ]
        result = self.engine.analyze_frame(faces)
        self.assertEqual(result["totalFaces"], 2)
        self.assertEqual(result["readyFaces"], 2)
        self.assertEqual(result["frameReadinessRatio"], 1.0)
        self.assertTrue(result["shouldTriggerSnap"])

    def test_partial_blink_frame(self):
        faces = [
            {"faceId": 1, "eyeOpenScore": 0.95, "gazeScore": 0.90},
            {"faceId": 2, "eyeOpenScore": 0.10, "gazeScore": 0.85}
        ]
        result = self.engine.analyze_frame(faces)
        self.assertEqual(result["totalFaces"], 2)
        self.assertEqual(result["readyFaces"], 1)
        self.assertEqual(result["frameReadinessRatio"], 0.5)
        self.assertFalse(result["shouldTriggerSnap"])

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

    def test_single_person_ready(self):
        faces = [{"faceId": 1, "eyeOpenScore": 0.90, "gazeScore": 0.88}]
        result = self.engine.analyze_frame(faces)
        self.assertEqual(result["totalFaces"], 1)
        self.assertEqual(result["readyFaces"], 1)
        self.assertTrue(result["shouldTriggerSnap"])

    def test_threshold_boundary_exact_match(self):
        engine_50 = PhotoReadinessEngine(min_threshold=0.50)
        faces = [
            {"faceId": 1, "eyeOpenScore": 0.95, "gazeScore": 0.90},
            {"faceId": 2, "eyeOpenScore": 0.0, "gazeScore": 0.0}
        ]
        result = engine_50.analyze_frame(faces)
        self.assertEqual(result["frameReadinessRatio"], 0.5)
        self.assertTrue(result["shouldTriggerSnap"])

    def test_eye_open_threshold_strictness(self):
        faces = [{"faceId": 1, "eyeOpenScore": 0.79, "gazeScore": 1.0}]
        result = self.engine.analyze_frame(faces)
        self.assertEqual(result["readyFaces"], 0)
        self.assertFalse(result["shouldTriggerSnap"])

    def test_zero_threshold_with_empty_faces(self):
        engine_zero = PhotoReadinessEngine(min_threshold=0.0)
        result = engine_zero.analyze_frame([])
        self.assertFalse(result["shouldTriggerSnap"])

    def test_large_group_frame(self):
        faces = [{"faceId": i, "eyeOpenScore": 0.95, "gazeScore": 0.90} for i in range(10)]
        result = self.engine.analyze_frame(faces)
        self.assertEqual(result["totalFaces"], 10)
        self.assertEqual(result["readyFaces"], 10)
        self.assertTrue(result["shouldTriggerSnap"])

if __name__ == "__main__":
    unittest.main()