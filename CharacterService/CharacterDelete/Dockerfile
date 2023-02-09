FROM public.ecr.aws/lambda/python:3.8
COPY requirments.txt .
RUN pip install -r requirments.txt --target "${LAMBDA_TASK_ROOT}"
COPY character_delete.py ${LAMBDA_TASK_ROOT}
CMD ["character_delete.lambda_handler"]