module "gke" {
  source = "terraform-google-modules/kubernetes-engine/google"
  project_id = var.project_id
  name = "spyface-cluster"
  region = var.region
  zones = var.zones
  network = google_compute_network.spyface_vpc.name
  subnetwork = google_compute_subnetwork.spyface_subnet.name
  ip_range_services = "spyface-range-services"
  ip_range_pods = "spyface-range-pods"
  default_max_pods_per_node = 30
  create_service_account = false
  service_account = google_service_account.cluster_account.email

  node_pools = [ {
    name = "spyfdace-node-pool"
    machine-type = "e2-medium"
    min_count = 1
    max_count = 1
    local_ssd_count = 0
    disk_size_gb = 50
    disk_type = "pd-standard"
    image_type = "COS"
    initial_node_count = 1
  } ]

}