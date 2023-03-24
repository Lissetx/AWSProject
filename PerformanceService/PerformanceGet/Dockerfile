FROM public.ecr.aws/lambda/python:3.8
COPY requirments.txt .
RUN pip install -r requirments.txt --target "${LAMBDA_TASK_ROOT}"
COPY performance_get.py ${LAMBDA_TASK_ROOT}
CMD ["performance_get.lambda_handler"]