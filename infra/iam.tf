resource "google_service_account" "cluster_account" {
  account_id = "spyface"
  display_name = "spyface cluster"
  project = var.project_id
}

resource "google_project_iam_member" "spyface_log" {
  role = "roles/logging.logWriter"
  member = "serviceAccount:${google_service_account.cluster_account.email}"
}

resource "google_project_iam_member" "spyface_metric" {
  role = "roles/monitoring.metricWriter"
  member = "serviceAccount:${google_service_account.cluster_account.email}"
}

resource "google_project_iam_member" "spyface_monitoring" {
  role = "roles/monitoring.viewer"
  member = "serviceAccount:${google_service_account.cluster_account.email}"
}

resource "google_project_iam_member" "spyface_stackdriver" {
  role = "roles/stackdriver.resourceMetadata.writer"
  member = "serviceAccount:${google_service_account.cluster_account.email}"
}

resource "google_project_iam_member" "spyface_storage" {
  role = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.cluster_account.email}"
}