resource "google_compute_disk" "nfs" {
  name = "nfs-disk"
  type = "pd-standard"
  zone = "us-central1-a"
  size = 10

  lifecycle {
    ignore_changes = [
      labels
    ]
  }
}