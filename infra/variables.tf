variable "project_id" {
  type = string
}

variable "region" {
  default = "us-central1"
}

variable "zones" {
  type = list
  default = ["us-central1-a", "us-central1-b", "us-central1-f"]
}

variable "network" {
  type = string
  default = "spyface-vpc"
}

variable "subnetwork" {
  type = string
  default = "spyface-subnet"
}