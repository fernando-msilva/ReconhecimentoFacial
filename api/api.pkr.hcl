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

source "docker" "api" {
  image  = "gcr.io/${var.project_id}/spyface:base"
  commit = true
  changes = [
    "ENTRYPOINT [\"\"]",
    "CMD [\"uvicorn\", \"spyface.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8080\"]"
  ]
}

build {
  name = "api-image"
  sources = [
    "source.docker.api"
  ]

  provisioner "file" {
    source = "src/spyface"
    destination = "/spyface"
  }

  provisioner "file" {
    source = "src/config"
    destination = "/config"
  }

  provisioner "file" {
    source = "requirements.txt"
    destination = "/requirements.txt"
  }

  provisioner "shell" {
    inline = [
      "chmod +x /config/system_config.sh",
      "/config/system_config.sh",
      "pip install -r /requirements.txt",
      "apt-get update && apt-get install libgl1-mesa-dev libglib2.0-0 libsm6 libxrender1 libxext6 -y"
    ]
  }

  post-processors {
    post-processor "docker-tag" {
      repository = "gcr.io/${var.project_id}/api"
      tags = ["latest", "0.1"]
    }

    post-processor "docker-push" {}
  }
}