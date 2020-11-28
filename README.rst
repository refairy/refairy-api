refairy-api
====================

.. contents::

대한민국 온라인 수호 프로젝트, 리페어리의 API입니다.

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
