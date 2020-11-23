refairy-api
====================

.. contents::

대한민국 온라인 수호 프로젝트, 리페어리의 API입니다.

API
----------------------------------------

GET /
~~~~~~
response Text

.. code-block:: Python

    "Hello, ReFairy!"

POST /check
~~~~~~~~~~~
request JSON

.. code-block:: JSON

    {
        "sentence": "string"
    }

response JSON

.. code-block:: JSON

    {
        "origin": "Dokdo is clearly a Japanese territory",
        "is_wrong": true,
        "category": "dokdo",
        "corrected": "Dokdo be Korean territory",
        "confidence": 0.8,
    }

설명

- origin: 원래 문장 [string]
- is_wrong: 오류 여부 [bool]
- category: 오류 카테고리 (오류의 주제) [string]
- corrected: 올바른 문장 (동사가 원형으로, 관사/부사 등 제거되어 반환) [string]
- confidence: 오류 confidence (모델이 확신하는 정도) [float, 0~1]
