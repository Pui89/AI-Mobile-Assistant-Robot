# AI NOMAD / Mobile Assistant Robot — Perception Accuracy Upgrade v0.1

**Status:** Requirements specified; no autonomous assistance or physical manipulation capability is validated.

Shared contract: [PUI89 Perception and Accuracy Standard](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/perception/PUI89_PERCEPTION_AND_ACCURACY_STANDARD_V0.1.md).

## Priority perception tasks

1. Detect people, mobility aids, pets, furniture, doors, stairs, glass and dynamic obstacles.
2. Estimate human pose only for explicitly defined safety/navigation needs; avoid identity recognition by default.
3. Maintain privacy-preserving person tracks with short retention and no unnecessary face identification.
4. Detect free space, floor boundaries, stair edges, door openings and narrow passages.
5. Estimate object pose and grasp affordances only with calibrated RGB-D/depth evidence and uncertainty.
6. Recognize handover state and verify whether an object was actually received/released.
7. Maintain indoor localization and map quality; detect localization loss and map changes.
8. Predict short-horizon movement of nearby people/obstacles without assuming intent or consent.
9. Verify task completion from independent evidence; starting a task is not proof of completion.

## Evaluation

Measure person/obstacle recall, false alarms, minimum-distance estimation error, stair-edge missed detections, localization drift, object pose error, grasp-point error, tracking identity switches and task-verification false success. Evaluate low light, reflective surfaces, clutter, narrow corridors, moving people, pets and partial occlusion.

**Safety boundary:** preserve human control and safe stopping. No grasp, lift, handover or navigation action is authorized by a single perception score.
