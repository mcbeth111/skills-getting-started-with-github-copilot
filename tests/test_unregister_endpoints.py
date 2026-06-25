def test_unregister_success_removes_participant(client):
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.request(
        "DELETE",
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"

    activities_response = client.get("/activities")
    assert email not in activities_response.json()[activity_name]["participants"]


def test_unregister_activity_not_found(client):
    response = client.request(
        "DELETE",
        "/activities/Unknown Club/participants",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_student_not_found(client):
    response = client.request(
        "DELETE",
        "/activities/Chess Club/participants",
        params={"email": "absent@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
