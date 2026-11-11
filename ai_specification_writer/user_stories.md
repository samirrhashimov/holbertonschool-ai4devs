# User Stories - PerfectSnap Camera App

### User Story 1
As a group photo taker, I want the camera to detect all faces in the frame in real time so that the app knows who needs to be looking at the screen.
**Acceptance Criteria**:
- System detects all visible human faces within 0.5 seconds of opening the camera.
- System highlights detected faces with visual boundary markers.
- System dynamically updates the face count when people enter or leave the frame.
**Priority**: MVP

### User Story 2
As a photo taker, I want the app to detect whether each person's eyes are open so that photos are not taken when someone blinks.
**Acceptance Criteria**:
- System accurately determines open vs. closed eye status for each detected face.
- System displays an indicator (e.g., green ring for open, red ring for closed) around each face.
- System updates eye status in real time with minimal latency (<100ms).
**Priority**: MVP

### User Story 3
As a group photo taker, I want the app to track gaze direction so that it knows if everyone is looking directly at the camera lens/screen.
**Acceptance Criteria**:
- System identifies whether a detected face is gazing toward the camera view area.
- Visual indicator changes state when a user turns their focus toward the screen.
- System works accurately across different lighting conditions and skin tones.
**Priority**: MVP

### User Story 4
As a user, I want the camera to automatically trigger the shot when 100% of people are looking and have their eyes open so that I do not need to push the shutter manually.
**Acceptance Criteria**:
- Shutter triggers automatically within 300ms once all conditions (eyes open + looking at screen) are met.
- An optional 3-second countdown audio beep alerts users right before the auto-snap occurs.
- System plays a distinct shutter sound and provides haptic feedback upon capture.
**Priority**: MVP

### User Story 5
As a user, I want a burst capture and composite mode so that if one person blinks during the photo, the app can combine the best faces from a quick series of shots.
**Acceptance Criteria**:
- System captures 5–8 fast consecutive frames when auto-trigger conditions are close to optimal.
- AI algorithm automatically replaces blinked faces with open-eyed faces from adjacent frames.
- User can view and confirm the generated composite photo before saving.
**Priority**: High

### User Story 6
As a solo traveler using a tripod, I want to set a readiness timer so that I have time to run into position before the AI gaze detection activates.
**Acceptance Criteria**:
- User can select a delay timer (3s, 5s, 10s) before auto-detection begins.
- Screen displays a clear visual countdown timer visible from a distance.
- Auto-capture logic triggers only after the delay timer expires and all faces are ready.
**Priority**: High

### User Story 7
As a user, I want to manually adjust the threshold for auto-capture (e.g., allow 90% compliance instead of 100% for large crowds) so that I can capture big group photos faster.
**Acceptance Criteria**:
- User can select between "Strict (100% Ready)", "Flexible (80%+ Ready)", or "Manual Trigger".
- In "Flexible" mode, the camera snaps when the selected percentage of faces meet criteria.
- Setting persists for subsequent camera sessions until changed.
**Priority**: Medium

### User Story 8
As a photographer, I want a manual shutter button override so that I can still take a picture anytime regardless of AI detection status.
**Acceptance Criteria**:
- Screen presents a standard, accessible shutter button at all times.
- Pressing the manual button instantly captures a photo irrespective of eye status or gaze alignment.
- Manual press does not crash or freeze the real-time AI background process.
**Priority**: MVP

### User Story 9
As a user, I want to view and review photos in an in-app gallery with face readiness highlights so that I can verify that everyone's eyes are open.
**Acceptance Criteria**:
- App gallery provides a zoom tool focused automatically on detected faces for quick review.
- User can delete, save to device gallery, or share photos directly from the review screen.
- App shows metadata tag confirming "AI Perfect Shot" for automatically verified photos.
**Priority**: Medium

### User Story 10
As a user in low-light environments, I want screen flash or night mode support so that face and eye detection continues working reliably in dark places.
**Acceptance Criteria**:
- App automatically boosts screen brightness or enables flash when ambient light is low.
- Detection algorithms maintain accuracy in low-light conditions.
- User can manually toggle flash mode (On, Off, Auto).
**Priority**: Low