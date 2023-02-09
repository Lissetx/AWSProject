FROM public.ecr.aws/lambda/python:3.8
COPY requirments.txt .
RUN pip install -r requirments.txt --target "${LAMBDA_TASK_ROOT}"
COPY user_post.py ${LAMBDA_TASK_ROOT}
CMD ["user_post.lambda_handler"]