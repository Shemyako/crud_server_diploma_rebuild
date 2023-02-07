# crud_server_diploma_rebuild
Переделка [дипломной работы](https://github.com/Shemyako/diploma-server). Этот сервис отвечает за crud операции с базой данных. Отдельно существует сервис с бд. Отдельно будут реализованы сервисы с авторизацией, оповещениями, формированием отчётов.

## БД
Структура базы данных не менялась, изменился способ хранения (Docker) и подключения (соответственно, к котейнеру требуется подключаться). [Гит](https://github.com/Shemyako/db-diploma-rebuild)

## Запуск
proj:

uvicorn run:app

dev:

uvicorn run:app --reload
