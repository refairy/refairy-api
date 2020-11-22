refairy-api
====================

.. contents::

대한민국 온라인 수호 프로젝트, 리페어리의 API입니다.

JSON 형태
----------------------------------------

- 원래 문장 [string]
- 오류 여부 [bool]
- 오류 카테고리 (오류의 주제) [string]
- 올바른 문장 (동사가 원형으로, 관사/부사 등 제거되어 반환) [string]
- 오류 confidence (모델이 확신하는 정도) [float, 0~1]

예시
----------------------------------------

.. code-block:: JSON

    {
        "origin": "Dokdo is clearly a Japanese territory",
        "is_wrong": "true",
        "category": "dokdo",
        "corrected": "Dokdo be Korean territory",
        "confidence": "0.8",
    }
