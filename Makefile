deploy: infracost build_all_images terraform_apply kubernetes_deploy

terraform_apply:
	@cd infra && terraform apply --var-file vars.tfvars

terraform_plan:
	@cd infra && terraform plan --var-file vars.tfvars

terraform_destroy:
	@cd infra && terraform destroy --var-file vars.tfvars

infracost:
	@cd infra && infracost breakdown --path . --terraform-plan-flags "--var-file vars.tfvars"

build_all_images: docker_auth build_base build_krakend build_api build_train

docker_auth:
	@gcloud auth configure-docker --quiet

build_krakend:
	@cd krakend && packer init . && packer build -var project_id=$(PROJECT) .

build_base:
	@cd imagem-base && packer init . && packer build -var project_id=$(PROJECT) .

build_train:
	@cd spyface && packer init . && packer build -var project_id=$(PROJECT) .

build_api:
	@cd api && packer init . && packer build -var project_id=$(PROJECT) .

kubernetes_deploy: kubernetes_credential kubernetes_apply

kubernetes_credential:
	@gcloud container clusters get-credentials spyface-cluster --region us-central1 --project $(PROJECT)

kubernetes_apply:
	@kubectl apply -f kubernetes/