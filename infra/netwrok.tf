resource "google_compute_network" "spyface_vpc" {
  name = var.network
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "spyface_subnet" {
  name = var.subnetwork
  network = google_compute_network.spyface_vpc.id
  ip_cidr_range = "10.0.0.0/24"

  secondary_ip_range = [ 
    {
      range_name = "spyface-range-pods"
      ip_cidr_range = "10.1.0.0/24"
    },
    {
      range_name = "spyface-range-services"
      ip_cidr_range = "10.2.0.0/24"
    }
  ]
}