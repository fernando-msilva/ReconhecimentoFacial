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

source "docker" "python" {
  image  = "python:3.8-slim-buster"
  commit = true
  changes = [
    "ENTRYPOINT [\"\"]"
  ]
}

build {
  name = "base-image"
  sources = [
    "source.docker.python"
  ]

  provisioner "shell" {
    inline = [
      "mkdir -p /opt/config /opt/modelo"
    ]
  }

  provisioner "file" {
    source = "haarcascade_frontalface_default.xml"
    destination = "/opt/config/haarcascade_frontalface_default.xml"
  }

  post-processors {
    post-processor "docker-tag" {
      repository = "gcr.io/${var.project_id}/spyface"
      tags = ["base"]
    }
    
    post-processor "docker-push" {}
  }
}