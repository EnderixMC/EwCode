FROM python:3.11.2-bullseye
COPY . /ewcode
RUN echo '#!/bin/bash\npython3 /ewcode/ewcode.py "$@"' > /bin/ewcode
WORKDIR /src
ENTRYPOINT /bin/bash
