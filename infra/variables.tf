variable "project_id" {
  
}

variable "region" {
  default = "us-central1"
}

variable "zones" {
  type = list
  default = ["us-central1-a", "us-central1-b", "us-central1-f"]
}

variable "network" {
  
}

variable "subnetwork" {
  
}