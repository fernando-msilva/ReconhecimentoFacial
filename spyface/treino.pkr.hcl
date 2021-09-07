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

source "docker" "treino" {
  image  = "gcr.io/${var.project_id}/spyface:base"
  commit = true
  changes = [
    "WORKDIR /spyface",
    "VOLUME /spyface/storage/imagens",
    "ENTRYPOINT [\"\"]",
    "CMD [\"python\", \"-u\", \"Testagem.py\"]"
  ]
}

build {
  name = "treino-image"
  sources = [
    "source.docker.treino"
  ]

  provisioner "file" {
    source = "src"
    destination = "/spyface"
  }

  provisioner "file" {
    source = "requirements.txt"
    destination = "/requirements.txt"
  }

  provisioner "shell" {
    inline = [
      "pip install -r /requirements.txt",
      "apt-get update && apt-get install libgl1-mesa-dev libglib2.0-0 libsm6 libxrender1 libxext6 -y"
    ]
  }

  post-processors {
    post-processor "docker-tag" {
      repository = "gcr.io/${var.project_id}/treino"
      tags = ["latest", "0.2"]
    }

    post-processor "docker-push" {}
  }
}