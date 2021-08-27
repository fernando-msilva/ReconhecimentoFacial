packer {
  required_plugins {
    docker = {
      version = ">= 0.0.7"
      source  = "github.com/hashicorp/docker"
    }
  }
}

variable "project_id" {
  default = ""
}

source "docker" "krakend" {
  image  = "devopsfaith/krakend"
  commit = true
  changes = [
    "ENTRYPOINT [\"/usr/bin/krakend\"]",
    "CMD [\"run\", \"-c\", \"/krakend.json\"]"
  ]
}

build {
  name = "krakend-image"
  sources = [
    "source.docker.krakend"
  ]

  provisioner "file" {
    source = "krakend.json"
    destination = "/krakend.json"
  }

  post-processors {
    post-processor "docker-tag" {
      repository = "gcr.io/${var.project_id}/krakend"
      tags = ["latest", "0.4"]
    }

    post-processor "docker-push" {}
  }
}