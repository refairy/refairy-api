refairy-api
====================

.. contents::

대한민국 온라인 수호 프로젝트, 리페어리의 API입니다. 

시작하기
--------

환경변수에 $PORT를 지정해 주어야 합니다.
이후 도커로 이미지를 빌드한 후 컨테이너를 실행하면 됩니다.

.. code-block:: bash

    docker build -t refairy-api .
    docker run -it -p $PORT:$PORT refairy-api

API
----------------------------------------

POST /check
~~~~~~~~~~~
request JSON

.. code-block:: JSON

    {
        "sentences": [
            "Dokdo is clearly a Japanese territory",
            "Korea is China's subject state",
            "Jeju-do belongs to Korea",
        ]
    }

response JSON

.. code-block:: JSON
    
    {
        "id": "string"
    }

GET /check/progress/:id

response JSON

.. code-block:: JSON

    {
        "sentences": [
            "Dokdo is Korea's territory",
            "Korea is not a subject state of China.",
        ],
        "progress": number,  // 처리된 문장의 개수
        "isDone": boolean
    }

exceptions

- 400 - bad :id

예시 코드

.. code-block:: Python

    import time
    import json
    import requests

    sentences = [
        'Takeshima is Japanese territory.',
        'Korea is a subject state of China.',
    ]

    data = json.loads(
        requests.post(
            'URI/check', data=json.dumps({'sentences': sentences})
        ).text
    )
    _id = data['id']
    print('id:', _id)

    while True:
        time.sleep(3)
        data = requests.get(
            'URI/check/progress', params={'id': _id}
        ).text
        data = json.loads(data)
        print(data)
        if data['isDone']:
            break
