::.f connection is valid with login acess
aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 705517780837.dkr.ecr.us-west-1.amazonaws.com/auditonme

::Docker fun stuff
docker compose up -d

::tags and pushes to ECR
docker tag performance_post:1.0 705517780837.dkr.ecr.us-west-1.amazonaws.com/auditonme:performance_post
docker push 705517780837.dkr.ecr.us-west-1.amazonaws.com/auditonme:performance_post