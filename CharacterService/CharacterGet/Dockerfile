FROM public.ecr.aws/lambda/python:3.8
COPY requirments.txt .
RUN pip install -r requirments.txt --target "${LAMBDA_TASK_ROOT}"
COPY character_get.py ${LAMBDA_TASK_ROOT}
CMD ["character_get.lambda_handler"]