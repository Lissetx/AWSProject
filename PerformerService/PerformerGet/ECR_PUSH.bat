::.f connection is valid with login acess
aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 705517780837.dkr.ecr.us-west-1.amazonaws.com/auditonme

::Docker fun stuff
docker compose up -d

::tags and pushes to ECR
docker tag performer_get:1.0 705517780837.dkr.ecr.us-west-1.amazonaws.com/auditonme:performer_get
docker push 705517780837.dkr.ecr.us-west-1.amazonaws.com/auditonme:performer_get