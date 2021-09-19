deploy: infracost build_all_images terraform_apply kubernetes_deploy

terraform_apply:
	@cd infra && terraform apply --var-file vars.tfvars

terraform_plan:
	@cd infra && terraform plan --var-file vars.tfvars

terraform_destroy:
	@cd infra && terraform destroy --var-file vars.tfvars

infracost:
	@cd infra && infracost breakdown --path . --terraform-plan-flags "--var-file vars.tfvars"

build_all_images: dockerhub_auth build_base build_krakend build_api build_train

dockerhub_auth:
	@echo $(TOKEN) | docker login -u $(REPOSITORY) --password-stdin

build_krakend:
	@cd krakend && docker image build -t $(REPOSITORY)/krakend:0.1 . && docker image push $(REPOSITORY)/krakend:0.1
	@docker image tag $(REPOSITORY)/krakend:0.1 $(REPOSITORY)/krakend:latest && docker image push $(REPOSITORY)/krakend:latest

build_base:
	@cd base-image && docker image build -t $(REPOSITORY)/spyface-base:0.1 . && docker image push $(REPOSITORY)/spyface-base:0.1
	@docker image tag $(REPOSITORY)/spyface-base:0.1 $(REPOSITORY)/spyface-base:latest && docker image push $(REPOSITORY)/spyface-base:latest

build_train:
	@cd train && docker image build -t $(REPOSITORY)/spyface-train:0.1 --build-arg REPOSITORY=$(REPOSITORY) . && docker image push $(REPOSITORY)/spyface-train:0.1
	@docker image tag $(REPOSITORY)/spyface-train:0.1 $(REPOSITORY)/spyface-train:latest && docker image push $(REPOSITORY)/spyface-train:latest

build_api:
	@cd api && docker image build -t $(REPOSITORY)/spyface-api:0.1 --build-arg REPOSITORY=$(REPOSITORY) . && docker image push $(REPOSITORY)/spyface-api:0.1
	@docker image tag $(REPOSITORY)/spyface-api:0.1 $(REPOSITORY)/spyface-api:latest && docker image push $(REPOSITORY)/spyface-api:latest

kubernetes_deploy: kubernetes_credential kubernetes_apply

kubernetes_credential:
	@gcloud container clusters get-credentials spyface-cluster --region us-central1 --project $(PROJECT)

kubernetes_apply:
	@kubectl apply -f kubernetes/